from tkinter import *

#Events for button clicks,errors etc..
def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(scvalue.get())
            except (Exception or ZeroDivisionError) as e:
                print(e)
                value = "Error"
            scvalue.set(value)
    elif text == "Clear":
        scvalue.set("")
    
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
menubar = Menu(root)
change = Menu(menubar,tearoff = 0)
change.add_command(label="New")

#Title
root.title("Calculator")
#Default window size
root.geometry("300x400")
root.resizable(0,0)

#icon
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='E:\python\calc\calculator(1).png'))#directory where the icon was present

#input box
scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar = scvalue,font = "Lucida 15 bold",width = 45,borderwidth = 5)
screen.pack(ipadx = 5,ipady = 5,pady = 5,padx = 5)

#buttons
f = Frame(root,bg = "grey")
for j in "789/":
    b = Button(f,text = "{}".format(j),font = "Lucida 25 bold",width = 3)
    b.pack(side = LEFT,padx = 1)
    b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg = "grey")
for j in "456*":
    b = Button(f,text = "{}".format(j),font = "Lucida 25 bold",width = 3)
    b.pack(side = LEFT,padx = 1)
    b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg = "grey")
for j in "123-":
    b = Button(f,text = "{}".format(j),font = "Lucida 25 bold",width = 3)
    b.pack(side = LEFT,padx = 1)
    b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg = "grey")
for j in "0.=+":
    b = Button(f,text = "{}".format(j),font = "Lucida 25 bold",width = 3)
    b.pack(side = LEFT,padx = 1)
    b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg = "grey")
b = Button(f,text = "Clear",font = "Lucida 25 bold",width = 14)
b.pack(side = LEFT,padx = 1)
b.bind("<Button-1>",click)
f.pack()

#finish
root.mainloop()


