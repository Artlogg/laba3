class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def some_method(self):
        print("Метод одиночки")

#Проверка
a = Singleton()
b = Singleton()

print(a is b) 
