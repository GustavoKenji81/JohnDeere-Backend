from fastapi import APIRouter
from app.services.system_service import SystemService

router = APIRouter(tags=["System"])

system_service = SystemService()


@router.get("/")
def home():
    return system_service.get_api_status()


@router.get("/health")
def health():
    return system_service.get_health()