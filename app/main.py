from fastapi import FastAPI

from app.routes.system import router as system_router
from app.routes.machine import router as machine_router


app = FastAPI(
    title="John Deere Backend API",
    version="1.0.0"
)

app.include_router(system_router)
app.include_router(machine_router)