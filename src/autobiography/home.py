from pathlib import Path

import streamlit as st


ASSETS_DIR = Path(__file__).parent / "assets"
COVER_IMAGE = ASSETS_DIR / "cover.jpg"
PROFILE_IMAGE = ASSETS_DIR / "profile.jpg"

st.markdown(
    """
    <style>
    .cover-placeholder {
        height: 230px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
        background: linear-gradient(120deg, #dbeafe, #e2e8f0);
        color: #334155;
        font-size: 1.1rem;
    }
    .profile-placeholder {
        width: 150px;
        height: 150px;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 4px solid white;
        border-radius: 50%;
        background: #cbd5e1;
        color: #334155;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if COVER_IMAGE.is_file():
    st.image(str(COVER_IMAGE), use_container_width=True)
else:
    st.markdown(
        '<div class="cover-placeholder">Cover image placeholder</div>',
        unsafe_allow_html=True,
    )

profile_col, text_col = st.columns([1, 4], vertical_alignment="center")

with profile_col:
    if PROFILE_IMAGE.is_file():
        st.image(str(PROFILE_IMAGE), width=150)
    else:
        st.markdown(
            '<div class="profile-placeholder">1:1 profile photo</div>',
            unsafe_allow_html=True,
        )

with text_col:
    st.title("James O. Samson")

st.subheader("Software Engineer / Game  Developer  / Quality Assurance")
st.write("I am a self-driven learner who excels at learning through direct practical application. \
    Driven by a strong sense of fulfilling a role, I focus on delivering work value by being self initiative.\
    My experience working with multi-functional teams has shown me that maintaining coordination and preventing \
    gaps between different departments requires clear and direct communication and a common technical vocabulary. \
    I purposefully design my workflows in order to boost productivity, minimize friction, and maximize efficiency, \
    and also open to feedback on my performance. I enjoy exchanging those insights with the team to foster an environment \
    of continuous team development"
)
st.caption("📍 Talisay City, Cebu  ·  Studies Bachelor of  Science in Computer Science")

st.divider()
# st.header("A little about me")
# st.write("[Share a few things you would like visitors to know first.]")

left_column, right_column = st.columns(2)
with left_column:
    st.subheader("What I do")
    st.write("Currently exploring on different tech fields")
with right_column:
    st.subheader("What I enjoy")
    st.write("-Badminton")
    st.write("-Jogging")
    st.write("-Biking")
    st.write("-Video Games")


