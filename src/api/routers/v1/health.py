from fastapi import APIRouter, status
from src.api.models.schemas import HealthCheck

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)

@router.get(
    "",
    summary="Health check endpoint",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
async def health_check():
    return HealthCheck()