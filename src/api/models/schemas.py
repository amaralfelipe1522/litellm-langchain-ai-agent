from pydantic import BaseModel

class HealthCheck(BaseModel):
    status: str = "ok"

class UserQuestion(BaseModel):
    question: str
    session_id: str