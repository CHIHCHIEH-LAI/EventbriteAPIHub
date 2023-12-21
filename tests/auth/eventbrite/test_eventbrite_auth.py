import pytest

from dotenv import load_dotenv
import os

from src.auth.eventbrite.eventbrite_auth import EventbriteAuth

load_dotenv()

def test_construct_auth_url():
    auth = EventbriteAuth()
    client_id = os.getenv('EVENTBRITE_API_KEY')
    expected_url = (
            f'https://www.eventbrite.com/oauth/authorize'
            f'?response_type=code'
            f'&client_id={client_id}'
            f'&redirect_uri=http://localhost:8000/auth/eventbrite/redirect'
    )
    assert auth.construct_auth_url() == expected_url

def test_redirect_to_auth():
    auth = EventbriteAuth()
    response = auth.redirect_to_auth()
    assert response.status_code == 307
    assert response.headers['Location'].startswith('https://www.eventbrite.com/oauth/authorize')