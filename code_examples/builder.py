class Computer:
    def __init__(self, cpu, ram, storage=None):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage

class ComputerBuilder:
    def __init__(self):
        self._cpu = None
        self._ram = None
        self._storage = None

    def cpu(self, cpu):
        self._cpu = cpu
        return self

    def ram(self, ram):
        self._ram = ram 
        return self

    def storage(self, storage):
        self._storage = storage
        return self

    def build(self):
        return Computer(
            self._cpu,
            self._ram, 
            self._storage
        )
computer = (
    ComputerBuilder()
    .cpu("Intel I7")
    .ram("32GB")
    .storage("512GB")
    .build()
)
print(f"CPU: {computer.cpu}, RAM: {computer.ram}, Storage: {computer.storage}")
