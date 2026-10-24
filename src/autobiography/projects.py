import math

import streamlit as st
import config as CONSTANTS
from typing import List, Optional

from models.Project import Project
from helper import fetch_github_projects



def load_all_projects() -> List[Project]:
    return fetch_github_projects(CONSTANTS.GITHUB_USERNAME)

def reset_pagination():
    # Setting these session states back to 1 will automatically update the st.pagination UI
    st.session_state.proto_page = 1
    st.session_state.passion_page = 1

def sort_projects(projects: List[Project], order: str) -> List[Project]:
    if order == "Most Stars":
        return sorted(projects, key=lambda p: p.stars, reverse=True)
    elif order == "A-Z":
        return sorted(projects, key=lambda p: p.name.lower())
    elif order == "Z-A":
        return sorted(projects, key=lambda p: p.name.lower(), reverse=True)
    return projects

def render_paginated_list(projects: List[Project], tab_key: str):
    if not projects:
        st.info("No projects found matching the selected filter.")
        return

    # Calculate total pages
    total_items = len(projects)
    total_pages = math.ceil(total_items / CONSTANTS.ITEMS_PER_PAGE)
    
    # Built-in pagination handling
    # The returned value is the currently selected page integer
    current_page = st.pagination(
        num_pages=max(1, total_pages), 
        default=1, 
        key=f"{tab_key}_page"
    )
    
    # Slice the list for the current page
    start_idx = (current_page - 1) * CONSTANTS.ITEMS_PER_PAGE
    end_idx = start_idx + CONSTANTS.ITEMS_PER_PAGE
    page_projects = projects[start_idx:end_idx]
    
    # Render single-column projects
    for p in page_projects:
        with st.container(border=True):
            st.subheader(p.name)
            st.write(p.description)
            
            col1, col2 = st.columns([3, 1])
            with col1:
                st.caption(f"🛠️ **{p.language}** | ⭐ {p.stars} | 🌐 {p.source.title()}")
                if p.topics:
                    st.caption("Tags: " + ", ".join([f"`{t}`" for t in p.topics[:5]]))
            with col2:
                st.markdown(f"[View Repository]({p.url})")


# --- 4. Main App Interface ---

# Initialize session state for pagination so callbacks don't throw KeyError
if 'proto_page' not in st.session_state:
    st.session_state.proto_page = 1
if 'passion_page' not in st.session_state:
    st.session_state.passion_page = 1

st.title("Unified Project Portfolio")

all_projects = load_all_projects()

tech_stack = sorted({
    tech
    for p in all_projects
    for tech in ([p.language] if p.language != "N/A" else []) + p.topics
})

# Filter and Sorting UI
col1, col2 = st.columns([3, 1])
with col1:
    st.write("##### Filter by Language or Tool:")
    selected_tech = st.pills(
        label="Filter by Language or Tool",
        options=["All"] + tech_stack,
        default="All",
        label_visibility="collapsed",
        key="tech_filter",
        on_change=reset_pagination  
    )
with col2:
    sort_order = st.selectbox(
        "Sort Order", 
        ["Newest First", "Most Stars", "A-Z", "Z-A"],
        key="sort_filter",
        on_change=reset_pagination  
    )

# Apply Logic: 1. Filter -> 2. Sort -> 3. Split into Categories
if selected_tech != "All":
    filtered_projects = [
        p for p in all_projects
        if selected_tech.lower() == p.language.lower() or selected_tech.lower() in p.topics
    ]
else:
    filtered_projects = all_projects

sorted_projects = sort_projects(filtered_projects, sort_order)

prototype_list = [p for p in sorted_projects if p.is_prototype]
passion_list = [p for p in sorted_projects if not p.is_prototype]

# Render Tabs
prototypes_tab, passion_tab = st.tabs(["Prototypes", "Personal & Serious Projects"])

with prototypes_tab:
    render_paginated_list(prototype_list, tab_key="proto")

with passion_tab:
    render_paginated_list(passion_list, tab_key="passion")