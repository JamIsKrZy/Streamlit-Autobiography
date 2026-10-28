import streamlit as st


st.title("Portfolio")

st.header("Skills")
testing_skills, tools = st.columns(2)
with testing_skills:
    st.subheader("Testing & Development")
    st.markdown(
        """
        - Manual Testing
        - Regression Testing
        - Automation Testing
        - Sanity Testing
        - E2E Testing
        - API Testing
        - Agile Development
        - Debugging
        - Observant
        - Web Development
        - Adaptability
        """
    )
with tools:
    st.subheader("Tools & Technologies")
    st.markdown(
        """
        - Playwright
        - Cypress
        - Postman
        - Jira
        - Docker
        - Node.js
        - Python
        - Express.js
        - Linux
        - Git
        - PostgreSQL
        - MySQL
        - GitHub
        - Java
        - React
        - HTML/CSS/JS
        """
    )

st.header("Experience")
with st.container(border=True):
    st.subheader("Quality Tester Intern")
    st.write("Symph · Remote · January 2024 – March 2025")
    st.markdown(
        """
        - Executed functional, regression, and user acceptance testing for enterprise-grade web and mobile applications.
        - Developed and executed automated test scripts using Playwright to improve testing efficiency for web applications.
        - Participated in Agile sprint planning, standups, and retrospectives to streamline the software development lifecycle.
        """
    )

st.header("Leadership & Activities")
with st.container(border=True):
    st.subheader("GameJam 2025 Champion")
    st.markdown(
        "[Sugbuanon Saga: Game Jam 2025](https://itch.io/jam/sugbuanon-saga-game-jam-2025) "
        "· Project Manager / System Developer · November 2025"
    )
    st.markdown(
        """
        - Structured development pipelines, managed project milestones, and facilitated team upskilling under tight event constraints.
        - Delegated tasks based on member skillsets to ensure optimal resource allocation and project completion.
        """
    )

with st.container(border=True):
    st.subheader("Human Resource Evaluator")
    st.write("GDGoC - CITU · Evaluator · 2024–2025")
    st.markdown(
        """
        - Coordinated logistics, documentation, and operations for technical workshops and developer sessions.
        - Managed member performance evaluation records to support organizational growth and engagement.
        """
    )

with st.container(border=True):
    st.subheader("SHS CARITAS DAYS")
    st.write(
        "University of San Jose - Recoletos · Technology Cluster Academic Chairman · 2024"
    )
    st.markdown(
        """
        - Led the Technology Cluster academic division, monitoring member progress.
        - Facilitated student learning as a substitute teacher by delivering structured technical lessons and instructional content.
        """
    )

with st.container(border=True):
    st.subheader("SHS Org Strand Officer")
    st.write(
        "University of San Jose - Recoletos · TVL-Build and Inspire · "
        "Co-Executive Head · 2022–2024"
    )
    st.markdown(
        """
        - Awarded the Best Leadership Award for exceptional organizational management and performance.
        - Oversaw project deadlines, task execution, and proactive planning for organization-wide events and sessions.
        """
    )

with st.container(border=True):
    st.subheader("BSP Leadership")
    st.write(
        "University of San Jose - Recoletos · Scribe / Quartermaster · 2019–2020"
    )
    st.markdown(
        """
        - Managed unit logistics, equipment inventory, and organizational documentation for local scout operations.
        - Led field formations and developed rapid, adaptable decision-making skills during team-based activities.
        """
    )

st.header("Contact")
st.write("jamesosamson322@gmail.com")
