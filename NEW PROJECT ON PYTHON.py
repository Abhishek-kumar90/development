from tkinter import *
a=Tk()
a.minsize(width=200,height=150)
a.maxsize(width=900,height=500)

def func():
    x=var.get()
    y=var1.get()
    print(x)
    print(y)
    #lb1.config(text=x)
    #lb2.config(text=y)
def fun():
    if ravar.get()==0:
        print("male")
    else:
        print("female")
    #print(ravar.get())
    #print(ravar1.get())


lb1=Label(a,text="username",bg="pink",fg="red")
lb2=Label(a,text="password",bg="pink",fg="red")
lb1.place(x=10,y=20)
lb2.place(x=10,y=45)
lb1=Label(a,text="nothing",bg="pink",fg="red")
lb2=Label(a,text="nothing",bg="pink",fg="red")
lb1.pack()
lb2.pack()


#lbl.grid(width=300,height=200)
var=StringVar()
ent=Entry(a,bg="white",fg="black",bd=2,textvariable=var)
ent.place(x=80,y=20)
var1=StringVar()
ent1=Entry(a,bg="white",fg="black",bd=2,textvariable=var1)
ent1.place(x=80,y=45)
butt=Button(a,text="ok",bg="yellow",fg="red",command=func)
butt.place(x=10,y=80)

ravar=IntVar()
rad=Radiobutton(a,text="male",value=0,variable=ravar).pack()
rad=Radiobutton(a,text="female",value=1,variable=ravar).pack()

butt1=Button(a,text="submit",bg="white",fg="black",command=fun).place(x=50,y=190)
a.mainloop()
