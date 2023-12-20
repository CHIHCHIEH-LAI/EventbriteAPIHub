from dotenv import load_dotenv
import os

from src.config import BASE_URI

load_dotenv()

EVENTBRITE_AUTH_CONFIG = {
    'AUTH_URL': 'https://www.eventbrite.com/oauth/authorize',
    'RESPONSE_TYPE': 'code',
    'API_KEY': os.getenv('EVENTBRITE_API_KEY'),
    'AUTH_REDIRECT_URI': BASE_URI + '/auth/redirect'
}