# from itertools import chain
import tkinter as tk
from tkinter import ttk
from tkinter import font
#538ADB - синый
#68BC7F - зеленый
# common_color="#A7E0A6"

opt_list=["option 1", "option 2"]
for x in range(3, 10, 1):
    opt_list.append(f"option {x}")

def openSubMenu():
    v1 = var_list.get()
    print(f"this is a openSubMenu: {v1}")
    entry1_perem = entry1.get()
    entry1_perem = len(entry1_perem)
    entry1.delete(0, entry1_perem)
    entry1.insert(0, v1)
#538ADB
main_color="#D2DFDB"
window = tk.Tk()
window.configure(background=main_color, highlightbackground=main_color)
# window = tk.Frame(tk.Frame)
window.title("Утилиты для инженеров")
window.geometry("600x550")
selected_el=tk.PhotoImage(file="./select.png")
unselected_el=tk.PhotoImage(file="./unselect.png")
def sel():
    v1 = var_list.get()

tk_frame_label_1 = tk.Label(text="", background='gray', anchor="sw", highlightbackground=main_color)
tk_frame_label_1.pack(side=tk.LEFT)

tk_frame_label_1.place(width=150)
tk_frame_label_1.grid(row=0,column=0)
tk_frame_label_2 = tk.Label(text="")
tk_frame_label_2.grid(row=3,column=0)
tk_frame_label_1_1 = tk.Label(tk_frame_label_1, text="", background='blue', highlightbackground=main_color)
tk_frame_label_1_1.pack(side=tk.LEFT, anchor="w")
#anchor="sw",
tk_frame_label_1_1.pack(padx = 50, pady = 5)
tk_frame_label_1_1.pack(side=tk.LEFT, anchor='w')
# tk_frame_label_1_1.place(height=100, width=50)
# padx = 20, pady = 20
# tk.LEFT
var_list = tk.StringVar(tk_frame_label_1)
font_size=font.Font(family="System", size=20)
# tk_frame_label_3 = tk.Label(window, text="Fill Shape: (side=tk.LEFT, padx = 10)
# tk_frame_label_1 = tk.Label(window, text="Fill Shape: ", anchor="w")
# tk_frame_label_1.pack(side=tk.LEFT, padx = 10)
# tk_frame_label_2 = tk.Label(window, text="Fill Shape: ")
# tk_frame_label_2.grid(row=3,column=0)
button1 = tk.Button(tk_frame_label_2,text="press ok",command=openSubMenu, width=10, background=main_color, highlightbackground=main_color, bd=0, font = font_size, foreground = "#3D554E", activebackground='black', activeforeground='red')
# button1.bind("<Enter>", lambda e: button1.config(fg  = "yellow", bg = "black"))
# button1.bind("<Leave>", lambda e: button1.config(fg  = "white", bg = main_color))
button1.grid(row=0,column=0)
# button2 = tk.Button(tk_frame_label_2,text="press ok",command=openSubMenu, width", anchor="w")
# tk_frame_label_3.pack=10)
# button2.grid(row=1,column=0)
entry1=tk.Entry(tk_frame_label_2, background=main_color, highlightbackground=main_color, font = font_size)
entry1.config(font=("System", 20, "bold"))
entry1.place(width=150)
# entry1.place(x=10, y=20, width=50, height=50)
entry1.grid(row=1,column=0)
# entry2=tk.Entry(window)
# entry2.grid(row=1,column=1)
var = tk.StringVar()
var.set(opt_list[0])
# num_var=0
for elm in opt_list:
    # num_var += 1
    rbut = tk.Radiobutton(tk_frame_label_1_1, text=elm, variable=var_list, value=elm, background=main_color, highlightbackground=main_color, bd=0, font = font_size, foreground = "#3D554E", activebackground='black', activeforeground='red', image=unselected_el, selectimage=selected_el, compound="left", indicator=0)
    rbut.place(x=0, y=0, width=150, height=150)
    # rbut.pack(side='left')
    #command=sel, variable="var{num_var}" onvalue=elm,
    rbut.pack(anchor="w", padx = 150, pady = 5)
    # anchor="w"

    # print("You are selected print " + str(var.get) )
# def get_select_opt():

#
# button1 = tk.Button(window,text="press ok",command=openSubMenu, width=10)
# button1.grid(row=0,column=0)

# window.grid(row=0, column=0, stick="0")
# window.grid_columnconfigure(0, weight=1)
window.mainloop()


#
# if __name__ == "__main__":
#     main()