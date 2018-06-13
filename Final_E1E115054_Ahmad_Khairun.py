# Assuming Python 2.x
# For Python 3.x support change print -> print(..) and Tkinter to tkinter
from Tkinter import *
import time
import math
from random import randint


class animasi(object):

     lWidth = 700
     lHeight = 600

     posX = 50
     posY = 150
     
     def __init__(self):

        
        self.root = Tk()

        #membuat layar
        self.canvas = Canvas(self.root, width=self.lWidth, height = self.lHeight)
        self.canvas.pack()
        
        #membuat objek
        self.bola1 = self.canvas.create_oval(self.posX+0, self.posY+0, self.posX+40, self.posY+40, outline='white', fill='red')
        self.bola2 = self.canvas.create_oval(self.posX+0, self.posY+0, self.posX+40, self.posY+40, outline='white', fill='blue')
        self.canvas.pack()

        #memanggil method animasi
        self.root.after(0, self.animation)
        self.root.mainloop()
        

     def animation(self):

        # kordinat posisi awal posisi awal
        awal = -15
        x = 5
        y = 0

        rand1 = 1
        rand2 = 10
        x2 = 3
        y2 = 7

        # jarak gerak bolah
        jauh = 1

        #manandakan bola maju
        maju = True

        # kecepatan perpindahan kordinat
        xhasil = 1

        # menjalankan animasi
        jalan = True
        while jalan:
             
            ylama = y
            
            #persamaan kuadrat
            y = x*x  - 10*x + 16
               
            yhasil = y - ylama
            
            x = x + xhasil
            
            time.sleep(0.01)
            self.canvas.move(self.bola1, jauh, yhasil)
            self.canvas.move(self.bola2, x2, y2)
            self.pos = self.canvas.coords(self.bola1)
            self.pos2 = self.canvas.coords(self.bola2)
            self.canvas.update()
            
            #print "- y : "+str(y)+" - x : "+str(x)+" - tinggi : "


            if self.pos2[3] > self.lHeight or self.pos2[1] < 0:
                 while self.pos2[3] + y2 > self.lHeight or self.pos2[1] + y2 < 0:
                      if y2 < 0:
                           print "++++++y"
                           y2 = randint(rand1, rand2)
                      else:
                           print "-----y"
                           y2= -randint(rand1, rand2)
                    
                 
            if self.pos2[2] > self.lWidth or self.pos2[0] < 0:
                 while self.pos2[2] + x2 > self.lWidth or self.pos2[0] + x2 < 0:
                      if x2 < 0:
                           x2 = randint(rand1, rand2)
                      else:
                           x2= -randint(rand1, rand2)
                      
            print "- y : "+str(y2)+" - x : "+str(x2)+" - tinggi : "
            
            # mengulang gerakan animasi ketika berada dibawah (memantul)
            if self.pos[3] >= self.lHeight:
                if maju:
                     x = awal
                else:
                     x = 25
                
            #print str("[0] : "+str(self.pos[0])+" - [1] : "+str(self.pos[1])+" - [2] : "+str(self.pos[2])+" - [3] : "+str(self.pos[3])  )

            if self.pos[2] >= self.lWidth:
                maju = False
                xhasil = -xhasil
                jauh = -jauh
            elif self.pos[0] <= 0:
                xhasil = -xhasil
                jauh = -jauh
                maju = True

     

#menjalankan class bola
animasi()


            
