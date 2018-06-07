
# Assuming Python 2.x
# For Python 3.x support change print -> print(..) and Tkinter to tkinter
from tkinter import *
import time
import math



class animasi(object):
            

     def __init__(self):
        apax=50
        apay=363


        self.root = Tk()

        self.canvas = Canvas(self.root, width=500, height = 600)
        self.canvas.pack()
        
        #self.bola = self.canvas.create_oval(2, 960, 42, 1000, outline='white',         fill='blue')
        
        self.bola = self.canvas.create_oval(apax+0, apay+0, apax+40, apay+40, outline='white', fill='red')
        self.canvas.pack()
        
        self.root.after(0, self.animation)
        self.root.mainloop()
        

     def animation(self):
        
        #kordinat posisi awal
        x = 20
        y = 0

        #kecepatan perpindahan
        xhasil = 0.1
        
        #menjalankan animasi
        jalan = True
        while jalan:
  
            ylama = y
            
           #fungsi Trigonometri
            y =  200 * math.sin(x)

            yhasil = y - ylama
            x = x + xhasil
            
            #delay looping
            time.sleep(0.025)
            
            self.canvas.move(self.bola, xhasil, yhasil)
            self.canvas.update()
            


animasi()
