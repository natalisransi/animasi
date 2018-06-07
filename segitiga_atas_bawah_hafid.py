from tkinter import *
import time
import math


class segitiga(object):
     def __init__(self):

        #Membuat Layar
        self.root = Tk()
        self.canvas = Canvas(self.root, width=1000, height = 1000)

        #Membuat Objek Segitiga
        self.canvas.pack()
        self.model = self.canvas.create_polygon((25, 950, 50, 1000, 0, 1000),outline="red",fill="white")
        self.canvas.pack()
        self.root.after(0, self.animation)
        self.root.mainloop()
        

     def animation(self):
        #inisialisasi nilai awal
        x = 2
        y = 0


        #kecepatan pindah kordinat
        xhasil = 1

        loop = 0


        #menjalankan animasi
        jalan = True
        while jalan:
            ylama = y
            #persamaan kuadrat
            y = x*x  - 100*x + 1450

            yhasil = y - ylama
            x = x + xhasil
            
            time.sleep(0.025)
            self.canvas.move(self.model, xhasil, yhasil)
            self.canvas.update()

            if y == 0:
                print(str(xhasil) + " " + str(xhasil) + "Stop")
                loop = loop +1
                
            else:
                print("Coba : "+str(loop)+" - y : "+str(y)+" - x : "+str(x))


            #kondisi bila posisi segitiga melewati layar (loop)
            if x == 90:
                x = 2

            
segitiga()

