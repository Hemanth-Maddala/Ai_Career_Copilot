from dotenv import load_dotenv
load_dotenv()

import os
from crew import run_crew

if __name__ == "__main__":
    user_input = {
        "name": "Hemanth",
        "skills": ["python", "matplotlib","seaborn","numpy","pandas"],
        "goal": "Machine Learning",
        "timeframe": "4 months"
    }

    result = run_crew(user_input)
    print("\nFINAL OUTPUT:\n")
    print(result)   