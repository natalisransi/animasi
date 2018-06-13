from tkinter import *
import time
import math

class alien2(object):

     lWidth = 600
     lHeight = 600

     posX = 50
     posY = 150

     def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=self.lWidth, height = self.lHeight)
        self.canvas.pack()
        self.alien1 = self.canvas.create_oval(self.posX+500, self.posY+0, self.posX+550, self.posY+50, outline='blue', fill='blue')
        self.alien2 = self.canvas.create_oval(self.posX+50, self.posY+0, self.posX+0, self.posY+50, outline='blue', fill='red')
        self.canvas.pack()
        self.root.after(0, self.animation)
        self.root.mainloop()

        



     def animation(self):
        x = -15.4
        x2 = 25
        xhasil = 0.1
        xhasil2 = -0.1
        y = 0
        y2 = 0
        
        jalan = True

        while jalan:
            ylama = y
            y = x*x  - 10*x + 16
            #y= 100*math.sin(x) + 20

            yhasil = y - ylama
            x = x + xhasil

            ylama2 = y2
            y2 = x2*x2  - 10*x2 + 16
            #y= 100*math.sin(x) + 20

            yhasil2 = y2 - ylama2
            x2 = x2 + xhasil2

            time.sleep(0.0009)
            self.canvas.move(self.alien2, xhasil, yhasil)
            self.canvas.move(self.alien1, xhasil2, yhasil2)
            self.canvas.update()

				
            if y + 40 >= self.lHeight - self.posY:
                x = -15.4

            if y > 400:
                x2 = 25

								
alien2()
