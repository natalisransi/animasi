from tkinter import *
import time
import math


class bola(object):

     Lebar = 500
     Tinggi = 600

     posX = 50
     posY = 150
     
     def __init__(self):

        
        self.root = Tk()
        self.canvas = Canvas(self.root, width=self.Lebar, height = self.Tinggi)
        self.canvas.pack()
        self.bola = self.canvas.create_oval(self.posX+0, self.posY+0, self.posX+40, self.posY+40, outline='white', fill='orange')
        self.canvas.pack()
        self.root.after(0, self.animation)
        self.root.mainloop()
        

     def animation(self):
        x = -15.4
        xhasil = 0.8
        y = 40
        coba=0
        
        jalan = True
        while jalan:
            
            ylama = y
            y = x*x  - 10*x + 16
               
            yhasil = y - ylama
            x = x + xhasil
            
            time.sleep(0.015)
            self.canvas.move(self.bola, xhasil, yhasil)
            self.canvas.update()

            if y + 40 >= self.Tinggi - self.posY:
                x = -15.4



bola()
