import tkinter as tk
from tkinter import ttk
window=tk.Tk()
window.title("Welcome")
#ttk.Label(window,text="A label").grid(column=0,row=0)
# window.resizable(False,False)
# Adding a label
a_label=ttk.Label(window,text="A label")
a_label.grid(column=0,row=0)

def click_me():
    action.configure(text="** I have been clicked!!! **")
    a_label.configure(foreground='red')
    a_label.configure(text='A red label')


action=ttk.Button(window,text="Click me",command=click_me)
action.grid(column=1,row=0)
window.mainloop()

