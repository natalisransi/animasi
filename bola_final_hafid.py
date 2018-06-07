from tkinter import *
import time

lebar = 600
tinggi = 400

tk = Tk()
canvas = Canvas(tk, width=lebar, height=tinggi)
tk.title("Gambar Bola Bergerak")

canvas.pack()

bola = canvas.create_oval(10, 10, 70, 70, fill="orange")
bola2 = canvas.create_oval(10, 10, 70, 70, fill="blue")
bola3 = canvas.create_oval(10, 10, 70, 70, fill="red")
kecepatanx = 4
kecepatany = 5
kec1 = 3
kec2 = 4
kec11 = 2
kec22 = 3

while True:
    canvas.move(bola, kecepatanx, kecepatany)
    pos = canvas.coords(bola)
    if pos[3] >= tinggi or pos[1] <= 0:
        kecepatany = -kecepatany
    if pos[2] >= lebar or pos[0] <= 0:
        kecepatanx = -kecepatanx
    tk.update()
    time.sleep(0.001)

    canvas.move(bola2, kec1, kec2)
    pos2 = canvas.coords(bola2)
    if pos2[3] >= tinggi or pos2[1] <= 0:
        kec2 = -kec2
    if pos2[2] >= lebar or pos2[0] <= 0:
        kec1 = -kec1
    tk.update()
    time.sleep(0.001)

    canvas.move(bola3, kec11, kec22)
    pos3 = canvas.coords(bola2)
    if pos3[3] >= tinggi or pos3[1] <= 0:
        kec22 = -kec22
    if pos3[2] >= lebar or pos3[0] <= 0:
        kec11 = -kec11
    tk.update()
    time.sleep(0.001)

tk.mainloop()