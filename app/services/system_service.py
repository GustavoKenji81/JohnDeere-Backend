class SystemService:

    def get_api_status(self):

        return {
            "name": "John Deere Backend API",
            "version": "1.0.0",
            "status": "online"
        }

    def get_health(self):

        return {
            "status": "healthy"
        }