from fastapi import FastAPI
from src.auth.eventbrite.router import router as auth_router

app = FastAPI()
app.include_router(auth_router)