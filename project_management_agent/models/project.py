from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field


class Project(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    description: str = ""
    status: str = "Planning"
    created_at: datetime = Field(default_factory=datetime.now)