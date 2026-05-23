# ✨ AI Career Copilot

An AI-powered multi-agent career assistant built using CrewAI, Ollama, Streamlit, and Pydantic.

This project helps users generate:

* 📊 Skill Gap Analysis
* 🗺️ Personalized Learning Roadmaps
* 🚀 Real-World Portfolio Projects

using a team of autonomous AI agents working collaboratively.

---

# 🚀 Features

## 🧠 Multi-Agent System with CrewAI

This project uses multiple specialized AI agents:

| Agent             | Responsibility                                     |
| ----------------- | -------------------------------------------------- |
| Skill Analyzer    | Analyzes strengths, weaknesses, and missing skills |
| Career Strategist | Creates personalized learning roadmaps             |
| Project Generator | Suggests real-world portfolio projects             |

---

## 📊 Structured Outputs with Pydantic

All agent responses are converted into structured schemas using Pydantic models.

Examples:

* SkillAnalysis
* StrategyOutput
* ProjectOutput

---

## 🎨 Streamlit Frontend

Interactive UI built with Streamlit:

* User-friendly inputs
* Dynamic roadmap display
* Project cards
* Market relevance score
* Expandable learning plans

---

## 🤖 Local LLM Support (Ollama)

Currently using:

* `llama3.1`

via Ollama for completely local inference.

Future support planned:

* Gemini
* Tool-enabled agents
* GitHub search integration
* Web research tools

---

# 🏗️ Tech Stack

* Python
* CrewAI
* Streamlit
* Ollama
* Pydantic
* CrewAI Tools
* Gemini (planned)
* GitHub Tools (planned)

---

# 📂 Project Structure

```bash
AI_Career_Copilot/
│
├── agents/
│   ├── skill_analyzer.py
│   ├── strategist.py
│   └── project_generator.py
│
├── tasks/
│   ├── analysis_task.py
│   ├── strategy_task.py
│   └── project_task.py
│
├── schema/
│   ├── skill_schema.py
│   ├── strategy_schema.py
│   └── project_schema.py
│
├── crew.py
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone <your_repo_url>
cd AI_Career_Copilot
```

---

## 2️⃣ Create Virtual Environment

```bash
conda create -n ai-service python=3.11
conda activate ai-service
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Install Ollama

Download Ollama:

* https://ollama.com/

Pull model:

```bash
ollama pull llama3.1
```

Run Ollama locally before starting the app.

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 🧠 Concepts Used

* Multi-Agent Systems (MAS)
* ReAct Pattern
* Structured Outputs
* Agent Collaboration
* Sequential Task Execution
* AI Workflow Orchestration

---

# 🔮 Future Improvements

* ✅ Gemini Integration
* ✅ GitHub Search Tool
* ✅ SerperDev Search Tool
* ✅ Resume Upload Support
* ✅ PDF Export
* ✅ Modern Dashboard UI
* ✅ Memory-enabled Agents
* ✅ Human-in-the-loop Approval

---

# 📚 Learn More About CrewAI

Official CrewAI Documentation:

CrewAI GitHub Repository: https://docs.crewai.com/en/introduction

---

# 💡 What is CrewAI?

CrewAI is an open-source framework for orchestrating autonomous AI agents and building complex workflows. It enables developers to create collaborative multi-agent systems with structured task execution, memory, tools, and workflows.

---

# 📌 Current Status

✅ Core Multi-Agent Workflow Completed
✅ Structured Outputs Completed
✅ Streamlit UI Integrated
🚧 Advanced Tool Integration In Progress

---

# 👨‍💻 Author

Built as a hands-on learning project to deeply understand:

* CrewAI
* Multi-Agent Systems
* AI Workflows
* Local LLMs
* Structured AI Outputs
* Streamlit UI Integration

---
