from crewai import Crew, Process
from tasks.analysis_task import get_analysis_task
from tasks.strategy_task import get_strategy_task
from tasks.project_task import get_project_task

from agents.project_generator import project_generator
from agents.skill_analyzer import skill_analyzer
from agents.strategist import strategist


def run_crew(user_input):
    analysis = get_analysis_task(user_input)
    strategy = get_strategy_task(user_input,analysis)
    projects = get_project_task(user_input,strategy)

    crew = Crew(
        agents=[project_generator, skill_analyzer, strategist],
        tasks=[analysis, strategy, projects],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    return result