import pytest
# from django.test import Client
from django.urls import reverse

from djangoaulas.django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Controle de aulas - Home</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">Django Aulas</a>')


def test_email_link(resp):
    assert_contains(resp, f"href='mailto:joao@joao.com.br'")
