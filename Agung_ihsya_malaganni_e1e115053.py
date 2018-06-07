# Assuming Python 2.x
# For Python 3.x support change print -> print(..) and Tkinter to tkinter
from Tkinter import *
import time
import math


class alien2(object):

     lWidth = 500
     lHeight = 600

     posX = 200
     posY = 150
     
     def __init__(self):

        
        self.root = Tk()
        self.canvas = Canvas(self.root, width=self.lWidth, height = self.lHeight)
        self.canvas.pack()
        self.alien2 = self.canvas.create_polygon(self.posX+5, self.posY+120, self.posX+5, self.posY+100, outline='black')
        self.canvas.pack()
        self.root.after(0, self.animation)
        self.root.mainloop()
        

     def animation(self):
        x = -15.4
        xmove = 0.7
        y = 0
        coba = 0

        run = True
        while run:
            ymove = y
            y = x*x  - 2*x + 10
            yy = y - ymove
            x = x + xmove
            
            time.sleep(0.010)
            self.canvas.move(self.alien2, xmove, yy)
            self.canvas.update()

            if y == 0:
                print str(xmove)+" "+str(yy)+""
                
                coba = coba +1
                
            else:
                print ""+str(coba)+" - y : "+str(y)+" - x : "+str(x)
            if coba == 2:
                run = False

            if y + 10 >= self.lHeight - self.posY:
                x = -10


alien2()
