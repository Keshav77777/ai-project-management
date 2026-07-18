from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field


class Task(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    project_id: str
    title: str
    description: str = ""
    status: str = "Pending"
    priority: str = "Medium"
    created_at: datetime = Field(default_factory=datetime.now)