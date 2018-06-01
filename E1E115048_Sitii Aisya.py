# Assuming Python 2.x
# For Python 3.x support change print -> print(..) and Tkinter to tkinter
from Tkinter import *
import time
import math


class aljabarliner(object):

     lWidth = 500
     lHeight = 600

     posX = 30
     posY = 140
     
     def __init__(self):

        
        self.root = Tk()
        self.canvas = Canvas(self.root, width=self.lWidth, height = self.lHeight)
        self.canvas.pack()
        self.alien1 = self.canvas.create_oval(self.posX+0, self.posY+0, self.posX+40, self.posY+40, outline='white', fill='red')
        self.alien2 = self.canvas.create_oval(self.posX+0, self.posY+0, self.posX+40, self.posY+40, outline='white', fill='yellow')
        self.canvas.pack()
        self.root.after(0, self.animation)
        self.root.mainloop()
        

     def animation(self):
        x = -15.4
        xhasil = 0.1
        y = 0

        jalan = True
        while jalan:
             
            ylama = y
            y = x*x  - 10*x + 16
               
            yhasil = y - ylama
            x = x + xhasil
            
            time.sleep(0.001)
            self.canvas.move(self.alien2, yhasil, xhasil)
            self.canvas.move(self.alien1,xhasil , yhasil)
            self.canvas.update()


            if y + 40 >= self.lHeight - self.posY:
                x = -15.4


aljabarliner()
