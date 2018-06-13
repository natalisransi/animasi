from tkinter import *
import time

lebar = 800
tinggi = 600

tk = Tk()
canvas = Canvas(tk, width=lebar, height=tinggi)
tk.title("Gambar Bola Bergerak")

canvas.pack()

bola = canvas.create_oval(10, 10, 70, 70,outline='white', fill="orange")
bola1 = canvas.create_oval(10, 10, 70, 70,outline='white', fill="blue")
bola2 = canvas.create_oval(10, 10, 70, 70,outline='white', fill="red")

kecepatanx = 2
kecepatany = 4
kx1=1
ky1=2

kx2=2
ky2=2

while True:
    canvas.move(bola, kecepatanx, kecepatany)
    canvas.move(bola1, kx1, ky2)
    canvas.move(bola2, kx2, ky2)

    pos = canvas.coords(bola)
    pos1 = canvas.coords(bola1)
    pos2 = canvas.coords(bola2)

    if pos[3] >= tinggi or pos[1] <= 0:
        kecepatany = -kecepatany
    if pos[2] >= lebar or pos[0] <= 0:
        kecepatanx = -kecepatanx

    if pos1[3] >= tinggi or pos1[1] <= 0:
        ky1 = -ky1
    if pos1[2] >= lebar or pos1[0] <= 0:
        kx1 = -kx1

    if pos2[3] >= tinggi or pos2[1] <= 0:
        ky2 = -ky2
    if pos2[2] >= lebar or pos2[0] <= 0:
        kx2 = -kx2


    tk.update()
    time.sleep(0.002)


tk.mainloop()
