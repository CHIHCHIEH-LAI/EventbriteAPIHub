import pytest

from fastapi.testclient import TestClient
from src.main import app
from src.eventbrite_auth.router import EventbriteAuth

client = TestClient(app)

def test_construct_auth_url():
    auth = EventbriteAuth()
    expected_url = (
            f"https://www.eventbrite.com/oauth/authorize"
            f"?response_type=code"
            f"&client_id={auth.api_key}"
            "&redirect_uri=http://localhost:8000/oauth/redirect"
    )
    assert auth.construct_auth_url() == expected_url

def test_redirect_to_auth():
    auth = EventbriteAuth()
    response = auth.redirect_to_auth()
    assert response.status_code == 307
    assert response.headers['Location'].startswith("https://www.eventbrite.com/oauth/authorize")

# def test_auth_eventbrite_endpoint():
#     response = client.get("/auth/eventbrite")
#     assert response.status_code == 307
#     assert response.headers['Location'].startswith("https://www.eventbrite.com/oauth/authorize")
