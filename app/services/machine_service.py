from app.repositories.machine_repository import MachineRepository


class MachineService:

    def __init__(self):

        self.repository = MachineRepository()


    def get_all(self):

        return self.repository.find_all()


    def get_by_id(self, machine_id):

        return self.repository.find_by_id(machine_id)