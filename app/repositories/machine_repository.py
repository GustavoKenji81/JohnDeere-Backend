class MachineRepository:

    def __init__(self):

        self.machines = [

            {
                "id": 1,
                "name": "Trator 001",
                "status": "Running"
            },

            {
                "id": 2,
                "name": "Colheitadeira 001",
                "status": "Stopped"
            }

        ]


    def find_all(self):

        return self.machines


    def find_by_id(self, machine_id):

        for machine in self.machines:

            if machine["id"] == machine_id:

                return machine

        return None
    
    def save(self, machine):

        self.machines.append(machine)

        return machine