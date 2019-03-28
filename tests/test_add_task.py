import pytest
from utils.builders import TaskBuilder
from utils.todoist_data import TodoistData
from app.app import TodoistApp
from model.task import Task
from faker import Faker
from datetime import datetime
from test_data.tasks_due import due as due_provider
from typing import List
import allure
import requests


class TestAddTask:

    @pytest.mark.parametrize('due_date_string, due_lang, expected_date', due_provider)
    @allure.title('Test Human defined task due date')
    def test_due(self, todoist_task: TodoistApp.Tasks, due_date_string, due_lang, expected_date: datetime, data_to_be_deleted):
        task = TaskBuilder.new()\
            .with_content(Faker().sentence())\
            .with_due_date_string(due_date_string)\
            .with_due_lang(due_lang)\
            .build()

        resp = todoist_task.create(task)
        assert resp.code == 200

        created_task: Task = resp.model
        actual_task: Task = TodoistData.get_task(created_task.id)
        assert actual_task.due.datetime == expected_date

        # delete created task only if success
        data_to_be_deleted['tasks'].append(created_task.id)

    @allure.title('Test without due date')
    def test_no_due(self, todoist_task, data_to_be_deleted):
        task = TaskBuilder.new() \
            .with_content(Faker().sentence()) \
            .build()

        resp = todoist_task.create(task)
        assert resp.code == 200

        created_task: Task = resp.model
        actual_task: Task = TodoistData.get_task(created_task.id)
        assert actual_task.due is None

        # delete created task only if success
        data_to_be_deleted['tasks'].append(created_task.id)

    @allure.title('Test order tasks in project')
    def test_order_in_project(self, todoist_task, data_to_be_deleted, project_id):
        created_tasks: List[Task] = list()
        for _ in range(3):
            task = TaskBuilder.new() \
                .with_content(Faker().sentence()) \
                .with_project_id(project_id) \
                .build()
            created_tasks.append(todoist_task.create(task).model)

        for i, task in enumerate(created_tasks):
            actual_task: Task = TodoistData.get_task(task.id)
            assert actual_task.order == i + 1
            assert actual_task.project_id == project_id

        # delete created task only if success
        data_to_be_deleted['tasks'] += [task.id for task in created_tasks]
        data_to_be_deleted['projects'].append(project_id)
