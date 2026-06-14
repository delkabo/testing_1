#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, messagebox
import sys
import argparse
import time

class ZenityLikeDialog():
    def __init__(self):
        self.args = self.parse_arguments()
        self.result = None

    def parse_arguments(self):
        parser = argparse.ArgumentParser(description='Zenity-like dialog')

        # Основные параметры
        parser.add_argument('--title', default='Диалоговое окно', help='Заголовок окна')
        parser.add_argument('--text', default='', help='Текст сообщения')
        parser.add_argument('--width', type=int, default=400, help='Ширина окна')
        parser.add_argument('--height', type=int, default=200, help='Высота окна')

        # Типы диалогов
        parser.add_argument('--question', action='store_true', help='Диалог с вопросом')
        parser.add_argument('--info', action='store_true', help='Информационное сообщение')
        parser.add_argument('--warning', action='store_true', help='Предупреждение')
        parser.add_argument('--error', action='store_true', help='Ошибка')
        parser.add_argument('--entry', action='store_true', help='Поле ввода')
        parser.add_argument('--list', action='store_true', help='Список выбора')
        parser.add_argument('--file-selection', action='store_true', help='Выбор файла')
        parser.add_argument('--color-selection', action='store_true', help='Выбор цвета')

        # Параметры для конкретных типов
        parser.add_argument('--list-items', nargs='+', help='Элементы списка')
        parser.add_argument('--entry-text', default='', help='Текст по умолчанию для поля ввода')
        parser.add_argument('--ok-label', default='OK', help='Текст кнопки OK')
        parser.add_argument('--cancel-label', default='Отмена', help='Текст кнопки отмены')
        parser.add_argument('--no-cancel', action='store_true', help='Скрыть кнопку отмены')

        # Цвета кнопок
        parser.add_argument('--ok-color', default='#4CAF50', help='Цвет кнопки OK (HEX)') ##4CAF50
        parser.add_argument('--cancel-color', default='#f44336', help='Цвет кнопки отмены (HEX)')
        parser.add_argument('--yes-color', default='#4CAF50', help='Цвет кнопки Да (HEX)')
        parser.add_argument('--no-color', default='#f44336', help='Цвет кнопки Нет (HEX)')
        parser.add_argument('--button-text-color', default='white', help='Цвет текста кнопок')
        parser.add_argument('--button-font', default='Arial 10 bold', help='Шрифт кнопок')

        return parser.parse_args()

    def create_styled_button(self, parent, text, command, color, width=10):
        """Создает стилизованную кнопку с указанным цветом"""
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            bg=color,
            fg=self.args.button_text_color,
            font=self.args.button_font,
            width=width,
            relief=tk.RAISED,
            bd=2,
            cursor="hand2"
        )
        return btn

    def show_info(self):
        """Информационное сообщение"""
        root = self.create_window()
        self.create_icon_label(root, 'info')
        self.create_text_label(root, self.args.text)
        self.create_ok_button(root)
        root.mainloop()
        return "OK"

    def show_warning(self):
        """Предупреждение"""
        root = self.create_window()
        self.create_icon_label(root, 'warning')
        self.create_text_label(root, self.args.text)
        self.create_ok_button(root)
        root.mainloop()
        return "OK"

    def show_error(self):
        """Ошибка"""
        root = self.create_window()
        self.create_icon_label(root, 'error')
        self.create_text_label(root, self.args.text)
        self.create_ok_button(root)
        root.mainloop()
        return "OK"

    def show_question(self):
        """Диалог с вопросом"""
        root = self.create_window()
        self.create_icon_label(root, 'question')
        self.create_text_label(root, self.args.text)

        button_frame = ttk.Frame(root)
        button_frame.pack(pady=10)

        def on_yes():
            self.result = "YES"
            root.quit()

        def on_no():
            self.result = "NO"
            root.quit()

        # Стилизованные кнопки Да/Нет
        yes_btn = self.create_styled_button(button_frame, "Да", on_yes, self.args.yes_color)
        yes_btn.pack(side=tk.LEFT, padx=5)

        no_btn = self.create_styled_button(button_frame, "Нет", on_no, self.args.no_color)
        no_btn.pack(side=tk.LEFT, padx=5)

        root.mainloop()
        root.destroy()
        return self.result

    def show_entry(self):
        """Поле ввода"""
        root = self.create_window()
        self.create_text_label(root, self.args.text)

        entry_var = tk.StringVar(value=self.args.entry_text)
        entry = ttk.Entry(root, textvariable=entry_var, width=40)
        entry.pack(pady=10)
        entry.focus()

    def on_ok():
        self.result = entry_var.get()
        root.quit()

        button_frame = ttk.Frame(root)
        button_frame.pack(pady=10)

        # Стилизованные кнопки OK/Отмена
        ok_btn = self.create_styled_button(button_frame, self.args.ok_label, on_ok, self.args.ok_color)
        ok_btn.pack(side=tk.LEFT, padx=5)

        if not self.args.no_cancel:
            cancel_btn = self.create_styled_button(button_frame, self.args.cancel_label, root.quit, self.args.cancel_color)
            cancel_btn.pack(side=tk.LEFT, padx=5)

        # Обработка Enter и Escape
        root.bind('<Return>', lambda e: on_ok())
        root.bind('<Escape>', lambda e: root.quit())

        root.mainloop()
        root.destroy()
        return self.result if self.result else ""

    def show_list(self):
        """Список выбора"""
        if not self.args.list_items:
            print("Ошибка: не указаны элементы списка --list-items", file=sys.stderr)
            return ""

        root = self.create_window()
        self.create_text_label(root, self.args.text)

        # Создаем Listbox с прокруткой
        frame = ttk.Frame(root)
        frame.pack(pady=10, fill=tk.BOTH, expand=True)

        listbox = tk.Listbox(frame, height=min(10, len(self.args.list_items)))
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
        listbox.configure(yscrollcommand=scrollbar.set)

        for item in self.args.list_items:
            listbox.insert(tk.END, item)

        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def on_ok():
        selection = listbox.curselection()
        if selection:
            self.result = self.args.list_items[selection[0]]
        root.quit()

        button_frame = ttk.Frame(root)
        button_frame.pack(pady=10)

        # Стилизованные кнопки OK/Отмена
        ok_btn = self.create_styled_button(button_frame, self.args.ok_label, on_ok, self.args.ok_color)
        ok_btn.pack(side=tk.LEFT, padx=5)

        if not self.args.no_cancel:
            cancel_btn = self.create_styled_button(button_frame, self.args.cancel_label, root.quit, self.args.cancel_color)
            cancel_btn.pack(side=tk.LEFT, padx=5)

        # Двойной клик для выбора
        listbox.bind('<Double-Button-1>', lambda e: on_ok())

        root.mainloop()
        root.destroy()
        return self.result if self.result else ""

    def show_color_selection(self):
        """Выбор цвета"""
        root = self.create_window()
        self.create_text_label(root, self.args.text or "Выберите цвет:")

        # Палитра цветов
        colors = [
            '#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF',
            '#FFA500', '#800080', '#008000', '#800000', '#008080', '#000080',
            '#FFC0CB', '#A52A2A', '#D2691E', '#4B0082', '#2E8B57', '#DC143C'
        ]

        color_frame = ttk.Frame(root)
        color_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        selected_color = tk.StringVar(value='#D2691E')
    def on_color_select(color):
        selected_color.set(color)
        # Показываем предпросмотр
        preview_label.config(bg=color)

        # Создаем кнопки цветов
        row, col = 0, 0
        for color in colors:
            color_btn = tk.Button(
                color_frame,
                bg=color,
                width=4,
                height=2,
                relief=tk.RAISED,
                bd=2,
                command=lambda c=color: on_color_select(c)
            )
            color_btn.grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 5:  # 6 цветов в строке
                col = 0
                row += 1

        # Поле предпросмотра
        preview_frame = ttk.Frame(root)
        preview_frame.pack(pady=10)

        ttk.Label(preview_frame, text="Выбранный цвет:").pack(side=tk.LEFT)
        preview_label = tk.Label(preview_frame, width=10, height=2, relief=tk.SUNKEN, bd=1)
        preview_label.pack(side=tk.LEFT, padx=5)

    def on_ok():
        self.result = selected_color.get()
        root.quit()

        button_frame = ttk.Frame(root)
        button_frame.pack(pady=10)

        ok_btn = self.create_styled_button(button_frame, self.args.ok_label, on_ok, self.args.ok_color)
        ok_btn.pack(side=tk.LEFT, padx=5)

        if not self.args.no_cancel:
            cancel_btn = self.create_styled_button(button_frame, self.args.cancel_label, root.quit, self.args.cancel_color)
            cancel_btn.pack(side=tk.LEFT, padx=5)

        root.mainloop()
        root.destroy()
        return self.result if self.result else ""

    def create_window(self):
        """Создание основного окна"""
        root = tk.Tk()
        root.title(self.args.title)
        root.geometry(f"{self.args.width}x{self.args.height}")
        root.resizable(False, False)

        # Центрирование окна
        root.update_idletasks()
        x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
        y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
        root.geometry(f"+{x}+{y}")

        return root

    def create_icon_label(self, parent, icon_type):
        """Создание метки с иконкой"""
        icons = {
            'info': 'ℹ️',
            'warning': '⚠️',
            'error': '❌',
            'question': '❓'
        }
        label = ttk.Label(parent, text=icons.get(icon_type, ''), font=('Arial', 24))
        label.pack(pady=10)

    def create_text_label(self, parent, text):
        """Создание метки с текстом"""
        if text:
            # label = ttk.Label(parent, text=text, wraplength=self.args.width - 50)
            label = ttk.Label(parent, text=text, wraplength=self.args.width - 50)
            label.pack(pady=10)

    def create_ok_button(self, parent):
        """Создание кнопки OK"""
        def on_ok():
            self.result = "OK"
            parent.quit()

        ok_btn = self.create_styled_button(parent, self.args.ok_label, on_ok, self.args.ok_color)
        ok_btn.pack(pady=10)

    def run(self):
        """Запуск соответствующего диалога"""
        try:
            if self.args.question:
                return self.show_question()
            elif self.args.info:
                return self.show_info()
            elif self.args.warning:
                return self.show_warning()
            elif self.args.error:
                return self.show_error()
            elif self.args.entry:
                return self.show_entry()
            elif self.args.list:
                return self.show_list()
            elif self.args.color_selection:
                return self.show_color_selection()
            else:
                # По умолчанию информационное окно
                return self.show_info()
                # return self.show_color_selection()
        except Exception as e:
            print(f"Ошибка: {e}", file=sys.stderr)
            return "this is oshibka"

def main():
    # time.sleep(5)
    dialog = ZenityLikeDialog()
    result = dialog.run()

    # bt_create_window = dialog.create_window()
    # bt_show_color_selection = dialog.show_color_selection()
    # getinfo = dialog.show_info()

    # print(bt_create_window)
    # print(bt_show_color_selection)
    # if bt_create_window:
    #
    #     if getinfo:
    #         print(getinfo)
    if result:
        print(result)

if __name__ == "__main__":
    main()
# if name == "main":
#     main()







