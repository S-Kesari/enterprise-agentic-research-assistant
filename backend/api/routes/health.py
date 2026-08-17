from config.dependencies import get_settings
from config.settings import Settings
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/health")
def health_check(settings: Settings = Depends(get_settings)):
    return {
        "status": "ok",
        "environment": settings.environment
    }
