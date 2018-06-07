
# Assuming Python 2.x
# For Python 3.x support change print -> print(..) and Tkinter to tkinter

#library
from Tkinter import *
import time
import math


class alien(object):
     def __init__(self):

        apa = 0
        self.root = Tk()
        #membuat layar
        self.canvas = Canvas(self.root, width=500, height = 500)
        self.canvas.pack()
        #membuat bentuk bola
        self.alien1 = self.canvas.create_oval(0, 960, 40, 1000, outline='white', fill='blue')
        self.canvas.pack()
        self.root.after(0, self.animation)
        self.root.mainloop()
        

     def animation(self):
        #apa = 1000
        x = 2
        xhasil = 1
        y = 0
        coba = 0

        jalan = True
        while jalan:
            ylama = y
            y = x*x  - 100*x + 1600
            yhasil = y - ylama
            x = x + xhasil
            
            time.sleep(0.025)
            self.canvas.move(self.alien1, xhasil, yhasil)
            self.canvas.update()

            if y == 0:
                print str(xhasil)+" "+str(yhasil)+"hoax"
                coba = coba +1
                
            else:
                print str(x)+" "+str(y)+"    "+str(x)+" "+str(y)
            if coba == 2:
                jalan = False

alien()
