# Python logging
# import logging 
# logger = logging.getLogger("my_app")

class Button:
    def render(self):
        raise NotImplementedError

# Concrete products
class WindowsButton(Button):
    def render(self):
        print("Rendering a Windows-style button.")

class HTMLButton(Button):
    def render(self):
        print("Rendering an HTML-style button.")

# GUI framework (Creator classes)
class Dialog:
    def create_button(self):
        raise NotImplementedError

    def render(self):
        button = self.create_button()
        button.render()

class WindowsDialog(Dialog):
    def create_button(self):
        return WindowsButton()

class WebDialog(Dialog):
    def create_button(self):
        return HTMLButton()
        
dialog = WindowsDialog()
dialog.render()  