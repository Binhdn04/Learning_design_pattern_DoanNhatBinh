# Module cấp cao không nên phụ thuộc vào module cấp thấp. Cả hai nên phụ thuộc vào abstraction (interface)
# Chi tiết nên phụ thuộc vào abstraction
from abc import ABC, abstractmethod

class MessageSender(ABC):
    @abstractmethod
    def send(self, message):
        pass
class EmailSender(MessageSender):
    def send(self, message):
        print("Send by Email:", message)

class SMSSender(MessageSender):
    def send(self, message):
        print("Send by SMS:", message)

class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender
    def notify(self, message):
        self.sender.send(message)

email = NotificationService(EmailSender())
email.notify("Hi")
sms = NotificationService(SMSSender())
sms.notify("Hello")