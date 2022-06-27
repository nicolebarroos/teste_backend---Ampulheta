import json

import pytest
from rest_framework.test import APITestCase
from api.models import User, Project
from rest_framework.authtoken.models import Token


@pytest.mark.django_db
class TestProjectAPI(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='Administrador', password='81662527', email="administrador@gmail.com")
        self.project = Project.objects.bulk_create(
            [
                Project(pk=1, title="Cardápio digital", description="Projeto voltado a criação de cardápios digitais"),
                Project(pk=2, title="App Delivery", description="Aplicativo de delivery próprio"),
                Project(pk=3, title="Ecommerce", description="Projeto voltado para vendas no varejo")
            ]
        )

    @pytest.mark.django_db
    def test_add_project(self):
        token = Token.objects.get_or_create(user=self.user)
        resp = self.client.post(
            "/api/v1.0/project/",
            json.dumps({
                "title": "Cardápio digital",
                "description": "Projeto voltado a criação de cardápios digitais",
            }),
            content_type="application/json",
            HTTP_AUTHORIZATION='Token {}'.format(token[0].__str__())
        )

        assert resp.status_code == 201
        assert resp.data['title'] == "Cardápio digital"

    @pytest.mark.django_db
    def test_list_all_projects(self):
        token = Token.objects.get_or_create(user=self.user)
        resp = self.client.get(
            "/api/v1.0/project/",
            HTTP_AUTHORIZATION='Token {}'.format(token[0].__str__())
        )

        assert resp.status_code == 200
        assert resp.data[0]["title"] == self.project[0].title
        assert resp.data[1]["title"] == self.project[1].title
        assert resp.data[2]["title"] == self.project[2].title

    @pytest.mark.django_db
    def test_get_project(self):
        token = Token.objects.get_or_create(user=self.user)
        resp = self.client.get(
            "/api/v1.0/project/1/",
            HTTP_AUTHORIZATION='Token {}'.format(token[0].__str__())
        )

        assert resp.status_code == 200
        assert resp.data["title"] == self.project[0].title

    @pytest.mark.django_db
    def test_update_project(self):
        token = Token.objects.get_or_create(user=self.user)
        resp = self.client.put(
            "/api/v1.0/project/1/",
            json.dumps({
                "title": "Cardápio digital - APP",
                "description": "Projeto voltado a criação de cardápios digitais para apps",
            }),
            content_type="application/json",
            HTTP_AUTHORIZATION='Token {}'.format(token[0].__str__())
        )

        assert resp.status_code == 200
        assert resp.data['title'] == "Cardápio digital - APP"