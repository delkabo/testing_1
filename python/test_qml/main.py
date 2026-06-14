import sys
import os
from pathlib import Path

# 1. Импортируем необходимое из PySide6
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QQmlContext
from PySide6.QtCore import QUrl

# 2. Импортируем нашу модель из отдельного файла
from backend import DataModel

if __name__ == "__main__":
    # 3. Создаем экземпляр приложения
    app = QGuiApplication(sys.argv)

    # 4. Создаем QML-движок
    engine = QQmlApplicationEngine()

    # 5. Регистрируем наш Python-класс как тип для QML.
    #    Это КЛЮЧЕВОЙ МОМЕНТ №1.
    #    Благодаря этой строке в QML сработает `import BackendModule 1.0`
    from PySide6.QtQml import qmlRegisterType
    qmlRegisterType(DataModel, "BackendModule", 1, 0, "DataModel")

    # 6. Альтернативный способ: можно также экспортировать готовый экземпляр объекта,
    #    если нужен синглтон (одна общая модель на все приложение).
    #    Это КЛЮЧЕВОЙ МОМЕНТ №2 (используйте либо п.5, либо п.6, но не оба сразу для одного класса).
    # model_instance = DataModel()
    # engine.rootContext().setContextProperty("dataModel", model_instance)
    # Тогда в QML нужно будет использовать не `DataModel { id: ... }`, а просто обращаться к `dataModel`.

    # 7. Загружаем основной QML-файл.
    #    Важно указать полный путь, используя `QUrl.fromLocalFile()`.
    qml_file = Path(__file__).parent / "main.qml"
    engine.load(QUrl.fromLocalFile(os.fspath(qml_file)))

    # 8. Проверяем, загрузился ли корневой QML-объект
    if not engine.rootObjects():
        print("Ошибка: Не удалось загрузить QML файл!", file=sys.stderr)
        sys.exit(-1)

    # 9. Запускаем главный цикл приложения
    print("[Python] Приложение запущено. Ожидание взаимодействия...")
    sys.exit(app.exec())
