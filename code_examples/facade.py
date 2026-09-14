# Order Pizza
class Kitchen:
    def prepare(self):
        print("Chuan bi pizza")

class Oven:
    def bake(self):
        print("Nuong pizza")

class Delivery:
    def deliver(self):
        print("Giao pizza")

# Facade
class PizzaShop:
    def order_pizza(self):
        Kitchen().prepare()
        Oven().bake()
        Delivery().deliver()
# Client
shop = PizzaShop()
shop.order_pizza()