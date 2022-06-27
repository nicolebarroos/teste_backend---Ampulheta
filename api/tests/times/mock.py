import pytest

from api.models import User, Project


@pytest.fixture
def user(db) -> User:
    return User.objects.create(email="administrador@gmail.com", username="Administrador", password="81662527")


@pytest.fixture
def project(user) -> Project:
    return Project.objects.create(title="Cardápio digital", description="Projeto voltado a criação de cardápios digitais")