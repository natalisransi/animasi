from tkinter import *
import time

lebar = 600
tinggi = 400

tk = Tk()
canvas = Canvas(tk, width=lebar, height=tinggi)
tk.title("Gambar Bola Banyak Bergerak")

canvas.pack()

bola = canvas.create_oval(10, 10, 70, 70, fill="yellow")
bola2 = canvas.create_oval(10, 10, 70, 70, fill="red")
bola3 = canvas.create_oval(10, 10, 70, 70, fill="blue")
kecepatanx = 4
kecepatany = 1
kecepatanx = 3
kecepatany = 2
kecepatanx = 3
kecepatany = 1

while True:
    canvas.move(bola, kecepatanx, kecepatany)
    pos = canvas.coords(bola)
    if pos[3] >= tinggi or pos[1] <= 0:
        kecepatany = -kecepatany
    if pos[2] >= lebar or pos[0] <= 0:
        kecepatanx = -kecepatanx
    tk.update()
    time.sleep(0.001)

    canvas.move(bola2, kecepatanx, kecepatany)
    pos = canvas.coords(bola2)
    if pos[3] >= tinggi or pos[1] <= 0:
        kecepatany = -kecepatany
    if pos[2] >= lebar or pos[0] <= 0:
        kecepatanx = -kecepatanx
    tk.update()
    time.sleep(0.001)

    canvas.move(bola3, kecepatanx, kecepatany)
    pos = canvas.coords(bola3)
    if pos[3] >= tinggi or pos[1] <= 0:
        kecepatany = -kecepatany
    if pos[2] >= lebar or pos[0] <= 0:
        kecepatanx = -kecepatanx
    tk.update()
    time.sleep(0.001)

tk.mainloop()
