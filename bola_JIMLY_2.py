from tkinter import *
import time

lebar = 600
tinggi = 400

tk = Tk()
canvas = Canvas(tk, width=lebar, height=tinggi)
tk.title("Gambar Bola Bergerak")

canvas.pack()

bola = canvas.create_oval(10, 10, 70, 70, fill="orange")
bola2 = canvas.create_oval(10, 10, 70, 70, fill="red")
bola3 = canvas.create_oval(10, 10, 70, 70, fill="blue")
kecepatanx = 19
kecepatany = 21
x2 = 20
y2 = 15
x3 = 17
y3 = 18

while True:
    canvas.move(bola, kecepatanx, kecepatany)
    pos = canvas.coords(bola)
    canvas.move(bola2, x2, y2)
    pos2 = canvas.coords(bola2)
    canvas.move(bola3, x3, y3)
    pos3 = canvas.coords(bola3)
    
    if pos[3] >= tinggi or pos[1] <= 0:
        kecepatany = -kecepatany
    if pos[2] >= lebar or pos[0] <= 0:
        kecepatanx = -kecepatanx
    tk.update()
    time.sleep(0.001)

 
    if pos2[3] >= tinggi or pos2[1] <= 0:
        y2 = -y2
    if pos2[2] >= lebar or pos2[0] <= 0:
        x2 = -x2
    tk.update()
    time.sleep(0.001)

  
    if pos3[3] >= tinggi or pos3[1] <= 0:
        y3 = -y3
    if pos3[2] >= lebar or pos3[0] <= 0:
        x3 = -x3
    tk.update()
    time.sleep(0.001)

tk.mainloop()
