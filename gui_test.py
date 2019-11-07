from tkinter import *  
from PIL import Image, ImageTk

var = 1
def inc() :
    global var
    var = var + 1
    add = Image.open("images/"+ str(var) + ".jpg")
    pict1 = ImageTk.PhotoImage(add)
    img1.configure(image=pict1)
    img1.image = pict1
    print(var)


def dec() :
    global var
    var = var - 1
    add = Image.open("images/"+ str(var) + ".jpg")
    pict1 = ImageTk.PhotoImage(add)
    img1.configure(image=pict1)
    img1.image = pict1
    print(var)

root = Tk()

root.geometry("800x600")

frame0 = Frame(root, bg="white")
frame0.pack(fill=BOTH)
back = Button(frame0, text="back", padx=10, pady=10)
back.pack(side=LEFT, padx=20, pady=10)

frame1 = Frame(root, bg="white")
frame1.pack(fill=BOTH, expand=True)
add = Image.open("images/1.jpg")
pict1 = ImageTk.PhotoImage(add)
img1 = Label(frame1, image=pict1)
img1.pack(side=LEFT, padx=50)
add = Image.open("images/1.jpg")
pict2 = ImageTk.PhotoImage(add)
img2 = Label(frame1, image=pict2)
img2.pack(side=RIGHT, padx=50)

frame2 = Frame(root, bg="white")
frame2.pack(fill=BOTH)
prev = Button(frame2, text="Prev", command=dec)
prev.pack(pady=50)
nex = Button(frame2, text="Next", command=inc)
nex.pack(pady=50)

root.mainloop()