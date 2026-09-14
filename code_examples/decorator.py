# Them behavior cho object ma khong sua class goc bang cach boc trong object co behavior do.
class Coffee:
    def cost(self):
        return 30

class MilkDecorator: 
    def __init__(self, coffee):
        self.coffee = coffee
    def cost(self):
        return self.coffee.cost() + 5

class SugarDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 2
    
coffee = Coffee()
coffee = MilkDecorator(coffee)
coffee = SugarDecorator(coffee)

print(coffee.cost())