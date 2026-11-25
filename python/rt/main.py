#!/usr/bin/env python3
import sys
import os
import json
import stat
import subprocess
import urllib.request
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QLabel, QMessageBox, QScrollArea
)
from PyQt5.QtCore import QThread, pyqtSignal, Qt

# Поддержка проверки прав из скрипта-обертки (sudo -n astra_menu.py --check)
if "--check" in sys.argv:
    sys.exit(0)

SERVER_MENU_URL = "http://your-server.local"
CACHE_DIR = "/var/cache/astra_launcher"
CACHE_MENU_FILE = os.path.join(CACHE_DIR, "menu.json")
CACHE_SCRIPTS_DIR = os.path.join(CACHE_DIR, "scripts")
TIMEOUT_SEC = 3


class MenuSyncWorker(QThread):
    """Фоновая загрузка меню с сервера с откатом на локальный кэш."""
    finished = pyqtSignal(dict, str)  # (данные_меню, текст_статуса)

    def run(self):
        os.makedirs(CACHE_SCRIPTS_DIR, mode=0o700, exist_ok=True)
        try:
            req = urllib.request.urlopen(SERVER_MENU_URL, timeout=TIMEOUT_SEC)
            raw_data = req.read().decode("utf-8")
            data = json.loads(raw_data)

            # Перезаписываем локальную копию меню свежей версией
            with open(CACHE_MENU_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

            self.finished.emit(data, "🟢 Меню загружено с сервера")
        except Exception:
            if os.path.exists(CACHE_MENU_FILE):
                with open(CACHE_MENU_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                self.finished.emit(data, "🟠 Сервер недоступен. Открыта локальная копия")
            else:
                self.finished.emit({"items": []}, "🔴 Нет связи с сервером и нет локальной копии")


class ScriptRunnerWorker(QThread):
    """Фоновая проверка/скачивание конкретного скрипта перед запуском."""
    ready_to_run = pyqtSignal(str, str, str)  # (путь_к_скрипту, тип, статус_источника)
    error = pyqtSignal(str)

    def __init__(self, item):
        super().__init__()
        self.item = item

    def run(self):
        try:
            script_type = self.item.get("type", "python")
            url = self.item.get("url")
            local_path = self.item.get("local_path")

            # Поддержка старого формата JSON, если использовался ключ "source"
            if not url and not local_path and "source" in self.item:
                src = self.item["source"]
                if src.startswith("http://") or src.startswith("https://"):
                    url = src
                else:
                    local_path = src

            # 1. Если пункт чисто локальный (без URL)
            if local_path and not url:
                if os.path.exists(local_path):
                    self.ready_to_run.emit(local_path, script_type, "Локальный системный скрипт")
                else:
                    self.error.emit(f"Локальный файл не найден:\n{local_path}")
                return

            # 2. Если нет ни URL, ни локального пути
            if not url:
                self.error.emit("В настройках пункта меню не указан ни 'url', ни 'local_path'.")
                return

            # 3. Логика для сетевого скрипта: скачать новый или взять кэш
            item_id = self.item.get("id", "script_temp")
            ext = ".sh" if script_type == "bash" else ".py"
            cached_script_path = os.path.join(CACHE_SCRIPTS_DIR, f"{item_id}{ext}")

            try:
                req = urllib.request.urlopen(url, timeout=TIMEOUT_SEC)
                script_content = req.read()

                with open(cached_script_path, "wb") as f:
                    f.write(script_content)

                os.chmod(cached_script_path, stat.S_IRWXU)
                self.ready_to_run.emit(cached_script_path, script_type, "Загружено с сервера")
            except Exception:
                if os.path.exists(cached_script_path):
                    self.ready_to_run.emit(cached_script_path, script_type, "Запуск из локального кэша")
                else:
                    self.error.emit("Сервер недоступен, а локальная копия скрипта еще не сохранена.")

        except Exception as e:
            # Перехватываем любую непредвиденную ошибку, чтобы PyQt не падал в core dump
            self.error.emit(f"Внутренняя ошибка обработки пункта:\n{e}")


class LauncherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.active_workers = []
        self.init_ui()
        self.refresh_menu()

    def init_ui(self):
        self.setWindowTitle("Сервисное меню АРМ")
        self.resize(420, 520)

        self.layout = QVBoxLayout(self)

        self.status_label = QLabel("Инициализация...")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("font-weight: bold; padding: 6px;")
        self.layout.addWidget(self.status_label)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        self.list_container = QWidget()
        self.list_layout = QVBoxLayout(self.list_container)
        self.list_layout.setAlignment(Qt.AlignTop)
        scroll.setWidget(self.list_container)
        self.layout.addWidget(scroll)

        self.btn_refresh = QPushButton("Обновить список с сервера")
        self.btn_refresh.clicked.connect(self.refresh_menu)
        self.layout.addWidget(self.btn_refresh)

    def refresh_menu(self):
        self.btn_refresh.setEnabled(False)
        self.status_label.setText("⏳ Проверка меню на сервере...")

        worker = MenuSyncWorker()
        worker.finished.connect(self.on_menu_loaded)
        self.active_workers.append(worker)
        worker.start()

    def on_menu_loaded(self, data, status_text):
        self.btn_refresh.setEnabled(True)
        self.status_label.setText(status_text)

        # Очистка старых кнопок
        for i in reversed(range(self.list_layout.count())):
            widget = self.list_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        items = data.get("items", [])
        if not items:
            empty_lbl = QLabel("Список доступных задач пуст.")
            empty_lbl.setAlignment(Qt.AlignCenter)
            self.list_layout.addWidget(empty_lbl)
            return

        for item in items:
            btn = QPushButton(item["title"])
            btn.setMinimumHeight(42)
            btn.clicked.connect(lambda checked, it=item, b=btn: self.on_item_clicked(it, b))
            self.list_layout.addWidget(btn)

    def on_item_clicked(self, item, button):
        button.setEnabled(False)
        original_text = item["title"]
        button.setText(f"⏳ Проверка: {original_text}...")

        worker = ScriptRunnerWorker(item)

        def cleanup():
            button.setEnabled(True)
            button.setText(original_text)

        worker.ready_to_run.connect(lambda path, stype, src: (cleanup(), self.launch_script(path, stype, src)))
        worker.error.connect(lambda err: (cleanup(), QMessageBox.critical(self, "Ошибка", err)))

        self.active_workers.append(worker)
        worker.start()

    def launch_script(self, script_path, script_type, source_info):
        self.status_label.setText(f"▶ Запуск ({source_info})")
        interpreter = "bash" if script_type == "bash" else "python3"
        try:
            # Приложение уже запущено от root с сохраненным DISPLAY,
            # поэтому дочернее GUI-окно откроется напрямую от имени root
            subprocess.Popen([interpreter, script_path])
        except Exception as e:
            QMessageBox.critical(self, "Ошибка запуска", f"Не удалось запустить процесс:\n{e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LauncherWindow()
    window.show()
    sys.exit(app.exec_())
