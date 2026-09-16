class TV:
    def on(self):
        print("TV on")
    def off(self):
        print("TV off")

class TurnOnCommand:
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.on()

class TurnOffCommand:
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.off() 

class Remote:
    def press(self, command):
        command.execute()

tv = TV()
remote = Remote()
command = TurnOffCommand(tv)
remote.press(command)