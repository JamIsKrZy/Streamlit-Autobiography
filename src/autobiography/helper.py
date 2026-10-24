PROTOTYPE_TAGS = {"prototype", "hackathon", "game-jam", "experiment", "proof-of-concept"}
from models.Project import Project 
from typing import List, Optional
import requests

def fetch_github_projects(username: str) -> List[Project]:
    url = f"https://api.github.com/users/{username}/repos"
    params = {"type": "owner", "per_page": 100, "sort": "updated"}
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        return []
        
    projects = []
    for repo in response.json():
        if repo.get("fork") or repo.get("archived"):
            continue
            
        topics = [t.lower() for t in repo.get("topics", [])]
        is_proto = any(tag in topics for tag in PROTOTYPE_TAGS)
        
        projects.append(Project(
            id=f"github_{repo['id']}",
            name=repo["name"],
            description=repo.get("description") or "No description provided.",
            url=repo["html_url"],
            language=repo.get("language") or "N/A",
            topics=topics,
            stars=repo.get("stargazers_count", 0),
            is_prototype=is_proto,
            source="github"
        ))
    return projects
