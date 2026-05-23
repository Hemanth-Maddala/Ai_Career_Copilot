import streamlit as st
from crew import run_crew
import streamlit.components.v1 as components

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Career Copilot", layout="wide")

# ---------------- HEADER ----------------
st.markdown(
    """
    <h1 style="text-align: center;">
        ✨ <span>Your Personalized Career Plan</span>
    </h1>
    <p style="text-align: center; font-size: 1.1rem; color:grey">
        <em>AI powered roadmap, learning path, and project ideas tailored for you...</em>
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- INPUT SECTION ----------------
st.subheader("📝 Enter Your Details")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("👤 Enter Your Name", placeholder="Ex: Hemanth")
    goal = st.text_input("🎯 Enter Your Goal", placeholder="Ex: Machine Learning Engineer")

with col2:
    skills = st.text_input("🛠️ Enter Your Skills", placeholder="Ex: Sklearn, Keras, Matplotlib")
    timeframe = st.text_input("⏳ Timeframe", placeholder="Ex: 3 Months / weeks")

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- BUTTON ----------------
generate = st.button("🚀 Generate Plan", type="primary")

# ---------------- OUTPUT ----------------
if generate:

    # Clean skills input
    skills_list = [s.strip() for s in skills.split(",") if s.strip()]

    user_input = {
        "name": name,
        "skills": skills_list,
        "goal": goal,
        "timeframe": timeframe
    }

    # Run Crew
    with st.spinner("🤖 Agents are working..."):
        result = run_crew(user_input)

    st.markdown("---")

    # ---------------- SUMMARY ----------------
    st.markdown("### 📌 Summary")

    components.html(
        f"""
        <div style="display:flex; gap:12px; flex-wrap:wrap; margin-top:10px;">
        
        <div style="
            background:linear-gradient(135deg,#4facfe,#00f2fe);
            color:white;
            padding:8px 16px;
            border-radius:25px;
            font-weight:500;">
            🎯 {goal}
        </div>

        <div style="
            background:linear-gradient(135deg,#43e97b,#38f9d7);
            color:black;
            padding:8px 16px;
            border-radius:25px;
            font-weight:500;">
            🛠️ {", ".join(skills_list)}
        </div>

        <div style="
            background:linear-gradient(135deg,#667eea,#764ba2);
            color:white;
            padding:8px 16px;
            border-radius:25px;
            font-weight:500;">
            ⏳ {timeframe}
        </div>

        </div>
        """,
        height=100
    )

    st.success("✅ Plan Generated!")

    # ---------------- EXTRACT DATA ----------------
    analysis = result.tasks_output[0].pydantic
    strategy = result.tasks_output[1].pydantic
    projects = result.tasks_output[2].pydantic


# ---------------- SKILL ANALYSIS (CARD STYLE) ----------------
    st.subheader("📊 Skill Analysis")

    with st.container(border=True):

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### ✅ Strengths")
            for s in analysis.strengths:
                st.success(s)

            st.markdown("#### ⚠️ Weaknesses")
            for w in analysis.weaknesses:
                st.warning(w)

        with col2:
            st.markdown("#### ❌ Missing Skills")
            for m in analysis.missing_skills:
                st.error(m)

            st.metric("📈 Market Score", f"{analysis.market_relevance_score}/100")


# ---------------- ROADMAP (TIMELINE STYLE) ----------------
    st.subheader("🗺️ Roadmap")

    for i, step in enumerate(strategy.roadmap):

        with st.container(border=True):

            st.markdown(f"#### 🟢 {step.month}")
            st.caption(step.focus_area)

            for m in step.milestones:
                st.write("✔️", m)

            if step.resources_types:
                with st.expander("📚 Resources"):
                    for r in step.resources_types:
                        st.write("•", r)


# ---------------- PROJECTS (CARD STYLE) ----------------
    st.subheader("🚀 Projects")

    for proj in projects.projects:

        with st.container(border=True):

            st.markdown(f"#### 🔹 {proj.name}")

            st.write(proj.description)

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("**🛠️ Tech Stack**")
                for tech in proj.tech_stack:
                    st.info(tech)

            with col2:
                st.markdown("**🏗️ System Design**")
                st.write(proj.system_design_focus)

                st.markdown("**📊 Difficulty**")
                st.write(proj.difficulty)