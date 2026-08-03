from app.config.settings import settings
from app.database.engine import engine
from sqlalchemy import text

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

    def get_database_info(self):

        return {
            "database_url": str(engine.url),
            "driver": engine.driver
        }

    def test_database_connection(self):

        try:

            with engine.connect() as connection:

               connection.execute(text("SELECT 1"))

            return {

                "status": "connected"

            }

        except Exception as e:

            return {

                "status": "error",

                "message": str(e)

            }