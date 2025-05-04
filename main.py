from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import get_db  # Import from your database.py

app = FastAPI()

# Pydantic model for tasks
class Task(BaseModel):
    title: str
    description: str
    is_completed: bool

# Create a new task
@app.post("/tasks/")
def create_task(task: Task):
    conn = get_db()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, description, is_completed) VALUES (%s, %s, %s)",
        (task.title, task.description, task.is_completed)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Task created successfully"}

# Get all tasks
@app.get("/tasks/")
def read_tasks():
    conn = get_db()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return tasks

# Get a single task by ID
@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    conn = get_db()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tasks WHERE task_id = %s", (task_id,))
    task = cursor.fetchone()
    cursor.close()
    conn.close()
    if task:
        return task
    raise HTTPException(status_code=404, detail="Task not found")

# Update a task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    conn = get_db()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET title = %s, description = %s, is_completed = %s WHERE task_id = %s",
        (task.title, task.description, task.is_completed, task_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Task updated successfully"}

# Delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    conn = get_db()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE task_id = %s", (task_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Task deleted successfully"}
