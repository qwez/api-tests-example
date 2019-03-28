"""
Implements interface to get, create, delete data from Todoist application
Better practice is to do so in DB directly, but this is no possible in current case
"""

from app.app import TodoistApp
from model.task import Task
from utils.builders import TaskBuilder
from faker import Faker


class TodoistData:

    @staticmethod
    def get_task(id: int) -> Task:
        # should be implemented by fetching from DB
        return TodoistApp.task().get(id).model

    @staticmethod
    def create_task() -> Task:
        # should be implemented by inserting to DB
        return TodoistApp.task().create(TaskBuilder().with_content(Faker().sentence()).build()).model

    @staticmethod
    def check_task(id: int) -> bool:
        # should be implemented by fetching from DB
        return TodoistApp.task().get(id).code != 404

    @staticmethod
    def delete_task(id: int):
        # should be implemented by deleting from DB
        TodoistApp.task().delete(id)

    @staticmethod
    def delete_project(id: int):
        # should be implemented by deleting from DB
        TodoistApp.project().delete(id)
