import QtQuick
import QtQuick.Window
import QtQuick.Controls
import BackendModule 1.0 // Импортируем наш Python-модуль

Window {
    width: 400
    height: 300
    visible: true
    title: "QML + Python Integration"

    // Используем нашу модель. Объект DataModel доступен благодаря регистрации типа.
    DataModel {
        id: dataModel
        // Этот обработчик сработает, когда Python испустит сигнал dataChanged
        onDataChanged: (newData) => {
            console.log("[QML] Получен сигнал:", newData);
            statusLabel.text = newData;
        }
    }

    Column {
        anchors.centerIn: parent
        spacing: 15

        TextField {
            id: inputField
            placeholderText: "Введите текст здесь..."
            width: 300
            // ДВУСТОРОННЯЯ ПРИВЯЗКА: связываем свойство text поля ввода
            // со свойством userInput нашей Python-модели.
            text: dataModel.userInput
            onTextChanged: {
                dataModel.userInput = text
            }
        }

        Button {
            text: "Обработать на Python"
            width: 300
            // При нажатии вызываем слот processData() нашей Python-модели
            onClicked: {
                console.log("[QML] Вызов слота processData()...");
                dataModel.processData();
            }
        }

        Label {
            id: statusLabel
            width: 300
            wrapMode: Text.Wrap
            horizontalAlignment: Text.AlignHCenter
            text: "Жду ввода... (Попробуйте ввести текст и нажать кнопку)"
        }
    }
}
