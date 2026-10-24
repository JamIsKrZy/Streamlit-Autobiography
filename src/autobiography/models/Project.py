from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Project:
    id: str
    name: str
    description: str
    url: str
    language: Optional[str] = "N/A"
    topics: List[str] = field(default_factory=list)
    stars: int = 0
    is_prototype: bool = False
    source: str = "github"  # e.g., 'github', 'gitlab', 'custom'