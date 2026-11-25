#!/usr/bin/env python3
import sys
import os
import glob
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTextEdit, 
    QPushButton, QHBoxLayout, QLabel
)
from PyQt5.QtGui import QFont


def run_cmd(cmd):
    """Безопасное выполнение системной команды."""
    try:
        out = subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL, text=True)
        return out.strip()
    except Exception:
        return ""


def get_battery_info():
    """Сбор информации о батарее и расчет оставшегося времени работы."""
    bats = glob.glob("/sys/class/power_supply/BAT*")
    if not bats:
        return "Батарея не обнаружена (стационарный ПК или отсутствует АКБ)."

    lines = []
    for bat in bats:
        name = os.path.basename(bat)
        try:
            with open(os.path.join(bat, "status"), "r") as f:
                status = f.read().strip()
            with open(os.path.join(bat, "capacity"), "r") as f:
                capacity = f.read().strip()
        except Exception:
            continue

        # Перевод статуса
        status_ru = {
            "Discharging": "Разряжается (работа от батареи)",
            "Charging": "Заряжается",
            "Full": "Заряжена полностью",
            "Not charging": "Не заряжается (от сети)"
        }.get(status, status)

        info_str = f"• {name}: {capacity}% — {status_ru}"

        # Расчет оставшегося времени при работе от батареи
        if status == "Discharging":
            try:
                # В разных ноутбуках ядро отдает либо energy (мкВт*ч), либо charge (мкА*ч)
                if os.path.exists(os.path.join(bat, "energy_now")):
                    now = int(open(os.path.join(bat, "energy_now")).read().strip())
                    rate = int(open(os.path.join(bat, "power_now")).read().strip())
                else:
                    now = int(open(os.path.join(bat, "charge_now")).read().strip())
                    rate = int(open(os.path.join(bat, "current_now")).read().strip())

                if rate > 0:
                    hours_left = now / rate
                    hrs = int(hours_left)
                    mins = int((hours_left - hrs) * 60)
                    info_str += f"\n  Осталось времени работы: ~{hrs} ч. {mins} мин."
            except Exception:
                pass

        lines.append(info_str)

    return "\n".join(lines) if lines else "Нет данных о батарее."


def get_brightness_info():
    """Получение текущей яркости подсветки экрана."""
    backlights = glob.glob("/sys/class/backlight/*")
    if not backlights:
        return "Управление яркостью недоступно (внешний монитор или нет драйвера)."

    lines = []
    for bl in backlights:
        name = os.path.basename(bl)
        try:
            cur = int(open(os.path.join(bl, "brightness")).read().strip())
            max_b = int(open(os.path.join(bl, "max_brightness")).read().strip())
            percent = round((cur / max_b) * 100)
            lines.append(f"• Контроллер {name}: {percent}% (значение {cur} из {max_b})")
        except Exception:
            continue

    return "\n".join(lines) if lines else "Не удалось прочитать уровень яркости."


def get_monitors_info():
    """Получение списка подключенных мониторов и их моделей из EDID."""
    lines = []
    # Читаем напрямую из DRM (Direct Rendering Manager) ядра Linux
    drm_cards = glob.glob("/sys/class/drm/card*-*")
    for card in drm_cards:
        status_file = os.path.join(card, "status")
        if os.path.exists(status_file):
            with open(status_file, "r") as f:
                if f.read().strip() != "connected":
                    continue

            port_name = os.path.basename(card).split("-", 1)[1]
            model = "Встроенная матрица / Модель не передана"

            # Парсим бинарный EDID для извлечения названия модели монитора
            edid_file = os.path.join(card, "edid")
            if os.path.exists(edid_file):
                try:
                    with open(edid_file, "rb") as ef:
                        edid = ef.read()
                    # В стандарте EDID дескриптор имени начинается с байтов 00 00 00 FC 00
                    idx = edid.find(b"\x00\x00\x00\xfc\x00")
                    if idx != -1:
                        raw_name = edid[idx + 5:idx + 18]
                        parsed = raw_name.split(b"\n")[0].decode("ascii", errors="ignore").strip()
                        if parsed:
                            model = parsed
                except Exception:
                    pass

            lines.append(f"• Порт {port_name}: {model}")

    # Дополнительно берем текущее разрешение через xrandr
    xrandr_out = run_cmd("xrandr --current | grep ' connected'")
    if xrandr_out:
        lines.append("\nАктивные режимы (xrandr):")
        for xline in xrandr_out.splitlines():
            lines.append(f"  {xline}")

    return "\n".join(lines) if lines else "Активные мониторы не найдены."


def get_ram_info():
    """Информация об оперативной памяти и Swap из /proc/meminfo."""
    mem = {}
    try:
        with open("/proc/meminfo", "r") as f:
            for line in f:
                parts = line.split(":")
                if len(parts) == 2:
                    val_kb = int(parts[1].strip().split()[0])
                    mem[parts[0].strip()] = val_kb / (1024 * 1024)  # перевод в ГБ

        total = mem.get("MemTotal", 0)
        avail = mem.get("MemAvailable", 0)
        used = total - avail
        swap_total = mem.get("SwapTotal", 0)
        swap_free = mem.get("SwapFree", 0)

        return (
            f"• ОЗУ Всего: {total:.2f} ГБ\n"
            f"• ОЗУ Использовано: {used:.2f} ГБ (Доступно: {avail:.2f} ГБ)\n"
            f"• Файл подкачки (Swap): {swap_total - swap_free:.2f} / {swap_total:.2f} ГБ"
        )
    except Exception as e:
        return f"Ошибка чтения памяти: {e}"


def get_disks_info():
    """Информация о смонтированных разделах диска."""
    # Исключаем виртуальные файловые системы
    df_out = run_cmd("df -h -x tmpfs -x devtmpfs -x squashfs -x overlay")
    return df_out if df_out else "Не удалось получить список разделов."


class SysInfoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.collect_all_data()

    def init_ui(self):
        self.setWindowTitle("Диагностика и информация о системе")
        self.resize(650, 580)

        layout = QVBoxLayout(self)

        title = QLabel(f"Отчет об оборудовании (Запущено от пользователя: {os.getenv('USER', 'root')})")
        title.setStyleSheet("font-weight: bold; font-size: 13px; margin-bottom: 5px;")
        layout.addWidget(title)

        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        self.text_area.setFont(QFont("Monospace", 10))
        layout.addWidget(self.text_area)

        btn_layout = QHBoxLayout()
        btn_refresh = QPushButton("Обновить данные")
        btn_refresh.clicked.connect(self.collect_all_data)
        
        btn_close = QPushButton("Закрыть")
        btn_close.clicked.connect(self.close)

        btn_layout.addWidget(btn_refresh)
        btn_layout.addWidget(btn_close)
        layout.addLayout(btn_layout)

    def collect_all_data(self):
        report = [
            "=== ЭКРАН И МОНИТОРЫ ===",
            get_monitors_info(),
            "\n=== ЯРКОСТЬ ЭКРАНА ===",
            get_brightness_info(),
            "\n=== ПИТАНИЕ И БАТАРЕЯ ===",
            get_battery_info(),
            "\n=== ОПЕРАТИВНАЯ ПАМЯТЬ (RAM) ===",
            get_ram_info(),
            "\n=== ДИСКОВЫЕ РАЗДЕЛЫ ===",
            get_disks_info()
        ]
        self.text_area.setPlainText("\n".join(report))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = SysInfoWindow()
    win.show()
    sys.exit(app.exec_())
