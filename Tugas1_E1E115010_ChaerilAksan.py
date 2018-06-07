# Assuming Python 2.x
# For Python 3.x support change print -> print(..) and Tkinter to tkinter
from Tkinter import *
import time
import math


class alien2(object):

     lWidth = 500
     lHeight = 600

     posX = 50
     posY = 150
     
     def __init__(self):

        
        self.root = Tk()
        self.canvas = Canvas(self.root, width=self.lWidth, height = self.lHeight)
        self.canvas.pack()
        self.alien2 = self.canvas.create_oval(self.posX+0, self.posY+0, self.posX+70, self.posY+70, outline='white', fill='orange')
        self.alien3 = self.canvas.create_oval(self.posX+0, self.posY+0, self.posX+40, self.posY+40, outline='white', fill='blue')
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
            y = x*x  - 10*x + 16
               
            yhasil = y - ylama
            x = x + xhasil
            
            time.sleep(0.025)
            self.canvas.move(self.alien2, xhasil, yhasil)
            self.canvas.move(self.alien3, yhasil, xhasil)
            self.canvas.update()

            if y == 0:
                print str(xhasil)+" "+str(yhasil)+"hoax"
                
                coba = coba +1
                
            else:
                print "Coba : "+str(coba)+" - y : "+str(y)+" - x : "+str(x)
                #print str(x)+" "+str(y)+"    "+str(x)+" "+str(y)
            if coba == 2:
                jalan = False

            if y + 40 >= self.lHeight - self.posY:
                x = -15.4


alien2()
