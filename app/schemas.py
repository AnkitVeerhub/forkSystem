# app/schemas.py

from pydantic import BaseModel, Field, UUID4
from datetime import datetime

# Base schema
class TaskBase(BaseModel):
    name: str
    status: str = "pending"

# Create schema (inherits TaskBase)
class TaskCreate(TaskBase):
    pass

# Update schema
class TaskUpdate(BaseModel):
    name: str | None = None
    status: str | None = None

# Output schema
class TaskOut(TaskBase):
    id: UUID4
    created_at: datetime

    class Config:
        from_attributes = True
