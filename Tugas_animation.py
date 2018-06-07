import time
from tkinter import*
animation =Tk()
canvas=Canvas(animation, width= 800, height=600)
canvas.pack()
canvas.create_oval(10, 10, 70, 70, fill="green")
for x in range(0, 70):
    canvas.move(1, 5, 3)
    animation.update()
    time.sleep(0.008)
    
for x in range(0, 70):
    canvas.move(1, -5, 3)
    animation.update()
    time.sleep(0.008)

for x in range(0, 80):
    canvas.move(1, 5, -3)
    animation.update()
    time.sleep(0.008)
    
for x in range(0, 140):
    canvas.move(1, -5, -3)
    animation.update()
    time.sleep(0.008)

for x in range(0, 80):
    canvas.move(1, 5, 3)
    animation.update()
    time.sleep(0.008)
    
for x in range(0, 70):
    canvas.move(1, 5, 3)
    animation.update()
    time.sleep(0.008)
    
for x in range(0, 70):
    canvas.move(1, -5, 3)
    animation.update()
    time.sleep(0.008)

for x in range(0, 80):
    canvas.move(1, 5, -3)
    animation.update()
    time.sleep(0.008)
    
for x in range(0, 140):
    canvas.move(1, -5, -3)
    animation.update()
    time.sleep(0.005)

for x in range(0, 80):
    canvas.move(1, 5, 3)
    animation.update()
    time.sleep(0.08)
    
