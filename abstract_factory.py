from abc import ABC, abstractmethod

# Продукты
class Button(ABC):
    @abstractmethod
    def paint(self): pass

class Checkbox(ABC):
    @abstractmethod
    def paint(self): pass


# Конкретные продукты Windows
class WindowsButton(Button):
    def paint(self):
        print("Windows Button")

class WindowsCheckbox(Checkbox):
    def paint(self):
        print("Windows Checkbox")


# Конкретные продукты Mac
class MacButton(Button):
    def paint(self):
        print("Mac Button")

class MacCheckbox(Checkbox):
    def paint(self):
        print("Mac Checkbox")


# Абстрактная фабрика
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button: pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox: pass


# Конкретные фабрики
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


# Клиентский код
class Application:
    def __init__(self, factory: GUIFactory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def paint(self):
        self.button.paint()
        self.checkbox.paint()
        
#Использование

app = Application(WindowsFactory())
app.paint()

app = Application(MacFactory())
app.paint()
