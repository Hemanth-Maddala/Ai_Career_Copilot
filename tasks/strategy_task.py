from crewai import Task
from agents.strategist import strategist
from schema.strategy_schema import StrategyOutput


def get_strategy_task(user_input, context_task):
    return Task(
        description=f"""
Create a roadmap based on the user's profile:

User Data:
{user_input}

IMPORTANT:
- Use the search tool to find current industry trends (2025)
- Base your roadmap on real-world demand
- Do NOT rely only on internal knowledge

Instructions:
- Create a roadmap for {user_input.get("timeframe", "3 months")}
- Break it down by month
- Ensure Month 1 focuses on fixing the most critical skill gaps
- Focus on depth over breadth
- Make it practical and job-oriented

Use the previous analysis as context.
""",
        expected_output="A structured roadmap with clear monthly milestones.",
        agent=strategist,
        context=[context_task],
        output_pydantic=StrategyOutput
    )