from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import get_db

app = FastAPI()

# Pydantic model for tasks
class Task(BaseModel):
    user_id: int
    title: str
    description: str
    is_completed: bool

@app.post("/tasks/")
def create_task(task: Task):
    conn = get_db()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO tasks (user_id, title, description, is_completed) VALUES (%s, %s, %s, %s)",
            (task.user_id, task.title, task.description, task.is_completed)
        )
        conn.commit()
        return {"message": "Task created successfully"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()


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


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    conn = get_db()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE tasks SET user_id = %s, title = %s, description = %s, is_completed = %s WHERE task_id = %s",
            (task.user_id, task.title, task.description, task.is_completed, task_id)
        )
        conn.commit()
        return {"message": "Task updated successfully"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    conn = get_db()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM tasks WHERE task_id = %s", (task_id,))
        conn.commit()
        return {"message": "Task deleted successfully"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
