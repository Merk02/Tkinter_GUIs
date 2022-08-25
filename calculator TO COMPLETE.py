import tkinter as tk


def t_1():
     
    global string
    string += '1'
    s.set(string)
    entry['textvariable'] = s
    
    
def t_2():
    
    global string
    string += '2' 
    s.set(string)
    entry['textvariable'] = s

    
def t_3():
    
    global string
    string += '3' 
    s.set(string)
    entry['textvariable'] = s


def t_4():
    
    global string
    string += '4' 
    s.set(string)
    entry['textvariable'] = s


def t_5():
    
    global string
    string += '5' 
    s.set(string)
    entry['textvariable'] = s


def t_6():
    
    global string
    string += '6' 
    s.set(string)
    entry['textvariable'] = s


def t_7():
    
    global string
    string += '7' 
    s.set(string)
    entry['textvariable'] = s


def t_8():
    
    global string
    string += '8' 
    s.set(string)
    entry['textvariable'] = s


def t_9():
    
    global string
    string += '9' 
    s.set(string)
    entry['textvariable'] = s
    
    
def t_0():
    
    global string
    string += '0' 
    s.set(string)
    entry['textvariable'] = s
    
    
def t_comma():
    
    global string
    string += '.' 
    s.set(string)
    entry['textvariable'] = s


def t_C():
    
    global a, b, add, sub, mult, div, string
    a = 0
    b = ''
    string = '' 
    add = 0
    sub = 0
    mult = 0
    div = 0
    s.set('0')
    entry['textvariable'] = s
    


def addition():
    
    global a, add, string
    if add == 0:
        
        add += 1
        a = float(string)
        
    else:
        a += float(string)
        
    string = ''
    

def subtraction():
    
    global a, sub, string
    
    if sub == 0:
        
        sub += 1
        a = float(string)
        
    else:
        
        a -= float(string)

    string = ''
    

def multiplication():
    
    global a, mult, string
    
    if mult == 0:
        
        mult += 1
        a = float(string) 
    
    else:
        
        a *= float(string)
        
    string = ''
    
    
def division():
    
    global a, div, string
    
    if div == 0:
        
        div += 1
        a = float(string) 
    
    else:
        
        a /= float(string)
        
    string = ''

    
def t_equal():
    
    global a, b, add, sub, mult, div, string
    
    if add > 0:
        
        b = a + float(string)
        
    elif sub > 0:
        
        b = a - float(string)
        
    elif mult > 0:
        
        b = a * float(string)
        
    elif div > 0:
        
        b = a / float(string)
        
    s.set(b)
    entry['textvariable'] = s
    string = ''
    add = 0
    sub = 0
    mult = 0
    div = 0
  
    

    
master = tk.Tk()


a = 0
b = ''
string = ''
add = 0
sub = 0
mult = 0
div = 0

s = tk.StringVar()
s.set('0')

entry = tk.Entry(master, width=24, font=('Arial, 20'), textvariable=s, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=50)


tC = tk.Button(master, text='C',  width=4, font=('Arial, 20'), command=t_C)
tC.grid(row=4, column=0)

t0 = tk.Button(master, text='0',  width=4, font=('Arial, 20'), command=t_0)
t0.grid(row=4, column=1)

t1 = tk.Button(master, text='1',  width=4, font=('Arial, 20'), command=t_1)
t1.grid(row=3, column=0)

t2 = tk.Button(master, text='2', width=4, font=('Arial, 20'), command=t_2)
t2.grid(row=3, column=1)

t3 = tk.Button(master, text='3',  width=4, font=('Arial, 20'), command=t_3)
t3.grid(row=3, column=2)

t4 = tk.Button(master, text='4',  width=4, font=('Arial, 20'), command=t_4)
t4.grid(row=2, column=0)

t5 = tk.Button(master, text='5',  width=4, font=('Arial, 20'), command=t_5)
t5.grid(row=2, column=1)

t6 = tk.Button(master, text='6',  width=4, font=('Arial, 20'), command=t_6)
t6.grid(row=2, column=2)

t7 = tk.Button(master, text='7',  width=4, font=('Arial, 20'), command=t_7)
t7.grid(row=1, column=0)

t8 = tk.Button(master, text='8',  width=4, font=('Arial, 20'), command=t_8)
t8.grid(row=1, column=1)

t9 = tk.Button(master, text='9',  width=4, font=('Arial, 20'), command=t_9)
t9.grid(row=1, column=2)


tplus = tk.Button(master, text='+',  width=4, font=('Arial, 20'), command=addition)
tplus.grid(row=1, column=6)

tminus = tk.Button(master, text='-',  width=4, font=('Arial, 20'), command=subtraction)
tminus.grid(row=2, column=6)

tper = tk.Button(master, text='*',  width=4, font=('Arial, 20'), command=multiplication)
tper.grid(row=3, column=6)

tdivide = tk.Button(master, text='/',  width=4, font=('Arial, 20'), command=division)
tdivide.grid(row=4, column=6)


tcomma = tk.Button(master, text=',',  width=4, font=('Arial, 20'), command=t_comma)
tcomma.grid(row=4, column=2)


tequal = tk.Button(master, text='=',  width=4, font=('Arial, 20'), command=t_equal)
tequal.grid(row=4, column=3)


tk.mainloop()


