from tkinter import *
import time

x = 600
y = 400

tk = Tk()
canvas = Canvas(tk, width=x, height=y)
tk.title("Gambar 2 Bola Bergerak dan Memantul")

canvas.pack()

bola = canvas.create_oval(10, 10, 70, 70, fill="red")
bola2 = canvas.create_oval(9, 9, 69, 69, fill="green")

speedBolax = 2
speedBolay = 2
speedBola2x = 5
speedBola2y = 5

while True:
    canvas.move(bola, speedBolax, speedBolay)
    pos = canvas.coords(bola)
    if pos[3] >= y or pos[1] <= 0:
        speedBolay = -speedBolay
    if pos[2] >= x or pos[0] <= 0:
        speedBolax = -speedBolax
    tk.update()
    time.sleep(0.01)

    canvas.move(bola2, speedBola2x, speedBola2y)
    pos = canvas.coords(bola2)
    if pos[3] >= y or pos[1] <= 0:
        speedBola2y = -speedBola2y
    if pos[2] >= x or pos[0] <= 0:
        speedBola2x = -speedBola2x
    tk.update()
    time.sleep(0.001)

tk.mainloop()
