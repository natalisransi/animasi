# Assuming Python 2.x
# For Python 3.x support change print -> print(..) and Tkinter to tkinter
from tkinter import *
import time
import math


class animasi(object):

     lWidth = 500
     lHeight = 600

     posX = 70
     posY = 150
     
     def __init__(self):

        
        self.root = Tk()
        self.root.title("Pantulan Bola")
        self.canvas = Canvas(self.root, width=self.lWidth, height = self.lHeight)
        self.canvas.pack()
        #self.animasi1 = self.canvas.create_oval(2, 960, 42, 1000, outline='white',         fill='blue')
        self.animasi = self.canvas.create_oval(self.posX+0, self.posY+0, self.posX+70, self.posY+70, outline='black', fill='pink')
        self.canvas.pack()
        self.root.after(0, self.animation)
        self.root.mainloop()
        

     def animation(self):
        x = -10
        xhasil = 0.1
        y = 0
        coba = 0

        jalan = True
        while jalan:
            ylama = y
            y = (x)**2 - 5*x + 14
            
               
            yhasil = y - ylama
            x = x + xhasil
            
            time.sleep(0.010)
            self.canvas.move(self.animasi, xhasil, yhasil)
            self.canvas.update()

            if y == 0:
                print (str(xhasil)+" "+str(yhasil)+"hoax")
                
                coba = coba +1
                
            else:
                print ("Coba : "+str(coba)+" - y : "+str(y)+" - x : "+str(x))
                
            if coba == 2:
                jalan = False

            if y + 40 >= self.lHeight - self.posY:
                x = -15.4


animasi()
