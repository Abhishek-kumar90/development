from tkinter import Tk,Menu

root=Tk()

menu_bar = Menu(root)

filemenu = Menu(menu_bar, tearoff=0)

filemenu.add_command(label="fill",command=root.destroy)
filemenu.add_command(label="kill",command=root.destroy)
filemenu.add_command(label="mill",command=root.destroy)

menu_bar.add_cascade(label="file",menu=filemenu)

root.configure(menu=menu_bar)
root.mainloop()




from tkinter import Tk,Menu
root = Tk()

menu_bar = Menu(root)

filemenu = Menu(menu_bar,tearoff=0)


filemenu.add_command(label="stop",command=root.destroy)
filemenu.add_command(label="exit",command=root.destroy)
filemenu.add_command(label="kill",command=root.destroy)

menu_bar.add_cascade(label="file",menu=filemenu)

root.configure(menu=menu_bar)
root.mainloop()
