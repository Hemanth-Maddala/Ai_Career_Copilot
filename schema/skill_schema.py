from pydantic import BaseModel, Field
from typing import List

class SkillAnalysis(BaseModel):
    strengths: List[str] = Field(..., description="Technical areas where the user excels.")
    weaknesses: List[str] = Field(..., description="Existing skills that need improvement.")
    missing_skills: List[str] = Field(..., description="Critical industry-standard skills the user lacks entirely.")
    market_relevance_score: int = Field(..., description="A score from 1-100 on how job-ready the current profile is.")