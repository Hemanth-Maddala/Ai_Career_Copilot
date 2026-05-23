from pydantic import BaseModel,Field
from typing import List

class RoadmapStep(BaseModel):
    month: str = Field(..., description="e.g., Month 1, Week 2, etc.")
    focus_area: str = Field(..., description="The main topic of study.")
    milestones: List[str] = Field(..., description="Specific tasks or achievements to complete.")
    resources_types: List[str] = Field(..., description="Suggested types of documentation or tools to use.")

class StrategyOutput(BaseModel):
    target_role: str = Field(..., description="The job role this roadmap prepares the user for.")
    roadmap: List[RoadmapStep]