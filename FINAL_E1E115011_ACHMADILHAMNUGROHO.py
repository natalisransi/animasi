from tkinter import *
import time

lebar = 600
tinggi = 400

tk = Tk()
canvas = Canvas(tk, width=lebar, height=tinggi)
tk.title("FINAL BOLA BERGERAK")

canvas.pack()

bola = canvas.create_oval(10, 10, 70, 70, fill="red")
bola2 = canvas.create_oval(20, 20, 70, 70, fill="yellow")
bola3 = canvas.create_oval(10, 10, 70, 70, fill="green")
bola4 = canvas.create_oval(10, 10, 70, 70, fill="blue")

kecepatanx = 0.5
kecepatany = 0.5

kecepatanx2 = 1
kecepatany2 = 1

kecepatanx3 = 1.5
kecepatany3 = 1.5

kecepatanx4 = 2
kecepatany4 = 2

while True:
    canvas.move(bola, kecepatanx, kecepatany)
    pos = canvas.coords(bola)
    if pos[3] >= tinggi or pos[1] <= 0:
        kecepatany = -kecepatany
    if pos[2] >= lebar or pos[0] <= 0:
        kecepatanx = -kecepatanx
    tk.update()
    time.sleep(0.001)


    canvas.move(bola2, kecepatanx2, kecepatany2)
    pos = canvas.coords(bola2)
    if pos[3] >= tinggi or pos[1] <= 0:
        kecepatany2 = -kecepatany2
    if pos[2] >= lebar or pos[0] <= 0:
        kecepatanx2 = -kecepatanx2
    tk.update()
    time.sleep(0.001)

    canvas.move(bola3, kecepatanx3, kecepatany3)
    pos = canvas.coords(bola3)
    if pos[3] >= tinggi or pos[1] <= 0:
        kecepatany3 = -kecepatany3
    if pos[2] >= lebar or pos[0] <= 0:
        kecepatanx3 = -kecepatanx3
    tk.update()
    time.sleep(0.001)

    canvas.move(bola4, kecepatanx4, kecepatany4)
    pos = canvas.coords(bola4)
    if pos[3] >= tinggi or pos[1] <= 0:
        kecepatany4 = -kecepatany4
    if pos[2] >= lebar or pos[0] <= 0:
        kecepatanx4 = -kecepatanx4
    tk.update()
    time.sleep(0.001)
    

print("Coba")
tk.mainloop()