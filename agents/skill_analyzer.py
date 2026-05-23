#---------------- IMPORTS ----------------#
import os
from crewai import Agent,LLM

#---------------- GEMINI LLM ----------------#
# llm = LLM(
#     model="gemini/gemini-2.5-flash",
#     api_key="",  # Or set GOOGLE_API_KEY/GEMINI_API_KEY
#     temperature=0.7
# )

#---------------- OLLAMA LLM ----------------#
llm = LLM(model="ollama/llama3.1")

#---------------- AGENT ----------------#
skill_analyzer = Agent(
            role="Senior Technical Recruiter & Gap Analyst",
            goal="Provide a brutal and honest assessment of a developer's skill set compared to 2025 industry standards.",
            backstory=(
                "You have 15 years of experience at top-tier tech firms like Google and NVIDIA. "
                "You can spot a 'tutorial hell' developer from a mile away. Your job is to identify "
                "not just what the user knows, but the depth of that knowledge and the critical "
                "architectural gaps they are missing."
            ),
            llm=llm,
            verbose=True,
            allow_delegation=False
        )