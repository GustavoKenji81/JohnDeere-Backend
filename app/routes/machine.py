from fastapi import APIRouter, HTTPException, Depends

from app.dependencies.machine_dependency import get_machine_service
from app.services.machine_service import MachineService
from app.schemas.machine_schema import MachineResponse

router = APIRouter(
    prefix="/machines",
    tags=["Machines"]
)

machine_service = MachineService()


@router.get("/", response_model=list[MachineResponse])
def get_all(machine_service: MachineService = Depends(get_machine_service)):

    return machine_service.get_all()


@router.get("/{machine_id}", response_model=MachineResponse)
def get_by_id(machine_id: int, machine_service: MachineService = Depends(get_machine_service)):

    machine = machine_service.get_by_id(machine_id)

    if machine is None:

        raise HTTPException(
            status_code=404,
            detail="Machine not found"
        )

    return machine