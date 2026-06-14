import tkinter as tk
from tkinter import ttk
opt_list=["opt 1", "opt 2", "opt 3", "opt 4"]
def openSubMenu():
    print("this is a openSubMenu")
def sel():
    print("You are selected print " + str(var.get) )
window = tk.Tk()
# window = tk.Frame(tk.Frame)
window.title("Утилиты для инженеров")
window.geometry("300x550")
tk_frame_label_1 = tk.Label(window, text="Fill Shape: ", anchor="w")
tk_frame_label_1.grid(row=3,column=0)
tk_frame_label_2 = tk.Label(window, text="Fill Shape: ")
tk_frame_label_2.grid(row=4,column=0)

# tk_frame_label_1.pack(side=tk.LEFT, padx = 10)
# button1 = ttk.Button(window,text="press ok",command=openSubMenu, width=10)
# button1.grid(row=0,column=0)
# button2 = ttk.Button(window,text="press ok",command=openSubMenu, width=10)
# button2.grid(row=1,column=0)
# entry1=ttk.Entry(window)
# entry1.grid(row=0,column=1)
# entry2=ttk.Entry(window)
# entry2.grid(row=1,column=1)
var = tk.StringVar()
var.set(opt_list[0])
for elm in opt_list:
    rbut = tk.Radiobutton(tk_frame_label_2, text=elm, variable=var, value=elm, command=sel)
rbut.pack(anchor="w")
button1 = ttk.Button(window,text="press ok",command=openSubMenu, width=10)
button1.grid(row=0,column=0)
# window.grid(row=0, column=0, stick="0")
# window.grid_columnconfigure(0, weight=1)
window.mainloop()
#
# if __name__ == "__main__":
# main()