from tkinter import*
top = Tk()
C=Canvas(top,height=500,width=500)
L1=Label(top,text="enter A value")
L1.place(x=10,y=10)
E1=Entry(top)
E1.place(x=100,y=10)
L2=Label(top,text="enter B Value")
L2.place(x=10,y=50)
E2=Entry(top)
E2.place(x=100,y=50)
L3=Label(top,text="Result")
L3.place(x=10,y=150)
E3=Entry(top)
E3.place(x=100,y=150)
def add():
    E3.delete(0,END)
    a=int(E1.get())
    b=int(E2.get())
    c=a+b
    E3.insert(0,str(c))

def sub():
    E3.delete(0,END)
    a=int(E1.get())
    b=int(E2.get())
    c=a-b
    E3.insert(0,str(c))
def mul():
    E3.delete(0,END)
    a=int(E1.get())
    b=int(E2.get())
    c=a*b
    E3.insert(0,str(c))
def div():
    E3.delete(0,END)
    a=int(E1.get())
    b=int(E2.get())
    c=a/b
    E3.insert(0,str(c))

B1=Button(top,text="ADD",command=add)
B1.place(x=10,y=100)
B2=Button(top,text="Sub",command=sub)
B2.place(x=60,y=100)
B3=Button(top,text="Mul",command=mul)
B3.place(x=110,y=100)
B4=Button(top,text="Div",command=div)
B4.place(x=160,y=100)
C.pack()
top.mainloop()
