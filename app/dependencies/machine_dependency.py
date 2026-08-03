from collections.abc import Generator
from fastapi import Depends
from sqlalchemy.orm import Session
from app.dependencies.database_dependency import get_db
from app.services.machine_service import MachineService


def get_machine_service(db: Session = Depends(get_db)) -> MachineService:

    return MachineService(db)

def test_connection(self):

    return str(self.db.bind.url)