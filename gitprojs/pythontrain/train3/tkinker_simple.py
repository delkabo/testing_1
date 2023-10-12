from cgitb import text
from tkinter import *

root = Tk()
root.title("lesson Tkinker")
root.geometry("400x200+700+500")
root.resizable(width=False, height=False)

value = StringVar()
# value.get
def test ():
    get = value.get()
    l["text"] = get

l = Label(text="test text")
e = Entry(textvariable=value)
b = Button(command=test, text="ok")




# b.bind('<Button-1>', test)

# grid(), pack()

l.pack()
e.pack()
b.pack()

root.mainloop()