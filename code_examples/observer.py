class Channel:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, user):
        self.subscribers.append(user)

    def new_video(self, title):
        for user in self.subscribers:
            user.update(title)

class User: 
    def __init__(self, name):
        self.name = name
    def update(self, title):
        print(f"{self.name} nhan thong bao: {title}")

channel = Channel()
channel.subscribe(User("Binh"))
channel.new_video("Python Design Patterns")