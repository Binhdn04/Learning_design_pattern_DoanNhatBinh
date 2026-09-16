from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def processPayment(self, amount):
        pass

class CreditCardPaymentProcessor(PaymentProcessor):
    def processPayment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class MomoPaymentProcessor(PaymentProcessor):
    def processPayment(self, amount):
        print(f"Processing Momo of ${amount}")

credit_card_processor = CreditCardPaymentProcessor()
momo_processor = MomoPaymentProcessor()
credit_card_processor.processPayment(10)
momo_processor.processPayment(15)