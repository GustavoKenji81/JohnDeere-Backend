from pydantic import BaseModel


class MachineResponse(BaseModel):
    id: int
    name: str
    status: str

class MachineCreate(BaseModel):
    name: str
    status: str