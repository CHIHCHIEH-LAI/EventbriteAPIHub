from fastapi import Response
from src.auth.eventbrite import config
import requests

class EventbriteAuth:
    def __init__(self):
        self.auth_url = config.AUTH_URL
        self.token_url = config.TOKEN_URL
        self.client_id = config.API_KEY
        self.client_secret = config.CLIENT_SECRET
        self.redirect_uri = config.REDIRECT_URI

    def construct_auth_url(self):
        return (
            f'{self.auth_url}'
            f'?response_type=code'
            f'&client_id={self.client_id}'
            f'&redirect_uri={self.redirect_uri}'
        )
    
    def redirect_to_auth(self):
        auth_url = self.construct_auth_url()
        headers = {'Location': auth_url}
        return Response(headers=headers, status_code=307)
    
    def exchange_code_for_token(self, access_code):
        data = {
            'grant_type': 'authorization_code',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': access_code,
            'redirect_uri': self.redirect_uri
        }
        response = requests.post(self.token_url, data=data)
        return response.json()

    def store_token(self, access_token):
        pass
        

    