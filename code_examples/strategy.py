class Car:
    def go(self):
        print("Di oto")

class Motorbike:
    def go(self):
        print("Di xe may")
class Bus: 
    def go(self):
        print("Di xe bus")
class Trip:
    def __init__(self, strategy):
        self.strategy = strategy

    def start(self):
        self.strategy.go()

trip = Trip(Motorbike())
trip.start()