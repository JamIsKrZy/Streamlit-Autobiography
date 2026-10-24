import streamlit as st





st.set_page_config(page_title="James O. Samson", page_icon="👋", layout="centered")

pages = [
    st.Page("home.py", title="Home", icon="👋", default=True),
    st.Page("about_me.py", title="About Me", icon="👋"),
    st.Page("portfolio.py", title="Portfolio", icon="🗂️"),
    st.Page("projects.py", title="Projects", icon="🛠️"),
]

navigation = st.navigation(pages, position="top")





def main() -> None:
    navigation.run()


if __name__ == "__main__":
    main()
