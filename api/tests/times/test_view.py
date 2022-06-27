import json

import pytest
from rest_framework.test import APITestCase
from api.models import User, Project, Time
from rest_framework.authtoken.models import Token


@pytest.mark.django_db
class TestTimeAPI(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='Administrador', password='81662527', email="administrador@gmail.com")
        self.project = Project.objects.create(title="Cardápio digital", description="Projeto voltado a criação de cardápios digitais")

        self.time = Time.objects.bulk_create(
            [
                Time(pk=1, started_at="2022-06-24T12:30:59.000000", ended_at="2022-06-24T21:30:59.000000", user=self.user, project=self.project),
                Time(pk=2, started_at="2022-06-24T12:30:59.000000", ended_at="2022-06-24T21:30:59.000000", user=self.user, project=self.project),
                Time(pk=3, started_at="2022-06-24T12:30:59.000000", ended_at="2022-06-24T21:30:59.000000", user=self.user, project=self.project)
            ]
        )

    @pytest.mark.django_db
    def test_add_time(self):
        token = Token.objects.get_or_create(user=self.user)
        resp = self.client.post(
            "/api/v1.0/times/",
            json.dumps({
                "started_at": "2022-06-24T12:30:59.000000",
                "ended_at": "2022-06-24T21:30:59.000000",
                "user": self.user.id,
                "project": self.project.id
            }),
            content_type="application/json",
            HTTP_AUTHORIZATION='Token {}'.format(token[0].__str__())
        )

        assert resp.status_code == 201

    @pytest.mark.django_db
    def test_list_all_times(self):
        token = Token.objects.get_or_create(user=self.user)
        resp = self.client.get(
            "/api/v1.0/times/",
            HTTP_AUTHORIZATION='Token {}'.format(token[0].__str__())
        )

        assert resp.status_code == 200
        assert resp.data[0]['id'] == 1
        assert resp.data[1]['id'] == 2
        assert resp.data[2]['id'] == 3

    @pytest.mark.django_db
    def test_get_time(self):
        token = Token.objects.get_or_create(user=self.user)
        resp = self.client.get(
            "/api/v1.0/times/1/",
            HTTP_AUTHORIZATION='Token {}'.format(token[0].__str__())
        )

        assert resp.status_code == 200

    @pytest.mark.django_db
    def test_update_time(self):
        token = Token.objects.get_or_create(user=self.user)
        resp = self.client.put(
            "/api/v1.0/times/1/",
            json.dumps({
                "started_at": "2022-06-23T12:30:59.000000",
                "ended_at": "2022-06-24T21:30:59.000000",
                "user": self.user.id,
                "project": self.project.id
            }),
            content_type="application/json",
            HTTP_AUTHORIZATION='Token {}'.format(token[0].__str__())
        )

        assert resp.status_code == 200

    @pytest.mark.django_db
    def test_get_time_by_project(self):
        token = Token.objects.get_or_create(user=self.user)
        resp = self.client.get(
            "/api/v1.0/times/get_time_by_project/",
            {'id_project': 1},
            content_type="application/json",
            HTTP_AUTHORIZATION='Token {}'.format(token[0].__str__())
        )

        assert resp.status_code == 200
        assert len(resp.data) > 0
