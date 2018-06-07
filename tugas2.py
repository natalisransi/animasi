
import time
import math
from Tkinter import *


class obj2(object):

     #ukuran layout animasi
     lWidth = 500
     lHeight = 600

     #posisi objek
     posX = 100
     posY = 150
     
     def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=self.lWidth, height = self.lHeight) #membuat layout
        self.canvas.pack()
        self.obj1 = self.canvas.create_oval(2, 960, 42, 1000, outline='white', fill='blue')
        self.obj2 = self.canvas.create_oval(self.posX+0, self.posY+0, self.posX+20, self.posY+20, outline='white', fill='black') #membuat objek
        self.canvas.pack()
        self.root.after(0, self.animation)
        self.root.mainloop()
        

     def animation(self):
        x = -15
        xhasil = 0.9 #kecepatan pindah objek
        y = 1
        coba = 0
        majuundur = True
        jalan = True #menjalankan animasi/objek
        pan = 0
        while jalan:
            ylama = y
            y = x*x  - 10*x + 25 #persamaan kuadrat
                           
            yhasil = y - ylama
            x = x + xhasil
            
            time.sleep(0.00001)
            self.canvas.move(self.obj2, xhasil, yhasil)
            self.canvas.move(self.obj1, xhasil, yhasil)
            self.canvas.update()
            
            print("-y "+str(y)+"-x "+str(x))

            if pan == 3:
                 maju = False
            elif pan == 0:
                 maju= True
            
            if maju:
                 xhasil = 0.3
                 if y + 40 >= self.lHeight - self.posY: #membuat luping untuk objek memantul
                     x = -15
                     pan +=1
            else:
                 xhasil = -0.3
                 if  x <= -15:
                      x=25
                      pan -=1
                      
            
                 


obj2()
