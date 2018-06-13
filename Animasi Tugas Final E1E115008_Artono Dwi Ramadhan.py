from tkinter import *
import time
import math

lebar = 1200
tinggi = 700

class adr(object):

     lWidth = lebar
     lHeight = tinggi

     px = 50
     py = 200
     
     def __init__(self):

        self.root = Tk()
        self.root.title("Animasi Pantul Dua Bola")
        self.canvas = Canvas(self.root, width=self.lWidth, height = self.lHeight, bg='black')
        self.canvas.pack()
        self.bola1 = self.canvas.create_oval(self.px, self.py, self.px+50, self.py+50, outline='lightgreen', fill='lightblue')
        self.bola2 = self.canvas.create_oval(self.px, self.py, self.px+70, self.py+70, outline='lightgreen', fill='red')
        self.canvas.pack()
        self.root.after(0, self.animation)
        self.root.mainloop()
        
     def animation(self):
        x = 2
        xn = 0.5
        y = 0
        sx2 = 6
        sy2 = 8

        while True:
            yold = y
            y = x * 4 - 7**2 + 20
               
            yhasil = y - yold
            x = x + xn
            
            time.sleep(0.015)
            self.canvas.move(self.bola1, x, y)
            self.canvas.move(self.bola2, sx2, sy2)
            self.canvas.update()

            pos = self.canvas.coords(self.bola1)
            pos2 = self.canvas.coords(self.bola2)

            print ("y : "+str(y)+" - x : "+str(x))
                
            if pos[3] >= 700 or pos[1] <= 0:
                x = 2
                y = 0

            if pos2[3] >= tinggi or pos2[1] <= 0:
                sy2 = -sy2
            if pos2[2] >= lebar or pos2[0] <= 0:
                sx2 = -sx2

adr()
