import tkinter as tk
import tkinter.messagebox as msgbox
import tkinter.simpledialog as dlg
import tkinter.filedialog as fdlg
import tkinter.colorchooser as cdlg
import tkinter.font as font
import tkinter.scrolledtext as sct
import tkinter.ttk as ttk
import math
from PIL import Image, ImageTk

class Calculator(tk.Frame):
    shouldClear = True
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        f1 = font.Font(size = 48, family = "Courier New")
        f2 = font.Font(size = 32, family = "Courier New")

        self.txtNum = tk.Text(self, height=1, width=7, font=f1)
        self.btnNum1 = tk.Button(self, text="1", command=self.clickNum1, height=1, width=2, font=f2)
        self.btnNum2 = tk.Button(self, text="2", command=self.clickNum2, height=1, width=2, font=f2)
        self.btnNum3 = tk.Button(self, text="3", command=self.clickNum3, height=1, width=2, font=f2)
        self.btnNum4 = tk.Button(self, text="4", command=self.clickNum4, height=1, width=2, font=f2)
        self.btnNum5 = tk.Button(self, text="5", command=self.clickNum5, height=1, width=2, font=f2)
        self.btnNum6 = tk.Button(self, text="6", command=self.clickNum6, height=1, width=2, font=f2)
        self.btnNum7 = tk.Button(self, text="7", command=self.clickNum7, height=1, width=2, font=f2)
        self.btnNum8 = tk.Button(self, text="8", command=self.clickNum8, height=1, width=2, font=f2)
        self.btnNum9 = tk.Button(self, text="9", command=self.clickNum9, height=1, width=2, font=f2)
        self.btnNum0 = tk.Button(self, text="0", command=self.clickNum0, height=1, width=4, font=f2)
        self.btnFnRoot = tk.Button(self, text="√", command=self.clickFnRoot, height=1, width=2, font=f2)
        self.txtNum.grid(row=0, column=0, columnspan=4, sticky=tk.W+tk.E)
        self.btnNum1.grid(row=1, column=0, columnspan=1, sticky=tk.W+tk.E)
        self.btnNum2.grid(row=1, column=1, columnspan=1, sticky=tk.W+tk.E)
        self.btnNum3.grid(row=1, column=2, columnspan=1, sticky=tk.W+tk.E)
        self.btnNum4.grid(row=2, column=0, columnspan=1, sticky=tk.W+tk.E)
        self.btnNum5.grid(row=2, column=1, columnspan=1, sticky=tk.W+tk.E)
        self.btnNum6.grid(row=2, column=2, columnspan=1, sticky=tk.W+tk.E)
        self.btnNum7.grid(row=3, column=0, columnspan=1, sticky=tk.W+tk.E)
        self.btnNum8.grid(row=3, column=1, columnspan=1, sticky=tk.W+tk.E)
        self.btnNum9.grid(row=3, column=2, columnspan=1, sticky=tk.W+tk.E)
        self.btnNum0.grid(row=4, column=0, columnspan=2, sticky=tk.W+tk.E)
        self.btnFnRoot.grid(row=4, column=2, columnspan=1, sticky=tk.W+tk.E)

    def setNum(self, num):
        if self.shouldClear:
            self.txtNum.delete(1.0, tk.END)
            # self.txtNum.insert(tk.END, num)
            self.txtNum.insert("1.0", num)
            self.shouldClear = False
        else:
            self.txtNum.insert(tk.END, num)

    def clickNum1(self):
        self.setNum("1")
    def clickNum2(self):
        self.setNum("2")
    def clickNum3(self):
        self.setNum("3")
    def clickNum4(self):
        self.setNum("4")
    def clickNum5(self):
        self.setNum("5")
    def clickNum6(self):
        self.setNum("6")
    def clickNum7(self):
        self.setNum("7")
    def clickNum8(self):
        self.setNum("8")
    def clickNum9(self):
        self.setNum("9")
    def clickNum0(self):
        self.setNum("0")
    def clickFnRoot(self):
        # self.lblNum.configure(text = str(float(self.lblNum.cget("text"))**0.5))
        curNum = float(self.txtNum.get(1.0, tk.END))
        self.txtNum.delete(1.0, tk.END)
        self.txtNum.insert(1.0, str(round(math.sqrt(curNum), 2)))
        self.shouldClear = True

cal = Calculator()
cal.master.title("Calculator")
cal.mainloop()