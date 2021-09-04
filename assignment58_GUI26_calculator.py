import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Calculate the answer')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Type your first Number:')
label2.config(font=('helvetica', 10))
canvas1.create_window(100, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(100, 140, window=entry1)


label2 = tk.Label(root, text='Type your 2nd Number:')
label2.config(font=('helvetica', 10))
canvas1.create_window(300, 100, window=label2)

entry2=tk.Entry (root)
canvas1.create_window(300, 140, window=entry2)
def getSum ():
    
    x1 = entry1.get()
    x2=entry2.get()
    label3 = tk.Label(root, text= 'The sum of ' + x1 + '+' + x2 + ' is:',font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)
    
    label4 = tk.Label(root, text= float(x1) + float(x2),font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)
    
button1 = tk.Button(text='+', command=getSum, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(100, 180, window=button1)

def subtract():
    
    x1=entry1.get()
    x2=entry2.get()
    label5 = tk.Label(root, text= 'The answer of ' + x1 + '-' + x2 + ' is:',font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label5)
    
    label6 = tk.Label(root, text= float(x1) - float(x2),font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label6)

button2= tk.Button(text='-', command=subtract, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(150, 180, window=button2)

def product():
    x1=entry1.get()
    x2=entry2.get()
    label7 = tk.Label(root, text= 'The product of ' + x1 + '*' + x2 + ' is:',font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label7)
    
    label8 = tk.Label(root, text= float(x1) * float(x2),font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label8)

button3= tk.Button(text='*', command=product, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button3)

def divide():
    x1=entry1.get()
    x2=entry2.get()
    label9 = tk.Label(root, text= 'The quotient of ' + x1 + '/' + x2 + ' is:',font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label9)
    
    label10 = tk.Label(root, text= float(x1) / float(x2),font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label10)

button2= tk.Button(text='/', command=divide, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(250, 180, window=button2)
root.mainloop()