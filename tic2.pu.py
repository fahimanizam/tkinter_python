import tkinter.messagebox
from tkinter import *

root = Tk()
root.geometry("1350x750+0+0")
root.title("Tic Tac Toe")
root.configure(background = 'Cadet Blue')

Tops = Frame(root, bg = 'Cadet Blue', pady = 2, width = 1350, height = 100, relief = RIDGE)
Tops.grid(row = 0, column = 0)

lblTitle = Label(Tops, font = ('arial', 50, 'blod'), text = "Advanced Tic Tac Tow Game", bd = 21, bg = 'Cadet Blue', fg = 'Cornsilk', justify = CENTER)
lblTitle.grid(row = 0, column = 0)

MainFrame = Frame(root, bg = 'Powder Blue', bd = 10, width = 1350, height = 600, relief = RIDGE)
MainFrame.grid(row = 1, column = 0)

LeftFrame = Frame(MainFrame, bd = 10, width = 750, height = 500, pady = 2, padx = 10, bg = "Cadet Blue", relief = RIDGE)
LeftFrame.grid(side = LEFT)

RightFrame = Frame
RightFrame


root.mainloop()
