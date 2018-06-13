from tkinter import *
import time
import math

class bola(object):
     lebar = 1000
     tinggi = 600

     posX = 100
     posY = 200

     def __init__(self):
        self.root = Tk()
        self.root.title("Bola Bergerak")
        self.canvas = Canvas(self.root, width=self.lebar, height = self.tinggi)
        self.canvas.pack()
        self.ball1 = self.canvas.create_oval(self.posX, self.posY, self.posX+60, self.posY+60, outline='white', fill='lightblue')
        self.canvas.pack()
        self.root.after(0, self.animation)
        self.root.mainloop()

     def animation(self):
        x = 18
        xx = 0.3
        y = 50
        
        while True:
            yy = y
            y = x**3 + 10
            yhsl = y - yy
            x = x + xx

            time.sleep(0.025)
            self.canvas.move(self.ball1, xx, yhsl)
            self.canvas.update()

            if y == 0:
                print (" " + str(xx)+" "+str(yhsl))
               
            else:
                print ("- y : "+str(y)+" - x : "+str(x))
                
            if y >= 600:
                x = -18

bola()
