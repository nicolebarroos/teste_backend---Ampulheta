import pytest

from api.models import User


@pytest.mark.django_db
def test_movie_model():
    user = User(email="administrador@gmail.com", username="Administrador", password="81662527")
    user.save()
    assert user.email == "administrador@gmail.com"
    assert user.username == "Administrador"
    assert user.password == "81662527"
    assert str(user) == user.username