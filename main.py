from fastapi import FastAPI
from src.api.routers.v1 import health, ask

app = FastAPI(
    title="AI Agent API",
    version="1.0.0",
)

app.include_router(health.router)
app.include_router(ask.router)