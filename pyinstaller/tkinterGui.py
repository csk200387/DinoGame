from tkinter import *
import os

# compile command
# pyinstaller -w -F --icon=ico.ico --add-data="ico.ico;." echo.py
root = Tk()
path = os.path.join(os.path.dirname(__file__), 'ico.ico')
if os.path.isfile(path):
    root.iconbitmap(path)

#root.iconbitmap('ico.ico')
root.geometry("400x200")
root.title("hello")
myLabel = Label(root, text="hello world")
myLabel.pack()

mainloop()
