from app.app import TodoistApp
import pytest
import logging
from utils.todoist_data import TodoistData
from config import TodoistApi

# import other fixtures
from test_data.tasks import task_id, task_ids
from test_data.projects import project_id


def pytest_addoption(parser):
    parser.addoption("--delay", action="store", help="delay before post", default=0.5, type=float)


@pytest.fixture()
def todoist() -> TodoistApp:
    app = TodoistApp()
    yield app


@pytest.fixture()
def todoist_task(todoist) -> TodoistApp.Tasks:
    app = todoist.task()
    yield app


@pytest.fixture()
def todoist_project(todoist) -> TodoistApp.Projects:
    app = todoist.project()
    yield app


# configure thread safe logging to file
@pytest.fixture(scope='session', autouse=True)
def setup_logger(worker_id):
    logger = logging.getLogger('app.api_client.HttpClient')
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('out_{}.log'.format(worker_id), mode='w')
    handler.setFormatter(logging.Formatter('%(levelname)-8s [%(asctime)s] %(name)-15s -> %(message)s'))
    logger.addHandler(handler)


# setup delay to avoid 500 error response code from Todoist API
@pytest.fixture(scope='session', autouse=True)
def config_setup(request):
    TodoistApi.Settings.delay = request.config.getoption('delay')


# clean up fixture
@pytest.fixture(scope='session')
def data_to_be_deleted():
    data = {
        'tasks': [],
        'projects': []
    }
    yield data
    # Remove data
    for task in data['tasks']:
        TodoistData.delete_task(task)
    for project in data['projects']:
        TodoistData.delete_project(project)
