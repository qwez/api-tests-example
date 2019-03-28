from dataclasses import dataclass
from typing import List
from datetime import date, datetime


@dataclass
class Due:
    recurring: bool = None
    string: str = None
    date: date = None
    datetime: datetime = None
    timezone: str = None


@dataclass
class BaseTask:
    project_id: int = None
    content: str = None
    completed: bool = None
    label_ids: List[int] = None
    order: int = None
    indent: int = None
    priority: int = None
    comment_count: int = None


@dataclass
class NewTask(BaseTask):
    due_string: str = None
    due_date: date = None
    due_datetime: datetime = None
    due_lang: str = None


@dataclass
class Task(BaseTask):
    id: int = None
    due: Due = None
    url: str = None
