from app.repositories.machine_repository import MachineRepository
from sqlalchemy.orm import Session


class MachineService:

    def __init__(self, db: Session):
        self.repository = MachineRepository(db)


    def get_all(self):
        return self.repository.find_all()


    def get_by_id(self, machine_id):
        return self.repository.find_by_id(machine_id)

    def create(self, machine_data):
        machines = self.repository.find_all()

        new_machine = {

            "id": len(machines) + 1,

            "name": machine_data.name,

            "status": machine_data.status

        }

        return self.repository.save(new_machine)

