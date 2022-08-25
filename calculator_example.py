
import tkinter as tk



def addition():
    global selection
    selection = plus['value']
    
def subtraction():
    global selection
    selection = minus['value']

def multiplication():
    global selection
    selection = by['value']

def division():
    global selection
    selection = divided['value']


def evaluate():
    
    if selection == 0:
        print(int(entry1.get()) + int(entry2.get()))
        
    elif selection == 1:
        print(int(entry1.get()) - int(entry2.get()))
    
    elif selection == 2:
        print(int(entry1.get()) * int(entry2.get()))
    
    elif selection == 3:
        print(int(entry1.get()) / int(entry2.get()))
    
    
master = tk.Tk()


selection = 0

entry1 = tk.Entry(master, width=20)
entry1.grid(row=1, column=0)

entry2 = tk.Entry(master, width=20)
entry2.grid(row=1, column=3)


var = tk.IntVar().set(1)

plus = tk.Radiobutton(master, text='+', variable=var, value=0, command=addition)
plus.grid(row=0, column=1)

minus = tk.Radiobutton(master, text='-', variable=var, value=1, command=subtraction)
minus.grid(row=1, column=1)

by = tk.Radiobutton(master, text='*', variable=var, value=2, command=multiplication)
by.grid(row=2, column=1)

divided = tk.Radiobutton(master, text='/', variable=var, value=3, command=division)
divided.grid(row=3, column=1)


button = tk.Button(master, text='evaluate', command=evaluate)
button.grid(row=4, column=1)



tk.mainloop()