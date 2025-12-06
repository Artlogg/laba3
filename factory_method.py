from abc import ABC, abstractmethod

# Интерфейс продукта
class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

# Конкретные продукты
class FileLogger(Logger):
    def log(self, message: str):
        print(f"[FILE] {message}")

class ConsoleLogger(Logger):
    def log(self, message: str):
        print(f"[CONSOLE] {message}")

# Создатель
class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self) -> Logger:
        pass

    def log_message(self, message):
        logger = self.create_logger()
        logger.log(message)

# Конкретные создатели
class FileLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return FileLogger()

class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return ConsoleLogger()

#Использование

factory = ConsoleLoggerFactory()
factory.log_message("Hello!")

factory = FileLoggerFactory()
factory.log_message("Hello file!")
