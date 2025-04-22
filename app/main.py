# app/main.py
from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from . import models, schemas
from .database import SessionLocal, engine
import uuid  # Import UUID module

# Create tables on startup
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Unix Fork-Inspired Task Manager")

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to create a new task
@app.post("/tasks", response_model=schemas.TaskOut)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.Task(name=task.name)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Route to list all tasks
@app.get("/tasks", response_model=list[schemas.TaskOut])
def list_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return tasks

# Route to update a task by UUID
@app.patch("/tasks/{task_id}", response_model=schemas.TaskOut)
def update_task(task_id: uuid.UUID, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    # Update task fields
    if task.name:
        db_task.name = task.name
    if task.status:
        db_task.status = task.status

    db.commit()
    db.refresh(db_task)
    return db_task
