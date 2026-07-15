from pydantic import BaseModel


class Milestone(BaseModel):
    title: str
    description: str


class Phase(BaseModel):
    name: str
    milestones: list[Milestone]


class ProjectPlan(BaseModel):
    project_name: str
    description: str
    timeline: str
    phases: list[Phase]