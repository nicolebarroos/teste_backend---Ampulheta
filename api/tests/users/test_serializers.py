from rest_framework.utils import json
from rest_framework.utils.encoders import JSONEncoder
import pytest

from api.serializers import UserSerializer


@pytest.mark.django_db
def test_valid_movie_serializer():
    valid_serializer_data = {
        "email": "administradorgmail.com",
        "username": "Administrador",
    }
    serializer = UserSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert json.loads(json.dumps(serializer.validated_data, cls=JSONEncoder)) == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


@pytest.mark.django_db
def test_invalid_movie_serializer():
    invalid_serializer_data = {
        "email": "administradorgmail.com",
    }
    serializer = UserSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"username": ["This field is required."]}
