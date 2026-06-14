import sys
from PySide6.QtCore import QObject, Signal, Property, Slot

class DataModel(QObject):
    # 1. Объявляем Сигнал, который можно испустить из Python
    dataChanged = Signal(str)

    def __init__(self):
        super().__init__()
        self._user_input = ""

    # 2. Создаем свойство, доступное для чтения/записи из QML
    @Property(str, notify=dataChanged)
    def userInput(self):
        return self._user_input

    @userInput.setter
    def userInput(self, value):
        if self._user_input != value:
            self._user_input = value
            # При изменении свойства испускаем сигнал (QML обновится)
            self.dataChanged.emit(value)

    # 3. Слот для обработки сложной логики
    @Slot()
    def processData(self):
        result = self._user_input.upper()  # Например, преобразуем в верхний регистр
        print(f"[Python] Обработка данных: {result}")
        self.dataChanged.emit(f"Обработано: {result}")
