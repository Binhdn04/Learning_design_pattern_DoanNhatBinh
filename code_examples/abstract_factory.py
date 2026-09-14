class UIFactory:
    def create_button(self):
        raise NotImplementedError

    def create_checkbox(self):
        raise NotImplementedError

class WindowsFactory(UIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

class MacFactory(UIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

class WindowsButton:
    print("Windows Button")

class WindowsCheckbox:
    print("Windows Checkbox")
class MacButton:
    pass

class MacCheckbox:
    pass 

factory = WindowsFactory()
button = factory.create_button()
checkbox = factory.create_checkbox()