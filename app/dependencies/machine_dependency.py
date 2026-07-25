from app.services.machine_service import MachineService


def get_machine_service() -> MachineService:
    return MachineService()