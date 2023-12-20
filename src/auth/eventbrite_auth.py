from fastapi import Response
from .config import EVENTBRITE_AUTH_CONFIG

class EventbriteAuth:
    def __init__(self):
        self.auth_url = EVENTBRITE_AUTH_CONFIG['AUTH_URL']
        self.response_type = EVENTBRITE_AUTH_CONFIG['RESPONSE_TYPE']
        self.client_id = EVENTBRITE_AUTH_CONFIG['API_KEY']
        self.redirect_uri = EVENTBRITE_AUTH_CONFIG['AUTH_REDIRECT_URI']

    def construct_auth_url(self):
        return (
            f"{self.auth_url}"
            f"?response_type={self.response_type}"
            f"&client_id={self.client_id}"
            f"&redirect_uri={self.redirect_uri}"
        )
    
    def redirect_to_auth(self):
        auth_url = self.construct_auth_url()
        headers = {"Location": auth_url}
        return Response(headers=headers, status_code=307)