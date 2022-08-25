
import tkinter as tk

def N():
    pass

        
def counter():
    
    global c
    c += 1


def click1():
    
    if c % 2 == 0:
    
        b1['text'] = 'O'
    
    else:
        
        b1['text'] = 'X'
    
    b1['command'] = N
    counter()
    

def click2():
    
    if c % 2 == 0:
    
        b2['text'] = 'O'
    
    else:
        
        b2['text'] = 'X'
    
    b2['command'] = N
    counter()
    
    
def click3():
    
    if c % 2 == 0:
    
        b3['text'] = 'O'
    
    else:
        
        b3['text'] = 'X'
    
    b3['command'] = N
    counter()
    
    
def click4():
    
    if c % 2 == 0:
    
        b4['text'] = 'O'
    
    else:
        
        b4['text'] = 'X'
    
    b4['command'] = N
    counter()
    
    
def click5():
    
    if c % 2 == 0:
    
        b5['text'] = 'O'
    
    else:
        
        b5['text'] = 'X'
    
    b5['command'] = N
    counter()
    
    
def click6():
    
    if c % 2 == 0:
    
        b6['text'] = 'O'
    
    else:
        
        b6['text'] = 'X'
    
    b6['command'] = N
    counter()
    
    
def click7():
    
    if c % 2 == 0:
    
        b7['text'] = 'O'
    
    else:
        
        b7['text'] = 'X'
    
    b7['command'] = N
    counter()
    
    
def click8():
    
    if c % 2 == 0:
    
        b8['text'] = 'O'
    
    else:
        
        b8['text'] = 'X'
    
    b8['command'] = N
    counter()
    
    
def click9():
    
    if c % 2 == 0:
    
        b9['text'] = 'O'
    
    else:
        
        b9['text'] = 'X'
    
    b9['command'] = N
    counter()
    

c = 0

master = tk.Tk()


b1 = tk.Button(master, text='', width=4, height=1, font=('Arial', '50', 'bold'), command=click1)
b1.grid(row=0, column=0)

b2 = tk.Button(master, text='', width=4, height=1, font=('Arial', '50', 'bold'), command=click2)
b2.grid(row=0, column=1)

b3 = tk.Button(master, text='', width=4, height=1, font=('Arial', '50', 'bold'), command=click3)
b3.grid(row=0, column=2)

b4 = tk.Button(master, text='', width=4, height=1, font=('Arial', '50', 'bold'), command=click4)
b4.grid(row=1, column=0)

b5 = tk.Button(master, text='', width=4, height=1, font=('Arial', '50', 'bold'), command=click5)
b5.grid(row=1, column=1)

b6 = tk.Button(master, text='', width=4, height=1, font=('Arial', '50', 'bold'), command=click6)
b6.grid(row=1, column=2)

b7 = tk.Button(master, text='', width=4, height=1, font=('Arial', '50', 'bold'), command=click7)
b7.grid(row=2, column=0)

b8 = tk.Button(master, text='', width=4, height=1, font=('Arial', '50', 'bold'), command=click8)
b8.grid(row=2, column=1)

b9 = tk.Button(master, text='', width=4, height=1, font=('Arial', '50', 'bold'), command=click9)
b9.grid(row=2, column=2)


master.mainloop()