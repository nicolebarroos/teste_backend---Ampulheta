import json

import pytest
from rest_framework.test import APITestCase, force_authenticate
from api.models import User
from rest_framework.authtoken.models import Token


@pytest.mark.django_db
class TestUserAPI(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='Administrador', password='81662527')

    def test_authentification(self):
        request = self.client.post('http://localhost:8000/api/v1.0/users/authenticate/',
                                  {
                                      "username": "Administrador",
                                      "password": "81662527"
                                  })

        TestUserAPI.token = request.data["token"]
        assert TestUserAPI.token

    @pytest.mark.django_db
    def test_add_user(self):
        token = Token.objects.get_or_create(user=self.user)
        resp = self.client.post(
            "/api/v1.0/users/create_user/",
            json.dumps({
                "email": "admin1@gmail.com",
                "username": "admin1",
                "password": "81662527"
            }),
            content_type="application/json",
            HTTP_AUTHORIZATION='Token {}'.format(token[0].__str__())
        )

        assert resp.status_code == 201
        assert resp.data['user']['username'] == "admin1"

        movies = User.objects.all()
        assert len(movies) > 0