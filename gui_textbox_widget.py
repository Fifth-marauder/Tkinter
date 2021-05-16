import tkinter as tk
from tkinter import ttk
window=tk.Tk()
window.title("Welcome")
#Modified click button
def click_me():
    action.configure(text="Hello  "+name.get()) 

#Changing the label
ttk.Label(window,text="Enter a name: ").grid(column=0,row=0)

#Adding a Textbox Entry widget
name=tk.StringVar()
name_entered=ttk.Entry(window, width=12,textvariable=name)
name_entered.grid(column=0,row=1)


action=ttk.Button(window,text="Click me", command=click_me)
action.grid(column=1,row=1)
#action.configure(state='disabled') #Disable the button widget

#Place cursor into name entry
name_entered.focus()


#Start GUI
window.mainloop()
    
