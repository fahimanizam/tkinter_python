import tkinter as tk
from math import *

convert_constant = 1
inverse_convert_constant = 1

btn_params = {
    'padx' : 16,
    'pady' : 1,
    'bd' : 4,
    'fg' : 'white',
    'bg' : '#566666',
    'font' : ('arial', 18),
    'width' : 2,
    'height' : 2,
    'relief' : 'flat',
    'activebackground' : '#666666'
}

def fsin(arg):
    return sin(arg * convert_constant)

def fooa(arg):
    return cos(arg * convert_constant)

def ftan(arg):
    return tan(arg * convert_constant)

def arcsin(arg):
    return inverse_convert_constant * (asin(arg))

def arccos(arg):
    return inverse_convert_constant * (acos(arg))

def arctan(arg):
    return inverse_convert_constant * (atan(arg))

class Calculator:
    def __init__(self, master):
        self.expression = ""
        self.recall = ""
        self.sum_up = ""
        self.text_input = tk.StringVar()
        self.master = master

        top_frame = tk.Frame(master, width = 650, height = 20, bd = 4, relief = 'flat', bg = '#666666')
        top_frame.pack(side = tk.TOP)

        bottom_frame = tk.Frame(master, width = 650, height = 470, bd = 4, relief = 'flat', bg = '#666666')
        bottom_frame.pack(side = tk.BOTTOM)

        my_item = tk.Label(top_frame, text = "Scientific Calculator", font = ('arial', 14), fg = 'black', width = 26, bg = '#516666')
        my_item.pack()

        txt_display = tk.Entry(top_frame, font = ('arial', 26), relief = 'flat', bg = '#455555', fg = 'pink', textvariable = self.text_input, width = 60, bd = 10, justify = 'right')
        txt_display.pack()

        # row 0

        self.btn_left_brack = tk.Button(bottom_frame, **btn_params, text = "(", command = lambda: self.btn_click('('))
        self.btn_left_brack.grid(row = 0, column = 0)

        self.btn_right_brack = tk.Button(bottom_frame, **btn_params, text = ")", command = lambda: self.btn_click(')'))
        self.btn_right_brack.grid(row = 0, column = 1)

        self.btn_exp = tk.Button(bottom_frame, **btn_params, text = "exp", command = lambda: self.btn_click('exp('))
        self.btn_exp.grid(row = 0, column = 2)

        self.btn_pi = tk.Button(bottom_frame, **btn_params, text = "n", command = lambda: self.btn_click('pi'))
        self.btn_pi.grid(row = 0, column = 3)

        self.btn_clear = tk.Button(bottom_frame, **btn_params, text = "C", command = self.btn_clear_all)
        self.btn_clear.grid(row = 0, column = 4)

        self.btn_del = tk.Button(bottom_frame, **btn_params, text = "del", command = self.btn_clear1)
        self.btn_del.grid(row = 0, column = 5)

        self.btn_change_sign = tk.Button(bottom_frame, **btn_params, text="+/-", command = self.change_signs)
        self.btn_change_sign.grid(row = 0, column = 6)

        self.btn_div = tk.Button(bottom_frame, **btn_params, text = "/", command = lambda: self.btn_click('/'))
        self.btn_div.grid(row = 0, column = 7)

        self.btn_sqrt = tk.Button(bottom_frame, **btn_params, text = "sqrt", command = lambda: self.btn_click('sqrt('))
        self.btn_sqrt.grid(row = 0, column = 8)

        # row 1
        self.btn_Deg = tk.Button(bottom_frame, **btn_params, activeforeground = 'orange', text = "Deg", command = self.convert_deg)
        self.btn_Deg.grid(row = 1, column = 0)

        self.btn_Rad = tk.Button(bottom_frame, **btn_params, foreground = 'orange', activeforeground = 'orange', text = "Rad", command = self.convert_rad)
        self.btn_Rad.grid(row = 1, column = 1)

        self.cube = tk.Button(bottom_frame, **btn_params, text = u"x\u00B3", command = lambda: self.btn_click('**3'))
        self.cube.grid(row = 1, column = 2)

        self.btn_abs = tk.Button(bottom_frame, **btn_params, text = "abs", command = lambda: self.btn_click('abs' + '('))
        self.btn_abs.grid(row = 1, column = 3)

        self.btn_7 = tk.Button(bottom_frame, **btn_params, text = "7", command = lambda: self.btn_click(7))
        self.btn_7.configure(activebackground="#6d4d4d", bg = '#4d4d4d')
        self.btn_7.grid(row = 1, column = 4)

        self.btn_8 = tk.Button(bottom_frame, **btn_params, text = "8", command = lambda: self.btn_click(8))
        self.btn_8.configure(activebackground = "#4d4d4d", bg = "#4d4d4d")
        self.btn_8.grid(row = 1, column = 5)

        self.btn_9 = tk.Button(bottom_frame, **btn_params, text = "9", command = lambda: self.btn_click(9))
        self.btn_9.configure(activebackground = "#4d4d4d", bg = "#4d4d4d")
        self.btn_9.grid(row = 1, column = 6)

        self.btn_multi = tk.Button(bottom_frame, **btn_params, text = "X", command = lambda: self.btn_click('*'))
        self.btn_multi.grid(row = 1, column = 7)

        self.btn_MC = tk.Button(bottom_frame, **btn_params, text = "MC", command = lambda: self.btn_click('mc'))
        self.btn_MC.grid(row = 1, column = 8)

        #row 3
        self.btn_Deg = tk.Button(bottom_frame, **btn_params, activeforeground = 'orange', text = "Deg", command = self.convert_deg)
        self.btn_Deg.grid(row = 3, column = 0)

        self.btn_Rad = tk.Button(bottom_frame, **btn_params, foreground = 'orange', activeforeground = 'orange', text = "Rad", command = self.convert_rad)
        self.btn_Rad.grid(row = 3, column = 1)

        self.cube = tk.Button(bottom_frame, **btn_params, text = u"x\u00B3", command = lambda: self.btn_click('**3'))
        self.cube.grid(row = 3, column = 2)

        self.btn_abs = tk.Button(bottom_frame, **btn_params, text = "abs", command = lambda: self.btn_click('abs' + '('))
        self.btn_abs.grid(row = 3, column = 3)

        self.btn_4 = tk.Button(bottom_frame, **btn_params, text = "4", command = lambda: self.btn_click(4))
        self.btn_4.configure(activebackground = "#4d4d4d", bg = "#4d4d4d")
        self.btn_4.grid(row = 3, column = 4)

        self.btn_5 = tk.Button(bottom_frame, **btn_params, text = "5", command = lambda: self.btn_click(5))
        self.btn_5.configure(activebackground = "#4d4d4d", bg = "#4d4d4d")
        self.btn_5.grid(row = 3, column = 5)

        self.btn_6 = tk.Button(bottom_frame, **btn_params, text = "6", command = lambda: self.btn_click(6))
        self.btn_6.configure(activebackground = "#4d4d4d", bg = "#4d4d4d")
        self.btn_6.grid(row = 3, column = 6)

        
        self.cube = tk.Button(bottom_frame, **btn_params, text = u"x\u00B3", command = lambda: self.btn_click('**3'))
        self.cube.grid(row = 3, column = 7)

        self.btn_abs = tk.Button(bottom_frame, **btn_params, text = "abs", command = lambda: self.btn_click('abs' + '('))
        self.btn_abs.grid(row = 3, column = 8)
        #row 4
        
        self.cube = tk.Button(bottom_frame, **btn_params, text = u"x\u00B3", command = lambda: self.btn_click('**3'))
        self.cube.grid(row = 4, column = 0)

        self.btn_abs = tk.Button(bottom_frame, **btn_params, text = "abs", command = lambda: self.btn_click('abs' + '('))
        self.btn_abs.grid(row = 4, column = 1)
        
        self.cube = tk.Button(bottom_frame, **btn_params, text = u"x\u00B3", command = lambda: self.btn_click('**3'))
        self.cube.grid(row = 4, column = 2)

        self.btn_abs = tk.Button(bottom_frame, **btn_params, text = "abs", command = lambda: self.btn_click('abs' + '('))
        self.btn_abs.grid(row = 4, column = 3)

        self.btn_1 = tk.Button(bottom_frame, **btn_params, text = "1", command = lambda: self.btn_click(1))
        self.btn_1.configure(activebackground = "#4d4d4d", bg = "#4d4d4d")
        self.btn_1.grid(row = 4, column = 4)

        self.btn_2 = tk.Button(bottom_frame, **btn_params, text = "2", command = lambda: self.btn_click(2))
        self.btn_2.configure(activebackground = "#4d4d4d", bg = "#4d4d4d")
        self.btn_2.grid(row = 4, column = 5)

        self.btn_3 = tk.Button(bottom_frame, **btn_params, text = "3", command = lambda: self.btn_click(3))
        self.btn_3.configure(activebackground = "#4d4d4d", bg = "#4d4d4d")
        self.btn_3.grid(row = 4, column = 6)
        
        self.cube = tk.Button(bottom_frame, **btn_params, text = u"x\u00B3", command = lambda: self.btn_click('**3'))
        self.cube.grid(row = 4, column = 7)

        self.btn_abs = tk.Button(bottom_frame, **btn_params, text = "abs", command = lambda: self.btn_click('abs' + '('))
        self.btn_abs.grid(row = 4, column = 8)

        #row 5
        
        self.cube = tk.Button(bottom_frame, **btn_params, text = u"x\u00B3", command = lambda: self.btn_click('**3'))
        self.cube.grid(row = 5, column = 0)

        self.btn_abs = tk.Button(bottom_frame, **btn_params, text = "abs", command = lambda: self.btn_click('abs' + '('))
        self.btn_abs.grid(row = 5, column = 1)
        
        self.cube = tk.Button(bottom_frame, **btn_params, text = u"x\u00B3", command = lambda: self.btn_click('**3'))
        self.cube.grid(row = 5, column = 2)

        self.btn_abs = tk.Button(bottom_frame, **btn_params, text = "abs", command = lambda: self.btn_click('abs' + '('))
        self.btn_abs.grid(row = 5, column = 3)

        self.btn_1 = tk.Button(bottom_frame, **btn_params, text = "", command = lambda: self.btn_click(1))
        self.btn_1.configure(activebackground = "#4d4d4d", bg = "#4d4d4d")
        self.btn_1.grid(row = 5, column = 4)

        self.btn_2 = tk.Button(bottom_frame, **btn_params, text = "0", command = lambda: self.btn_click(2))
        self.btn_2.configure(activebackground = "#4d4d4d", bg = "#4d4d4d")
        self.btn_2.grid(row = 5, column = 5)

        self.btn_3 = tk.Button(bottom_frame, **btn_params, text = "=", command = lambda: self.btn_click(3))
        self.btn_3.configure(activebackground = "#4d4d4d", bg = "#4d4d4d")
        self.btn_3.grid(row = 5, column = 6)
        
        self.cube = tk.Button(bottom_frame, **btn_params, text = u"x\u00B3", command = lambda: self.btn_click('**3'))
        self.cube.grid(row = 5, column = 7)

        self.btn_abs = tk.Button(bottom_frame, **btn_params, text = "abs", command = lambda: self.btn_click('abs' + '('))
        self.btn_abs.grid(row = 5, column = 8)
    #functions

    def btn_click(self, expression_val):
        if len(self.expression) >= 23:
            self.expression = self.expression
            self.text_input.set(self.expression)
        else:
            self.expression = self.expression + str(expression_val)
            self.text_input.set(self.expression)

    def btn_clear1(self):
        self.expression = self.expression[:-1]
        self.text_input.set(self.expression)

    def change_signs(self):
        self.expression = self.expression + '-'
        self.text_input.set(self.expression)

    def memory_clear(self):
        self.recall = ""

    def memory_add(self):
        self.recall = self.recall + '+' + self.expression

    def answer(self):
        self.answer = self.sum_up
        self.expression = self.expression + self.answer
        self.text_input.set(self.expression)

    def memory_recall(self):
        if self.expression == "":
            self.text_input.set('0' + self.expression + self.recall)
        else:
            self.text_input.set(self.expression + self.recall)

    def convert_deg(self):
        global convert_constant
        global inverse_convert_constant
        convert_constant = pi / 180
        inverse_convert_constant = 180 / pi
        self.btn_Rad["foreground"] = 'white'
        self.btn_Deg["foreground"] = 'orange'

    def convert_rad(self):
        global convert_constant
        global inverse_convert_constant
        convert_constant = 1
        inverse_convert_constant = 1
        self.btn_Rad["foreground"] = 'orange'
        self.btn_Deg["foreground"] = 'white'

    def btn_clear_all(self):
        self.expression = ""
        self.text_input.set("")

    def btn_equal(self):
        self.sum_up = str(eval(self.expression))
        self.text_input.set(self.sum_up)
        self.expression = self.sum_up


root = tk.Tk()
b = Calculator(root)
root.title("Scientific Calculator")
root.geometry("650x490+50+50")
root.resizable(False, False)
root.mainloop()