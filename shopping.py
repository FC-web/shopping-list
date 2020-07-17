from tkinter import *

wndw = Tk()
wndw.title('shopping list')
wndw.geometry('400x500+800+80')
wndw.resizable(0, 0)
show = Label(text='SHOPPING LIST MANAGER', font=12).pack()
Label(text='ADD ITEM ').pack()
inpu = StringVar()
fill = Entry(textvariable=inpu, border=1.2).pack()
v = []


def shw():
    global v
    for i in v:
        lable3 = Label(text=i).pack()
        print(i)


def add():
    global v
    label1 = Label(text=v.append(inpu.get())).pack()
    print(inpu.get())


btn1 = Button(text='ADD', border=1.2, command=add).pack()


def rmv():
    global v
    lable1 = Label(text=v.remove(inpu.get())).pack()
    print(v)


btn2 = Button(text='Remove', border=1.2, command=rmv).pack()

btn4 = Button(text='Show Items', border=1.2, command=shw).pack()


def new():
    global v
    Label(text=v.clear()).pack()


btn3 = Button(text='New Entry', border=1.2).pack()

wndw.mainloop()
