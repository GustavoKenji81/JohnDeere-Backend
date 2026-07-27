from app.config.settings import settings

class SystemService:

    def get_api_status(self):

        return {
            "name": settings.app_name,
            "version": settings.app_version,
            "status": "online"
        }

    def get_health(self):

        return {
            "status": "healthy"
        }