from tkinter import *
import time

lebar = 600
tinggi = 400

tk = Tk()
canvas = Canvas(tk, width=lebar, height=tinggi)
tk.title("Gambar Bola Bergerak")

canvas.pack()

bola = canvas.create_oval(10, 10, 70, 70, fill="pink")
bola2 = canvas.create_oval(10, 10, 70, 70, fill="green")

kecepatanx = 10
kecepatany = 20
kecepatanx2 = 10
kecepatany2 = 30
while True:
    canvas.move(bola, kecepatanx, kecepatany)
    pos = canvas.coords(bola)
    
    if pos[3] >= tinggi or pos[1] <= 0:
        kecepatany = -kecepatany
    if pos[2] >= lebar or pos[1] <= 0:
        kecepatanx = -kecepatanx
    tk.update()
    time.sleep(0.01)

    canvas.move(bola2, kecepatanx2, kecepatany2)
    pos2 = canvas.coords(bola2)
    
    if pos2[3] >= tinggi or pos2[1] <= 0:
        kecepatany2 = -kecepatany2
    if pos2[2] >= lebar or pos2[1] <= 0:
        kecepatanx2 = -kecepatanx2
       
    tk.update()
    time.sleep(0.001)
    



    


tk.mainloop()