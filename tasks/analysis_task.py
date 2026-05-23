from crewai import Task
from agents.skill_analyzer import skill_analyzer
from schema.skill_schema import SkillAnalysis


def get_analysis_task(user_input):
        return Task(
            description=(
                f"Analyze this user profile: {user_input}. \n"
                "1. Identify core technical strengths. \n"
                "2. Identify 'shallow' knowledge areas. \n"
                "3. List missing technologies required for modern high-paying roles. \n"
                "Provide a score of 1-100 based on current industry demand."
            ),
            expected_output="A deep-dive analytical report into the user's technical standing.",
            agent=skill_analyzer,
            output_pydantic=SkillAnalysis
        )