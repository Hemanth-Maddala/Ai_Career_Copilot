from pydantic import BaseModel,Field
from typing import List

class Project(BaseModel):
    name: str
    description: str
    tech_stack: List[str]
    system_design_focus: str = Field(..., description="The architectural concept this project teaches (e.g., Microservices, Caching, etc.)")
    difficulty: str

class ProjectOutput(BaseModel):
    projects: List[Project]