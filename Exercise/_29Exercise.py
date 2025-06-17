# 1 Create an Addition Calculator with Tkinter 
from tkinter import *

def click(event):
    global calcvalue
    text = event.widget.cget('text')
    print(text)
    
    if text == "=":
        try:
            value = eval(calcvalue.get())
        except Exception:
            value = "Error"
        calcvalue.set(value)

    elif text == "C":
        calcvalue.set("")

    else:
        calcvalue.set(calcvalue.get() + text)

        



root = Tk()
root.geometry('645x745')

calcvalue = StringVar()
calcvalue.set('')
screen = Entry(root, textvariable=calcvalue, font= 'lucida 40 bold')
screen.pack(fill=X, padx=10, pady=8)

f = Frame(root)
b = Button(f, text='7', font='lucida 28 bold' ,padx=25, pady=15,)
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)

b = Button(f, text='8', font='lucida 28 bold' ,padx=25, pady=15,)
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)

b = Button(f, text='9', font='lucida 28 bold' ,padx=25, pady=15,)
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)

b = Button(f, text='/', font='lucida 28 bold' ,padx=25, pady=15,)
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root)
b = Button(f, text='4', font='lucida 28 bold' ,padx=25, pady=15,)
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)

b = Button(f, text='5', font='lucida 28 bold' ,padx=25, pady=15,)
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)

b = Button(f, text='6', font='lucida 28 bold' ,padx=25, pady=15,)
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)

b = Button(f, text='*', font='lucida 28 bold' ,padx=25, pady=15,)
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root)
b = Button(f, text='1', font='lucida 28 bold' ,padx=25, pady=15,)
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)

b = Button(f, text='2', font='lucida 28 bold' ,padx=25, pady=15,)
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)

b = Button(f, text='3', font='lucida 28 bold' ,padx=25, pady=15,)
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)

b = Button(f, text='-', font='lucida 28 bold' ,padx=25, pady=15,)
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root)
b = Button(f, text='0', font='lucida 28 bold' ,padx=25, pady=15,)
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)

b = Button(f, text='C', font='lucida 28 bold' ,padx=25, pady=15,)
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)

b = Button(f, text='=', font='lucida 28 bold' ,padx=25, pady=15,)
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)

b = Button(f, text='+', font='lucida 28 bold' ,padx=25, pady=15,)
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)
f.pack()

root.mainloop()
