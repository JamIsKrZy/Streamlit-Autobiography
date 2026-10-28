import streamlit as st


st.title("About Me")
st.write(
    "I am a self-taught developer who learns best through practical experience. I develop my expertise by directly implementing concepts to real-world software and practical systems, rather than relying on theoretical readings. I have recently finished my second year of college, where I have successfully balanced my academic foundation with ongoing self-directed learning to remain at the forefront of industry standards. "
    "I possess a strong sense of curiosity and am dedicated to providing real value. As things change, communication is essential to maintaining a team on the same page, and I'm continually seeking ways to grow better at communicating so that I can collaborate with others. My technical execution instantly benefits from this focus on efficiency and simplicity. I deliberately design and set up my workflows to improve productivity and reduce friction when doing critical tasks. I am enthusiastic about the prospect of broadening my capabilities in the workplace and am eager to delve into entirely new technical domains in order to further enhance my skills in this field."
    "I am still deepening my technical toolkit by studying System Design and DevOps to understand how applications operate. Driven by my focus on efficiency, I am also actively exploring AI Agents to see how automated tools can be integrated to optimize modern development pipelines."
)

st.header("Education")
with st.container(border=True):
    st.subheader("BS Computer Science")
    st.write("Cebu Institute of Technology - University, Cebu City, Cebu · Graduate by: 2028")

with st.container(border=True):
    st.subheader("TVL-ICT SHS HighSchool")
    st.write("University of San Jose - Recoletos, Basak Campus. Cebu City, Cebu · Graduated: 2024")

with st.container(border=True):
    st.subheader("JHS HighSchool")
    st.write("University of San Jose - Recoletos, Basak Campus. Cebu City, Cebu · Graduated: 2022")


st.header("Experience")
with st.container(border=True):
    st.subheader("Quality Tester Intern")
    st.write("Symph (remote) · JAN 2024 - MAR 2025")
    
    st.write(
        "Executed functional, regression, and user acceptance testing for enterprise-grade web and mobile applications. "
        "Developed and executed automated test scripts using Playwright to improve testing efficiency for web applications."
        "Participated in Agile sprint planning, standups, and retrospectives to streamline the software development lifecycle."
    )

