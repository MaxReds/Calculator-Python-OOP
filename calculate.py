from tkinter import *
from tkinter import Misc
from typing import Any, Literal
import logging

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.iconbitmap('icon.ico')
        self.geometry('500x850')

        self.my_entry = Entry(self, width=25, font=("Helvetica", 24))
        self.my_entry.pack(pady=20)

        My_frame(self)

    def clear(self):
        self.my_entry.delete(0, END)

    def pos_neg(self):
       if self.my_entry.get():
           if self.my_entry.get().startswith("-"):
                number = int(self.my_entry.get())
                self.my_entry.delete(0, END)
                self.my_entry.insert(0, (-1) * number)

           elif "+" not in self.my_entry.get() and "-" not in self.my_entry.get() and "*" not in self.my_entry.get() and "/" not in self.my_entry.get():
                number = int(self.my_entry.get())
                self.my_entry.delete(0, END)
                self.my_entry.insert(0, (-1) * number)

    def num_press(self, num):
        self.my_entry.insert(END, num)

    def signage(self, sign):
        if self.my_entry.get():
            self.my_entry.insert(END, sign)

    def mather(self):
        if self.my_entry.get():
            equation = self.my_entry.get()
            self.my_entry.delete(0, END)
            self.my_entry.insert(END, eval(equation))


        
        
class My_frame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack()

        self.button_1 = Button(self, text="1", font=("Helvetica", 24), command = lambda: parent.num_press(1))
        self.button_2 = Button(self, text="2", font=("Helvetica", 24), command = lambda: parent.num_press(2))
        self.button_3 = Button(self, text="3", font=("Helvetica", 24), command = lambda: parent.num_press(3))

        self.button_4 = Button(self, text="4", font=("Helvetica", 24), command = lambda: parent.num_press(4))
        self.button_5 = Button(self, text="5", font=("Helvetica", 24), command = lambda: parent.num_press(5))
        self.button_6 = Button(self, text="6", font=("Helvetica", 24), command = lambda: parent.num_press(6))

        self.button_7 = Button(self, text="7", font=("Helvetica", 24), command = lambda: parent.num_press(7))
        self.button_8 = Button(self, text="8", font=("Helvetica", 24), command = lambda: parent.num_press(8))
        self.button_9 = Button(self, text="9", font=("Helvetica", 24), command = lambda: parent.num_press(9))

        self.button_0 = Button(self, text="0", font=("Helvetica", 24), command = lambda: parent.num_press(0))
        self.button_negative = Button(self, text="+/-", font=("Helvetica", 24), command=parent.pos_neg)
        self.button_equal = Button(self, text="=", font=("Helvetica", 24), command=parent.mather)

        self.button_plus = Button(self, text="+", font=("Helvetica", 24), command = lambda: parent.signage("+"))
        self.button_minus = Button(self, text="-", font=("Helvetica", 24), command = lambda: parent.signage("-"))
        self.button_multiply = Button(self, text="*", font=("Helvetica", 24), command = lambda: parent.signage("*"))

        self.button_divide = Button(self, text="/", font=("Helvetica", 24), command = lambda: parent.signage("/"))
        self.button_clear = Button(self, text="Clear", font=("Helvetica", 24), command=parent.clear)

        self.button_1.grid(row=0, column=0, ipadx=40, ipady=20, padx=(0, 10))
        self.button_2.grid(row=0, column=1, ipadx=40, ipady=20)
        self.button_3.grid(row=0, column=2, ipadx=40, ipady=20, padx=(10, 0))

        self.button_4.grid(row=1, column=0, ipadx=40, ipady=20, padx=(0, 10), pady=10)
        self.button_5.grid(row=1, column=1, ipadx=40, ipady=20)
        self.button_6.grid(row=1, column=2, ipadx=40, ipady=20, padx=(10, 0), pady=10)

        self.button_7.grid(row=2, column=0, ipadx=40, ipady=20, padx=(0, 10), pady=10)
        self.button_8.grid(row=2, column=1, ipadx=40, ipady=20)
        self.button_9.grid(row=2, column=2, ipadx=40, ipady=20, padx=(10, 0), pady=10)

        self.button_0.grid(row=3, column=0, ipadx=40, ipady=20, padx=(0, 10),pady=10)
        self.button_negative.grid(row=3, column=1, ipadx=30, ipady=20)
        self.button_equal.grid(row=3, column=2, ipadx=40, ipady=20, padx=(10, 0), pady=10)

        self.button_plus.grid(row=4, column=0, ipadx=40, ipady=20, padx=(0, 10), pady=10)
        self.button_minus.grid(row=4, column=1, ipadx=45, ipady=20)
        self.button_multiply.grid(row=4, column=2, ipadx=40, ipady=20, padx=(10, 0), pady=10)

        self.button_divide.grid(row=5, column=0, ipadx=46, ipady=20, padx=(0, 10), pady=10)
        self.button_clear.grid(row=5, column=1, columnspan=2, ipadx=85, ipady=20, padx=(10, 0), pady=10)

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w")
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")
    

app = App()
app.mainloop()

       
       

        
       
