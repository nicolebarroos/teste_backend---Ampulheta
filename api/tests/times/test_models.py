import pytest

from api.models import Time
from api.tests.times.mock import user, project


@pytest.mark.django_db
def test_time_model(user, project):
    time = Time(started_at="2022-06-24T12:30:59.000000", ended_at="2022-06-24T21:30:59.000000", user=user, project=project)

    assert time.started_at == "2022-06-24T12:30:59.000000"
    assert time.ended_at == "2022-06-24T21:30:59.000000"
    assert time.user == user
    assert time.project == project
    assert str(time) == time.started_at
