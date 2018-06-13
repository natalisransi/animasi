from tkinter import *
import time

lebar = 600
tinggi = 400
tk = Tk()
canvas = Canvas(tk, width=lebar, height=tinggi)
tk.title("Gambar Bola Bergerak")

canvas.pack()

bola = canvas.create_oval(10, 10, 70, 70, fill="orange")
bola1 = canvas.create_oval(10, 10, 70, 70, fill="red")
kecepatanx = 4
kecepatany = 5

kecepatanx1 = 3
kecepatany1 = 4

while True:
    canvas.move(bola, kecepatanx, kecepatany)
    canvas.move(bola1, kecepatanx1, kecepatany1)
    pos = canvas.coords(bola)
    pos1 = canvas.coords(bola1)
    
    if pos[3] >= tinggi or pos[1] <= 0:
        kecepatany = -kecepatany
    if pos[2] >= lebar or pos[0] <= 0:
        kecepatanx = -kecepatanx
    if pos1[3] >= tinggi or pos1[1] <= 0:
        kecepatany1 = -kecepatany1
    if pos1[2] >= lebar or pos1[0] <= 0:
        kecepatanx1 = -kecepatanx1
    tk.update()
    time.sleep(0.001)

tk.mainloop()

