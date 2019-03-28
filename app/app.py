from app.api_client import HttpClient, HttpResponse
from model.task import Task, NewTask
from model.project import NewProject, Project
import config
from . import jsons
from typing import List, ClassVar
from allure import step


class TodoistApiResponse:

    def __init__(self, response: HttpResponse, cls: ClassVar):
        """
        Represents Todoist application response.
        :param response: :class:`HttpResponse` object
        :param cls: class, in which json will be deserialized to
        """
        self._response = response
        self._class = cls

    @property
    def model(self):
        """
        Parse response json
        :return: <self._class> object
        """
        if self._class is None:
            raise Exception('Cannot call mode() with model type None')
        return jsons.load(self._response.json, self._class)

    @property
    def code(self):
        return self._response.code

    @property
    def body(self):
        """
        :return: :class:`str` raw text response body
        """
        return self._response.body


class Application:
    def __init__(self):
        self._client = HttpClient(config.TodoistApi.Settings)


class TodoistApp(Application):

    @staticmethod
    def task():
        """
        Get /tasks interface
        :return: :class:`TodoistApp.Tasks` object
        """
        return TodoistApp.Tasks()

    @staticmethod
    def project():
        """
        Get /projects interface
        :return: :class:`TodoistApp.Projects` object
        """
        return TodoistApp.Projects()

    class Tasks(Application):

        @step('Get tasks')
        def get_all(self) -> TodoistApiResponse:
            response = self._base.get()
            return TodoistApiResponse(response, List[Task])

        @step('Get task')
        def get(self, task_id: int) -> TodoistApiResponse:
            response = self._base.param(task_id).get()
            return TodoistApiResponse(response, Task)

        @step('Create tasks')
        def create(self, task: NewTask) -> TodoistApiResponse:
            response = self._base.post(
                jsons.dump(task)
            )
            return TodoistApiResponse(response, Task)

        @step('Delete tasks')
        def delete(self, task_id: int) -> TodoistApiResponse:
            response = self._base.param(task_id).delete()
            return TodoistApiResponse(response, None)

        @property
        def _base(self) -> HttpClient:
            return self._client.tasks

    class Projects(Application):

        @step('Create project')
        def create(self, project: NewProject) -> TodoistApiResponse:
            response = self._base.post(
                jsons.dump(project)
            )
            return TodoistApiResponse(response, Project)

        @step("Delete project")
        def delete(self, id: int):
            response = self._base.param(id).delete()
            return TodoistApiResponse(response, None)

        @property
        def _base(self) -> HttpClient:
            return self._client.projects

