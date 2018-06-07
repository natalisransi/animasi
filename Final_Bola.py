from tkinter import *
import time

lebar = 600
tinggi = 400

tk = Tk()
canvas = Canvas(tk, width=lebar, height=tinggi)
tk.title("Gambar Bola Bergerak (Artono Dwi Ramadhan : E1E115008)")

canvas.pack()

bola = canvas.create_oval(10, 10, 70, 70, fill="orange")
bola2 = canvas.create_oval(20, 20, 80, 80, fill="green")
bola3 = canvas.create_oval(20, 20, 80, 80, fill="red")
kecepatanx = 4
kecepatany = 5
x2 = 3
y2 = 7
x3 = 0
y3 = 5

while True:
    canvas.move(bola, kecepatanx, kecepatany)
    canvas.move(bola2, x2, y2)
    canvas.move(bola3, x3, y3)

    pos = canvas.coords(bola)
    pos2 = canvas.coords(bola2)
    pos3 = canvas.coords(bola3)

    if pos[3] >= tinggi or pos[1] <= 0:
        kecepatany = -kecepatany
    if pos[2] >= lebar or pos[0] <= 0:
        kecepatanx = -kecepatanx

    if pos2[3] >= tinggi or pos2[1] <= 0:
        y2 = -y2
    if pos2[2] >= lebar or pos2[0] <= 0:
        x2 = -x2

    if pos3[3] >= tinggi or pos3[1] <= 0:
        y3 = -y3
    if pos3[2] >= lebar or pos3[0] <= 0:
        x3 = -x3

    tk.update()
    time.sleep(0.018)

tk.mainloop()