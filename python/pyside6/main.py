import sys
import os
from PySide6.QtCore import QObject, Property, Signal, Slot, QUrl, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

# Создаем класс с данными для QML, наследуясь от QObject
class DataProvider(QObject):

    textChanged = Signal()
    def __init__(self):
        super().__init__()
        self._text = "Привет из Python!"


    # 2. Определяем свойствоб доступное для чтения и записи QML
    @Property(str, notify=textChanged)
    def text(self):
        return self._text
    
    print("1")
    
    @text.setter
    def text(self, value):
        if self._text == value:
            return
        # self._text = value
        self._text = self._text + "\n" + value
        self.textChanged.emit() # Уведомление QML об изменении

    @Slot(str)
    def receive_message(self, message):
        print(f"Сообщение из QML: {message}")
        self.text = f"Получено: {message}" # обновляем свойство
        


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # 3. Создаем экземпляр и регистрируем его в контексте QML
    provider = DataProvider()
    engine.rootContext().setContextProperty("dataProvider", provider)

    qml_file = os.path.join(os.path.dirname(__file__), "main.qml")
    engine.load(QUrl.fromLocalFile(qml_file))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())