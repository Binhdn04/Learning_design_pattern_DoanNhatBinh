class Payment:
    def pay(self, amount):
        pass

class PayPal:
    def make_payment(self, money):
        print(f"Paypal: ${money}")

class PayPalAdapter(Payment):
    def __init__(self, paypal):
        self.paypal = paypal

    def pay(self, amount):
        self.paypal.make_payment(amount)
paypal = PayPal()
payment = PayPalAdapter(paypal)
payment.pay(100)