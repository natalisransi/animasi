from tkinter import *
import time

lebar = 700
tinggi = 500

tk = Tk()
canvas = Canvas(tk, width=lebar, height=tinggi)
tk.title("Gambar Bola Bergerak")

canvas.pack()

bola = canvas.create_oval(10, 10, 70, 70,outline='red', fill="pink")
bola1 = canvas.create_oval(10, 10, 70, 70,outline='red', fill="blue")
bola2 = canvas.create_oval(10, 10, 70, 70,outline='red', fill="yellow")

kecepatanx = 2
kecepatany = 4
kecx1=1
kecy1=2

kecx2=2
kecy2=2

while True:
    canvas.move(bola, kecepatanx, kecepatany)
    canvas.move(bola1, kecx1, kecy2)
    canvas.move(bola2, kecx2, kecy2)

    pos = canvas.coords(bola)
    pos1 = canvas.coords(bola1)
    pos2 = canvas.coords(bola2)

    if pos[3] >= tinggi or pos[1] <= 0:
        kecepatany = -kecepatany
    if pos[2] >= lebar or pos[0] <= 0:
        kecepatanx = -kecepatanx

    if pos1[3] >= tinggi or pos1[1] <= 0:
        kecy1 = -kecy1
    if pos1[2] >= lebar or pos1[0] <= 0:
       kecx1 = -kecx1

    if pos2[3] >= tinggi or pos2[1] <= 0:
        kecy2 = -kecy2
    if pos2[2] >= lebar or pos2[0] <= 0:
        kecx2 = -kecx2


    tk.update()
    time.sleep(0.002)


tk.mainloop()
