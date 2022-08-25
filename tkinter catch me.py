import tkinter as tk
from random import randint


def change():
    global pos_x, pos_y
    pos_x = randint(1, 130) + 10
    pos_y = randint(1, 170) + 10
    if pos_x > 130:
        pos_x -= 130
    if pos_y > 170:
        pos_y -= 170
    return pos_x, pos_y

def motion(ev=None):
    change()
    button.place(x=pos_x, y=pos_y)

def destroy():
    return master.destroy()


master = tk.Tk()
master.title('<Catch me!> game')

pos_x = 0
pos_y = 0

button = tk.Button(master, text='Catch me!', command=destroy)
button.place(x=130, y=170)
button.bind('<Enter>', motion)

tk.mainloop()
