import tkinter as tk
from tkinter import ttk

# Создаем основное окно
root = tk.Tk()
root.title("Приложение")
root.geometry("800x600")

# Левая колонка (File и Exit)
frame_left = tk.Frame(root, width=200, height=300, bg="lightgray")
frame_left.pack(side=tk.LEFT, fill=tk.Y)

file_label = tk.Label(frame_left, text="Файл", font=('Arial', 12))
file_label.pack(pady=(20, 0))

exit_button = tk.Button(frame_left, text="Выход", command=lambda: root.destroy())
exit_button.pack(pady=10)

# Центральная колонка (меню инструментов)
frame_middle = tk.Frame(root, width=400, height=600, bg="white")
frame_middle.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

menu_categories = ["Диагностика системы", "Работа с доменом", "Типовые ошибки"]

for category in menu_categories:
    button = tk.Button(frame_middle, text=category, padx=10, pady=5)
    button.pack(fill=tk.X, pady=5)

# Правая колонка (Новости и Справка)
frame_right = tk.Frame(root, width=200, height=600, bg="lightblue")
frame_right.pack(side=tk.RIGHT, fill=tk.Y)

news_button = tk.Button(frame_right, text="Новости", padx=10, pady=5)
news_button.pack(fill=tk.X, pady=10)

help_button = tk.Button(frame_right, text="Справка", padx=10, pady=5)
help_button.pack(fill=tk.X, pady=10)

# Подменю

# Запускаем приложение
root.mainloop()
