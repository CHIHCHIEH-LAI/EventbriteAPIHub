from fastapi import APIRouter
from .eventbrite_auth import EventbriteAuth

router = APIRouter()
    
@router.get("/auth/eventbrite")
def auth_eventbrite():
    eventbrite_auth = EventbriteAuth()
    return eventbrite_auth.redirect_to_auth()