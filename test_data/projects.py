import pytest
from faker import Faker
from utils.builders import ProjectBuilder
from model.project import Project


@pytest.fixture
def project_id(todoist_project):
    project: Project = todoist_project.create(
        ProjectBuilder.new().with_name(
            Faker().sentence(nb_words=3)
        ).build()
    ).model
    yield project.id
