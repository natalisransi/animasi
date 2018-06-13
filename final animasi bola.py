from tkinter import *
import random
import time

lebar = 600
tinggi = 400

tk = Tk()
canvas = Canvas(tk, width=lebar, height=tinggi)
tk.title("Animasi Bola Bergerak")

canvas.pack()

class Ball:
    def __init__(self, color):
        self.bola = canvas.create_oval(10, 10, 70, 70, fill=color)  
        self.kecepatanx = random.randrange(1, 10)
        self.kecepatany = random.randrange(1, 10)

    def move(self):
        canvas.move(self.bola, self.kecepatanx, self.kecepatany)
        pos = canvas.coords(self.bola)
        if pos[3] >= tinggi or pos[1] <= 0:
            self.kecepatany = -self.kecepatany
        if pos[2] >= lebar or pos[0] <= 0:
            self.kecepatanx = -self.kecepatanx

nball = Ball("blue")
nball2 = Ball("green")
nball3 = Ball("red")
nball4 = Ball("black")
nball5 = Ball("orange")

while True:
    nball.move()
    nball2.move()
    nball3.move()
    nball4.move()
    nball5.move()
    tk.update()
    time.sleep(0.02)
    
tk.mainloop() 
