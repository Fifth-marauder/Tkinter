import tkinter as tk
from tkinter import ttk
window=tk.Tk()
window.title("Welcome")
ttk.Label(window,text="A label").grid(column=0,row=0)
#window.resizable(False,False)
window.mainloop()
