from dataclasses import dataclass
from typing import List
from datetime import date, datetime


@dataclass
class NewProject:
    name: str = None


@dataclass
class Project(NewProject):
    id: int = None
    comment_count: int = None
    order: int = None
    indent: int = None
