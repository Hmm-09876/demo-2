import pytest
from flask import Flask

from app import create_app
@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the Flask Web App!' in response.data
