import pytest
from rest_framework.exceptions import ErrorDetail

from rest_framework.utils import json
from rest_framework.utils.encoders import JSONEncoder

from api.serializers import ProjectSerializer


@pytest.mark.django_db
def test_valid_project_serializer():
    valid_serializer_data = {
        "title": "Cardápio digital",
        "description": "Projeto voltado a criação de cardápios digitais",
    }

    serializer = ProjectSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert json.loads(json.dumps(serializer.validated_data, cls=JSONEncoder)) == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_projec_serializer():
    invalid_serializer_data = {
        "title": "Cardápio digital",

    }

    serializer = ProjectSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"description": ["This field is required."]}
