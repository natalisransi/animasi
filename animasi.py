from tkinter import *

import time

import math





class alien2(object):



     lWidth = 600

     lHeight = 1000



     posX = 50

     posY = 150

     

     def __init__(self):



        

        self.root = Tk()

        self.canvas = Canvas(self.root, width=self.lWidth, height = self.lHeight)

        self.canvas.pack()


        self.alien2 = self.canvas.create_oval(self.posX+20, self.posY+20, self.posX+40, self.posY+40, outline='#26032C', fill='#60046E')

        self.canvas.pack()

        self.root.after(0, self.animation)

        self.root.mainloop()

        



     def animation(self):

        apa = 1000

        x = 15.4

        xhasil = 0.1

        y = 0

        coba = 0



        jalan = True

        while jalan:

            ylama = y

            y = x*x  - 2*x + 10

           

               

            yhasil = y - ylama

            x = x + xhasil

            

            time.sleep(0.010)

            self.canvas.move(self.alien2, xhasil, yhasil)

            self.canvas.update()



            if y == 0:
                coba = coba +1

                

            else:

                print ("Coba : "+str(coba)+" - y : "+str(y)+" - x : "+str(x))

                

            if coba == 2:

                jalan = False



            if y + 10 >= self.lHeight - self.posY:

                x = 5.4





alien2()
