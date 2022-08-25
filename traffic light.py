
import tkinter as tk


def traffic():
    
    if l[0] == True:
        
        circle1 = canvas.create_oval(50, 20,
                           210, 180,
                           outline='white',
                           fill='red',
                           width=5)
        
    else:
        
        circle1 = canvas.create_oval(50, 20,
                           210, 180,
                           outline='white',
                           fill='black',
                           width=5)
        
        
    if l[1] == True:
        
        circle2 = canvas.create_oval(50, 200,
                           210, 363,
                           outline='white',
                           fill='yellow',
                           width=5)
        
    else:
        
        circle2 = canvas.create_oval(50, 200,
                           210, 363,
                           outline='white',
                           fill='black',
                           width=5)
        
    if l[2] == True:
        
        circle3 = canvas.create_oval(50, 380,
                           210, 550,
                           outline='white',
                           fill='lime green',
                           width=5)
        
    else:

        circle3 = canvas.create_oval(50, 380,
                           210, 550,
                           outline='white',
                           fill='black',
                           width=5)



def Next():
    
    button_next['text'] = 'Next'
    global t, l
    t += 1
    c = t % 4
    l = phases[c-1]
    traffic()



phases = ((True, False, False), 
          (True, True, False), 
          (False, False, True),
          (False, True, False))

l = []
t = 1


master = tk.Tk()


canvas = tk.Canvas(master, width=250, height=600, bg='black')
canvas.grid(row=0, column=0)



button_next = tk.Button(master, text='Start', height=0, width=6, font=('Arial', '17'), command=Next)
button_next.grid(row=1, column=0)


button_quit = tk.Button(master, text='Quit', height=0, width=6, font=('Arial', '17'), command=master.destroy)
button_quit.grid(row=2, column=0)



master.mainloop()