from fastapi import APIRouter, Response
import os

router = APIRouter()

class EventbriteAuth:
    def __init__(self):
        self.api_key = os.getenv("EVENTBRITE_API_KEY")
        self.redirect_uri = "http://localhost:8000/auth/redirect"

    def construct_auth_url(self):
        return (
            f"https://www.eventbrite.com/oauth/authorize"
            f"?response_type=code"
            f"&client_id={self.api_key}"
            f"&redirect_uri={self.redirect_uri}"
        )
    
    def redirect_to_auth(self):
        auth_url = self.construct_auth_url()
        headers = {"Location": auth_url}
        return Response(headers=headers, status_code=307)
    
@router.get("/auth/eventbrite")
def auth_eventbrite():
    eventbrite_auth = EventbriteAuth()
    return eventbrite_auth.redirect_to_auth()