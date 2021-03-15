import pytest
from fastapi.testclient import TestClient
from web_Tag import app


@pytest.fixture
def base_client():
    return TestClient(app)


def test_home(base_client):
    response = base_client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Welcome to Sonic Tag!'}


def test_create(base_client):
    response = base_client.get('/game/create')
    assert response.status_code == 201
    assert response.json['success'] is True
    assert len(response.json['game_id']) == 36
    assert len(response.json['termination_password']) == 36


if __name__ == '__main__':
    pytest.main()