from fastapi import APIRouter
from app.services.system_service import SystemService
from app.database.engine import engine

router = APIRouter(tags=["System"])

system_service = SystemService()


@router.get("/")
def home():
    return system_service.get_api_status()


@router.get("/health")
def health():
    return system_service.get_health()

@router.get("/database")
def database_info():

    return system_service.get_database_info()

@router.get("/database/test")
def test_database():

    return system_service.test_database_connection()