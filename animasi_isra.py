from tkinter import *
import time
import math


class animasi(object):

     lWidth = 500
     lHeight = 600

     posX = 50
     posY = 150
     
     def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=self.lWidth, height = self.lHeight)
        self.canvas.pack()
        #self.animasi1 = self.canvas.create_oval(2, 960, 42, 1000, outline='white',         fill='blue')
        self.animasi2 = self.canvas.create_oval(self.posX+0, self.posY+0, self.posX+40, self.posY+40, outline='black', fill='Blue')
        self.canvas.pack()
        self.root.after(0, self.animation)
        self.root.mainloop()
        

     def animation(self):
        apa = 1000
        x = -15.4
        xhasil = 0.1
        y = 0
        coba = 0

        jalan = True
        while jalan:
            ylama = y
            y = x*x  - 2*x - 8
            #y= 100*math.sin(x) + 20
               
            yhasil = y - ylama
            x = x + xhasil
            
            time.sleep(0.01)
            self.canvas.move(self.animasi2, xhasil, yhasil)
            self.canvas.update()

            if y == 0:
                #print str(xhasil)+" "+str(yhasil)+"hoax"
                
                coba = coba +1
                
            
            if coba == 2:
                jalan = False

            if y + 40 >= self.lHeight - self.posY:
                x = -15.4


animasi()
