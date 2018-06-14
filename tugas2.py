from Tkinter import *
import time

lebar = 600
tinggi = 400

tk = Tk()
canvas = Canvas(tk, width=lebar, height=tinggi)
tk.title("Gambar Bola Bergerak")

canvas.pack()
#membuat bola
bola = canvas.create_oval(10, 10, 70, 70, fill="orange")
bola2 = canvas.create_oval(10, 10, 70, 70, fill="blue")
bola3 = canvas.create_oval(10, 10, 70, 70, fill="red")

#mengatur kecepatan bola
kecepatanx = 4
kecepatany = 5
kecepatanx1 = 2
kecepatany1 = 3
kecepatanx2 = 3
kecepatany2 = 4

#melooping bola dengan menggunakan kecepatan x dan y
while True:
    canvas.move(bola, kecepatanx, kecepatany)
    canvas.move(bola2, kecepatanx1, kecepatany1)
    canvas.move(bola3, kecepatanx2, kecepatany2)
    pos = canvas.coords(bola)
    pos2 = canvas.coords(bola2)
    pos3 = canvas.coords(bola3)
    if pos3[3] >= tinggi or pos3[1] <= 0:
        kecepatany2 = -kecepatany2
    if pos3[2] >= lebar or pos3[0] <= 0:
        kecepatanx2 = -kecepatanx2
    
    if pos2[3] >= tinggi or pos2[1] <= 0:
        kecepatany1 = -kecepatany1
    if pos2[2] >= lebar or pos2[0] <= 0:
        kecepatanx1 = -kecepatanx1
    
    if pos[3] >= tinggi or pos[1] <= 0:
        kecepatany = -kecepatany
    if pos[2] >= lebar or pos[0] <= 0:
        kecepatanx = -kecepatanx
    tk.update()
    time.sleep(0.001)

tk.mainloop()

  
