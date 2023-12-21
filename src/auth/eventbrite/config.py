from dotenv import load_dotenv
import os

from src.config import BASE_URI

load_dotenv()

AUTH_URL = 'https://www.eventbrite.com/oauth/authorize'
TOKEN_URL = 'https://www.eventbrite.com/oauth/token'
API_KEY = os.getenv('EVENTBRITE_API_KEY')
CLIENT_SECRET = os.getenv('EVENTBRITE_CLIENT_SECRET')
REDIRECT_URI = BASE_URI + '/auth/eventbrite/redirect'