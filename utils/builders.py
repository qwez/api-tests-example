import model
from datetime import date, datetime


class TaskBuilder:

    def __init__(self):
        self._task = model.NewTask()

    def with_content(self, content: str):
        self._task.content = content
        return self

    def with_project_id(self, id: int):
        self._task.project_id = id
        return self

    def with_order(self, order: int):
        self._task.order = order
        return self

    def add_label_id(self, id: int):
        if self._task.label_ids is None:
            self._task.label_ids = list()
        self._task.label_ids.append(id)
        return self

    def with_priority(self, priority: int):
        self._task.priority = priority
        return self

    def with_due_datetime(self, year: int, month: int, day: int, hours: int, minutes: int):
        self._task.due_datetime = datetime(year, month, day, hours, minutes)
        return self

    def with_due_date(self, year: int, month: int, day: int):
        self._task.due_date = date(year, month, day)
        return self

    def with_due_date_string(self, date: str):
        self._task.due_string = date
        return self

    def with_due_lang(self, lang: str):
        self._task.due_lang = lang
        return self

    def build(self) -> model.NewTask:
        return self._task

    @staticmethod
    def new():
        return TaskBuilder()


class DueBuilder:

    def __init__(self):
        self._due = model.Due()

    def with_date(self, year: int, month: int, day: int):
        self._due.date = date(year, month, day)
        return self

    def with_recurring(self, recurring: bool):
        self._due.recurring = recurring
        return self

    def with_string(self, string: str):
        self._due.string = string
        return self

    def build(self) -> model.Due:
        return self._due

    @staticmethod
    def new():
        return DueBuilder()


class ProjectBuilder:

    def __init__(self):
        self._project = model.NewProject()

    def with_name(self, name: str):
        self._project.name = name
        return self

    def build(self):
        return self._project

    @staticmethod
    def new():
        return ProjectBuilder()
