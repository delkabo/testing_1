import QtQuick
import QtQuick.Controls
import QtQuick.Window

Window {
    visible: true
    width: 400
    height: 200
    title: "Связка PySide6 + QML"


    Component.onCompleted: {
        if (dataProvider === null) {
            console.log("ОШИБКА: dataProvider равен null!");
        } else {
            console.log("OK: dataProvider зарегистрирован, text =", dataProvider.text);
        } 
    }

    Column {
        anchors.centerIn: parent
        spacing: 10

        // Отображаем текст из python
        Text {
            id: myText
            text: dataProvider.text
            font.pointSize: 16
        }

        // Изменяем текст прямо из интерфейса
        TextField {
            id: inputField
            placeholderText: "Введите новы текст"
        }

        Button {
            text: "Обновить текст в Python"
            onClicked: dataProvider.text = inputField.text
        }

        Button {
            text: "Обновить текст в Python. Тоже самое"
            onClicked: dataProvider.text = inputField.text
        }

        Button {
            text: "Отправить сообщение в Python"
            onClicked: dataProvider.receive_message("Привет,  серверная логика")
        }
    }
}