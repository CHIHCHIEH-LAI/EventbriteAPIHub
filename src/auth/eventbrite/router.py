from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from .eventbrite_auth import EventbriteAuth

router = APIRouter()
eventbrite_auth = EventbriteAuth()
    
@router.get('/auth/eventbrite')
def auth_eventbrite():
    return eventbrite_auth.redirect_to_auth()

@router.get('/auth/eventbrite/redirect')
def auth_redirect(request: Request):
    access_code = request.query_params.get('code')
    token_response = eventbrite_auth.exchange_code_for_token(access_code)
    with open("token_debug.txt", "w") as file:
        file.write(str(access_code))
    
    