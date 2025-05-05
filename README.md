Title: Student's DataBase Management System
Description
This SQL script creates a database for managing students and their course enrollments.
It includes the creation of tables for students, courses, and enrollments, along with some sample data.
The script assumes the use of MySQL or a compatible database system.
This script is created by Angela Chinweike, a student of Power Learn Projectb Academy,  Software Engineering program.

Title: Manage Tasks App

Hey Besties!

This is a simple FastAPI app I built to manage tasks — you can create, read, update, and delete (CRUD) tasks using a MySQL database.

What this project does
✅ Create a new task (title, description, status)

✅ Get all tasks

✅ Get a task by ID

✅ Update a task

✅ Delete a task

Basically, it’s a small backend project that lets you handle your to-do list like a pro!


Tech stack used
FastAPI → to build the API endpoints

MySQL → to store the tasks

mysql-connector-python → to connect FastAPI to the MySQL database

python-dotenv → to hide sensitive info like my database password (.env file)

How I set it up
Database (managetasks.sql)

I created two tables:

users → stores user details (user_id, username, email)

tasks → stores tasks (task_id, user_id, title, description, is_completed)

API app (main.py)

I built FastAPI routes to:

Create a task → POST /tasks/

Read all tasks → GET /tasks/

Read one task → GET /tasks/{task_id}

Update a task → PUT /tasks/{task_id}

Delete a task → DELETE /tasks/{task_id}

Database connection (database.py)

I made a function get_db() to handle connecting to the MySQL database.



Hiding my password

Instead of writing the password directly in the code (which is risky 😬), I used:

python-dotenv → reads values like DB host, user, password from a .env file.

.env file → stores the sensitive info (DB_HOST, DB_USER, DB_PASSWORD, etc.)

.gitignore → makes sure I never accidentally upload .env to GitHub!


Example .env file
ini
Copy
Edit
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=****** (Your actual password shows in here but is hidden in database.py where it should have been)
DB_NAME=managetasks

How to run the project
Install requirements:

bash- This simply means that you should run this comman using Git Bash
Copy
Edit
pip install -r requirements.txt
Run the FastAPI app:


bash
Copy
Edit
uvicorn main:app --reload
Visit the API docs:

arduino
Copy
Edit
http://127.0.0.1:8000/docs
Notes
Don’t forget to create the MySQL database and run the SQL script (managetasks.sql) before starting the app.

Always add .env to your .gitignore so your password is safe when you push to GitHub.

Why I did this
I wanted to:

Practice FastAPI and MySQL integration

Understand how to handle CRUD operations

Learn how to protect sensitive data using .env