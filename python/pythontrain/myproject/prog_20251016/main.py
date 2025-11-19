from pathlib import Path
import os
from tkinter import *
from tkinter.ttk import Combobox


p = Path(__file__).parents[2]
list = os.listdir(p)
# print(f"hello {list}")

# def clicked():
#     lbl.configure(text=f"hello {list}")

# pairs = [("name", "Anna"), ("age", 28), ("city", "berlin")]
# person = dict(pairs)

# def clicked():
#     lbl.configure(text=f"hello {pairs}")

# window = Tk()
# window.title("Добро пожаловать")
# window.geometry('700x200')
# lbl = Label(window, text=list, font=("Arial Bold", 15))
# lbl.grid(column=0, row=0)
# btn = Button(window, text="dont push", command=clicked)
# btn.grid(column=0, row=1)
# combo=Combobox(window)
# combo['values'] = (1,2,3,4,5,"Привет")
# combo.current(1)
# combo.grid(column=0, row=2)
# window.mainloop()

# print(person)


# answ = input("Хотите ли вы получить все данные: ")
# if answ == "да":
#     print(person)