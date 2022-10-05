from tkinter import *
from tkinter import ttk
a =Tk()
a.title("mix")
a.geometry("400x300")
a.minsize(width=200,height=150)
a.maxsize(width=900,height=500)
lb1 = Label(a,text="hii",bg="white",fg="blue")
lb1.place(x=0,y=0)
lb2=Label(a,text="hlo",bg="white",fg="yellow")
lb2.place(x=2,y=2)
var1=StringVar()
ent=Entry(a,bg="lightblue",fg="black",textvariable=var1,width=6,bd=6)
ent.place(x=10,y=20)

var2=StringVar()
ent=Entry(a,bg="lightblue",fg="black",textvariable=var1,width=6,bd=6)
ent.place(x=30,y=40)

com=ttk.Combobox(a,width=100,textvariable=var2)
com['values'] = ('january','february','march','april','may','june','july','august',
                 'september','october','november','december')
com.grid(column=1,row=5)
com.current(2)


var3=IntVar()
rad =Radiobutton(a,text="male",value=0,variable=var3).pack()
rad1=Radiobutton(a,text="female",value=0,variable=var3).pack()

rad1=Radiobutton(a,text="radio:1",value=0,variable=var3).pack()
rad1=Radiobutton(a,text="radio:2",value=0,variable=var3).pack()
rad1=Radiobutton(a,text="radio:3",value=0,variable=var3).pack()



a.mainloop()


from tkinter import *
from tkinter import ttk
window=Tk()
window.title("combobox")
var=StringVar()
com=ttk.Combobox(window,width=100,textvariable=var)
com['values'] = (' January', ' February',' March',' April',' May',' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')

com.grid(column=1,row=5)
com.current(2)
window.mainloop()
