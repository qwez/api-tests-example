from app.app import TodoistApp
import pytest
import allure


class TestGetTask:

    @allure.title('Test get all tasks')
    def test_get_all(self, todoist_task, task_ids, data_to_be_deleted):
        response = todoist_task.get_all()
        assert response.code == 200

        tasks = response.model
        expected_tasks = list(task_ids)
        actual_tasks = tuple(task.id for task in tasks)
        for task_id in task_ids:
            assert task_id in actual_tasks
            expected_tasks.remove(task_id)
        assert not expected_tasks

        # delete created task only if success
        data_to_be_deleted['tasks'] += list(task_ids)

    @allure.title('Test get one task')
    def test_get_one(self, todoist_task, task_id: int, data_to_be_deleted):
        response = todoist_task.get(task_id)
        assert response.code == 200

        task = response.model
        assert task.id == task_id

        # delete created task only if success
        data_to_be_deleted['tasks'].append(task_id)
