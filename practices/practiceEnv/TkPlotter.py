import tkinter as tk
import tkinter.font as tkFont
import matplotlib.pyplot as pyplot
import numpy as np
from PIL import Image, ImageTk
import os

class Plotter(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        f = tkFont.Font(family='Helvetica', size=16, weight='bold')
        self.lebelX = tk.Label(self, text='X:', font=f, height=1, width=3)
        self.lebelY = tk.Label(self, text='Y:', font=f, height=1, width=3)
        self.txtX = tk.Text(self, font=f, height=1, width=40)
        self.txtY = tk.Text(self, font=f, height=1, width=40)
        self.btnLoad = tk.Button(self, text='plot!', font=f, height=1, width=5, command=self.load)
        self.cvsMain = tk.Canvas(self, width=800, height=600, bg='white')

        self.lebelX.grid(row=0, column=0, sticky=tk.E)
        self.lebelY.grid(row=1, column=0, sticky=tk.E)
        self.txtX.grid(row=0, column=1, sticky=tk.NE + tk.SW)
        self.txtY.grid(row=1, column=1, sticky=tk.NE + tk.SW)
        self.btnLoad.grid(row=0, rowspan=2, column=2, sticky=tk.NE + tk.SW)
        self.cvsMain.grid(row=2, column=0, columnspan=3, sticky=tk.NE + tk.SW)

    def makeScatter(self, x, y):
        fig = pyplot.figure()
        ax = fig.add_subplot(111)
        rangeX = max(x) - min(x)
        ax.set_xlim(min(x) - rangeX * 0.1, max(x) + rangeX * 0.1)
        rangeY = max(y) - min(y)
        ax.set_ylim(min(y) - rangeY * 0.1, max(y) + rangeY * 0.1)
        pyplot.plot(x, y, 'bo')
        for i,j in zip(x, y):
            ax.annotate(str(i) + "," + str(j), xy=(i, j), xytext=(5, 5), textcoords='offset points')

        pyplot.savefig("temp.png")

    def load(self):
        x = self.txtX.get("1.0", tk.END).split(",")
        for i in range(len(x)):
            x[i] = float(x[i])
        y = self.txtY.get("1.0", tk.END).split(",")
        for i in range(len(y)):
            y[i] = float(y[i])

        self.makeScatter(x, y)

        self.imageMain = ImageTk.PhotoImage(file="temp.png")
        self.cvsMain.create_image(400, 300, image=self.imageMain, anchor=tk.CENTER)
        os.system("del temp.png")

pl = Plotter()
pl.master.title('TkPlotter')
pl.mainloop()
