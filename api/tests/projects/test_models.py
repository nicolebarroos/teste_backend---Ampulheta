import pytest

from api.models import Project, User


@pytest.fixture
def user(db) -> User:
    return User.objects.bulk_create(
        [
            User(pk=1, email="administrador@gmail.com", username="Administrador", password="81662527"),
            User(pk=2, email="administrador2@gmail.com", username="Administrador2", password="81662527"),
            User(pk=3, email="administrador3@gmail.com", username="Administrador3", password="81662527"),
        ]
    )

@pytest.mark.django_db
def test_project_model(user):
    project = Project(title="Cardápio digital", description="Projeto voltado a criação de cardápios digitais")
    project.save()
    project.users.add(user[0], user[1], user[2])
    project.save()
    assert project.title == "Cardápio digital"
    assert project.description == "Projeto voltado a criação de cardápios digitais"
    assert project.users.values().exists()
    assert str(project.title) == project.title
