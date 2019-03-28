from app.app import TodoistApp
from utils.todoist_data import TodoistData
import allure


class TestDeleteTask:

    @allure.title('Test delete task')
    def test_delete(self, todoist_task, task_id):
        response = todoist_task.delete(task_id)
        assert response.code == 204
        assert not response.body
        assert not TodoistData.check_task(task_id)
