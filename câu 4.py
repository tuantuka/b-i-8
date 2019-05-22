from tkinter import *

wd = Tk()
wd.title("Wellcome to LikeGeeks app")
wd.geometry('350x200')
lbl = Label(wd, text = "Hello")
lbl.grid(column = 0, row = 0)

def clicked():
    lbl.configure(text = "Button was clicked!")
btn = Button(wd, text = "Click Me", command = clicked)
btn.grid(column = 1, row = 0)
wd.mainloop()