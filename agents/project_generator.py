#---------------- IMPORTS ----------------#
import os
from crewai import Agent,LLM
from crewai_tools import GithubSearchTool

#---------------- GEMINI LLM ----------------#
# llm = LLM(
#     model="gemini/gemini-2.5-flash",
#     api_key="",  # Or set GOOGLE_API_KEY/GEMINI_API_KEY
#     temperature=0.7
# )

#---------------- OLLAMA LLM ----------------#
llm = LLM(model="ollama/llama3.1")


#---------------- GITHUB TOOL ----------------#
# tool_github = GithubSearchTool(
#     gh_token=os.getenv("GITHUB_TOKEN"),
#     content_types=["code", "repo"]
# )

#---------------- AGENT ----------------#
project_generator = Agent(
            role="Senior Software Architect",
            goal="Design unique portfolio projects that demonstrate Senior-level engineering skills.",
            backstory=(
                "You hate generic 'Todo' apps. You design systems. Your projects focus on scalability, "
                "database optimization, and real-world edge cases. You want to see projects that "
                "make an interviewer say, 'Wow, you actually handled race conditions here?'"
            ),
            llm=llm,
            verbose=True,
            allow_delegation=False,
            # tools=[tool_github]
        )