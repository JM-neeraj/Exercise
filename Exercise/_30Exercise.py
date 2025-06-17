# Configuring the appearance of a widget
# 1.Set the font size of the addition calculator and the color of the widget as follows. Set the background color to '#ffffc0' (light yellow) for the frame, white for numeric keys, red for clear keys, and green for + and = keys.
# 2.The size of the button should be 2 (the length in characters).
# 3.The font and size of the button and entry should be ('Helvetica', 14).

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

f = Frame(root, bg="#ffffc0")
b = Button(f, text='7', font='Helvetica 14 ' ,padx=25, pady=15, fg='white')
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)

b = Button(f, text='8', font='Helvetica 14 ' ,padx=25, pady=15, fg='white')
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)

b = Button(f, text='9', font='Helvetica 14 ' ,padx=25, pady=15, fg='white')
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)

b = Button(f, text='/', font='Helvetica 14 ' ,padx=25, pady=15, fg='white')
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="#ffffc0")
b = Button(f, text='4', font='Helvetica 14 ' ,padx=25, pady=15, fg='white')
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)

b = Button(f, text='5', font='Helvetica 14 ' ,padx=25, pady=15, fg='white')
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)

b = Button(f, text='6', font='Helvetica 14 ' ,padx=25, pady=15, fg='white')
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)

b = Button(f, text='*', font='Helvetica 14 ' ,padx=25, pady=15, fg='white')
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)
f.pack()


f = Frame(root, bg="#ffffc0")
b = Button(f, text='1', font='Helvetica 14 ' ,padx=25, pady=15, fg='white')
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)

b = Button(f, text='2', font='Helvetica 14 ' ,padx=25, pady=15, fg='white')
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)

b = Button(f, text='3', font='Helvetica 14 ' ,padx=25, pady=15, fg='white')
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)

b = Button(f, text='-', font='Helvetica 14 ' ,padx=25, pady=15, fg='white')
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="#ffffc0")
b = Button(f, text='0', font='Helvetica 14 ' ,padx=25, pady=15, fg='white')
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)

b = Button(f, text='C', font='Helvetica 14 ' ,padx=25, pady=15, fg='red')
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)

b = Button(f, text='=', font='Helvetica 14 ' ,padx=25, pady=15, fg='green')
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)

b = Button(f, text='+', font='Helvetica 14 ' ,padx=25, pady=15, fg='green')
b.pack(side=LEFT,  padx=8, pady=8)
b.bind("<Button-1>", click)
f.pack()

root.mainloop()
