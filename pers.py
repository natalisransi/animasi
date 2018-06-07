
# Assuming Python 2.x
# For Python 3.x support change print -> print(..) and Tkinter to tkinter
from Tkinter import *
import time
import math


#membuat Objek
class alien(object):
     def __init__(self):

        tinggi = 100
        lebar = 10
        self.root = Tk()
        self.canvas = Canvas(self.root, width=600, height = 700)
        self.canvas.pack()
        self.alien2 = self.canvas.create_oval(lebar+0, tinggi+0, lebar+50, tinggi+20, outline='black', fill='yellow')
        self.canvas.pack()
        self.root.after(0, self.animation)
        self.root.mainloop()
        

     def animation(self):
        #posisi Awal
        x = -15
        y = 0
        #kecepatan gerak animasi
        xhasil = 0.5
        #menjalankan animasi
        awal = True
        jalan = True
        while jalan:
            ylama = y
            #persamaan y = 256 + x^2 
            y = x*x + 81
            yhasil = y - ylama
            x = x + xhasil
            
            time.sleep(0.035)
            self.canvas.move(self.alien2, xhasil + yhasil ,yhasil  )
            self.canvas.update()
            print(" - y "+ str(y))
            
            if y >=480 and x > -10:
                jalan = False

            
            

alien()
