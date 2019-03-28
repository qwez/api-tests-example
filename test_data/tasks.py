import pytest
from utils.todoist_data import TodoistData
from typing import Tuple


@pytest.fixture
def task_ids(number=3) -> Tuple[int]:
    tasks = tuple(TodoistData.create_task().id for _ in range(number))
    yield tasks


@pytest.fixture
def task_id() -> int:
    task_id = TodoistData.create_task().id
    yield task_id
