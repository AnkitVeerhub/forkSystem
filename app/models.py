# app/models.py

from sqlalchemy import Column, String, DateTime
from datetime import datetime
from uuid import uuid4
from .database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    name = Column(String, index=True)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
