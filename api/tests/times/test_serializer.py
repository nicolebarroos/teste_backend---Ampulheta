import pytest
from api.tests.times.mock import user, project
from api.serializers import TimeSerializer


@pytest.mark.django_db
def test_valid_time_serializer(user, project):
    valid_serializer_data = {
        "started_at": "2022-02-14T03:00:00Z",
        "ended_at": "2022-02-14T04:00:00Z",
        "user": user.id,
        "project": project.id
    }

    serializer = TimeSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


@pytest.mark.django_db
def test_invalid_time_serializer(user, project):
    invalid_serializer_data = {
        "started_at": "2022-02-14T03:00:00Z",
        "user": user.id,
        "project": project.id
    }

    serializer = TimeSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"ended_at": ["This field is required."]}