#---------------- IMPORTS ----------------#
from crewai import Agent,LLM
from crewai_tools import SerperDevTool

#---------------- GEMINI LLM ----------------#
# llm = LLM(
#     model="gemini/gemini-2.5-flash",
#     api_key="",  # Or set GOOGLE_API_KEY/GEMINI_API_KEY
#     temperature=0.7
# )

#---------------- OLLAMA LLM ----------------#
llm = LLM(model="ollama/llama3.1")

#---------------- SERPDEV TOOL ----------------#
# tool_search = SerperDevTool()

#---------------- AGENT ----------------#
strategist = Agent(
            role="Tech Career Growth Strategist",
            goal="Design a hyper-efficient, 3-month roadmap that prioritizes high-ROI skills.",
            backstory=(
                "You specialize in 'Speed to Market.' You know exactly which skills get people hired "
                "and which are a waste of time. You create roadmaps that balance theory with hands-on "
                "application, ensuring learners don't burn out."
            ),
            llm=llm,
            verbose=True,
            allow_delegation=False,
            # tools=[tool_search]
        )