# from tkinter import *
# root = Tk()
# root.title("welcome boss")
# root.geometry('350x250')

# name_var=StringVar()
# pass_var=StringVar()


# lb1 = Label(root,text="hii")
# entry=Entry(root,textvariable=name_var)
# entry1=Entry(root,textvariable=pass_var)


# def func():
#     name_var.get()
#     pass_var.get()

# butt = Button(root,text="click me",bg="yellow",fg="blue",command=func)
# butt.pack()

# lb1.grid(row=0,column=1)
# entry.grid(row=1,column=2)
# entry1.grid(row=3,column=4)

# root.mainloop()






from tkinter import *
root = Tk()

root.title("welcome again boos")
root.geometry('250x350')
def func():
    # print("hii")
    var1.get()
    var2.get()
    print(var1.get())
    print(var2.get())
lb1 = Label(root,text="username",bg="white",fg ="blue").place(x=10,y=20)
lb2 = Label(root,text="password",bg="white",fg ="blue").place(x=40,y=30)

butt = Button(root,text="submit",bg="white",fg = "yellow",command=func)
butt.place(x=50,y=70)
var1=StringVar()

entry=Entry(root,width=30).place(x=70,y=110)
var2=StringVar()
entry1=Entry(root,width=30).place(x=60,y=120)

root.mainloop()

