from crewai import Task
from agents.project_generator import project_generator
from schema.project_schema import ProjectOutput


def get_project_task(user_input, context_task):
    return Task(
        description=f"""
Generate 3 unique, high-impact project ideas based on the user's profile.

User Data:
{user_input}

IMPORTANT:
- Use the GitHub tool to explore real-world repositories
- Analyze existing production-level projects
- Take inspiration from real systems (not tutorials)
- Do NOT generate generic ideas

Constraints:
- Projects must align with the roadmap provided in context
- Projects must use relevant modern tech stacks
- Each project must solve a real-world problem (FinTech, HealthTech, DevTools, etc.)
- Each project must include a strong system design component

For each project, include:
- name
- description
- tech_stack
- system_design_focus
- difficulty

Use the roadmap context to guide complexity and progression.
""",
        expected_output="A structured list of 3 real-world, portfolio-ready projects.",
        agent=project_generator,
        context=[context_task],
        output_pydantic=ProjectOutput
    )