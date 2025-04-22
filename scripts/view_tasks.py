# view_tasks.py

from app.database import SessionLocal
from app.models import Task

# Get a database session
db = SessionLocal()

# Fetch all tasks
tasks = db.query(Task).all()

# Print each task
for task in tasks:
    print(f"ID: {task.id} | Name: {task.name} | Status: {task.status}")
