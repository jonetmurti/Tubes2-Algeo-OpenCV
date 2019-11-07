import os
import cv2
import matcher
from tkinter import filedialog
from tkinter import *  
from PIL import Image, ImageTk, ImageOps



# Declare default
filename = None
labfile = None
label = None
frame0 = None

def openFile():
    # Global Variable
    global filename

    # Open File Path
    filename = filedialog.askopenfilename()
    labfile.config(text=filename)

    # Show Image
    image = Image.open(filename)
    size = (125,125)
    newimage = ImageOps.fit(image, size, Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(newimage)
    label.config(image=photo)
    label.image = photo

def firstPage():
    # Global Variable
    global labfile
    global label
    global var
    global v
    global frame1
    global match_algo

    if(frame0 != None) :
        frame0.destroy()
    frame1 = Frame(root)
    frame1.grid()
    # Label Method
    greet = Label(frame1, text="Choose a method :", font = ('Arial', 10))
    greet.grid(row=0, column=0)

    # Photo
    image = Image.open("view.gif")
    size = (125,125)
    newimage = ImageOps.fit(image, size, Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(newimage)
    label = Label(frame1, image=photo)
    label.image = photo
    label.grid(row=0, column=3, rowspan=4, columnspan=2)

    # RadioButton
    var = IntVar()
    button1 = Radiobutton(frame1, text="Euclidean Distance", variable=var, value=0)
    button1.grid(row=1, column=0, columnspan=1)
    button2 = Radiobutton(frame1, text="Cosine Similarity", variable=var, value=1)
    button2.grid(row=1, column=1, columnspan=1)

    # FileButton
    filebutton = Button(frame1, text="Choose a photo", command=openFile)
    filebutton.grid(row = 2, column = 0, columnspan=2)

    # Entry Text
    labentry = Label(frame1, text="Show Images :")
    labentry.grid(row=3,sticky=E)

    # Entry Number
    v = IntVar()
    entry = Entry(frame1, textvariable=v)
    entry.grid(row=3,column=1)

    # Path
    labfile = Label(frame1, text=filename, borderwidth=2, relief="groove", width=55)
    labfile.grid(row=4, columnspan=4)

    # Show Result
    showbutton = Button(frame1, text="Show Result", command=lambda: MatchProcess(var.get(), filename, "features.dsc", v.get()))
    showbutton.grid(row=5, columnspan=4)


i = 0
def MatchProcess(algo, im_path, data_path, nb) :
    global canvas1
    global names
    global img1
    global match
    global text1
    global frame0

    frame1.destroy()
    if (algo > 1):
        print("Algorithm not available!")
        exit

    ma = matcher.Matcher(data_path)

    names, match = ma.match(im_path, algo, nb)

    if(algo == 1) :
        for cos in range(len(match)) :
            match[cos] = 1 - match[cos]
    
    frame0 = Frame(root)
    frame0.grid()
    back = Button(frame0, text="back", padx=10, pady=10, command=firstPage)
    back.grid(row=0, column=0)

    #frame1 = Frame(root, bg="white")
    #frame1.pack(fill=BOTH, expand=True)
    add = Image.open(im_path)
    add = ImageOps.fit(add, (300, 300), Image.ANTIALIAS)
    pict2 = ImageTk.PhotoImage(add)
    canvas2 = Canvas(frame0, width=350, height=380, bd=2)
    canvas2.grid(row=1, column=0, columnspan=2)
    img2 = canvas2.create_image(30, 20, image=pict2, anchor=NW)
    canvas2.image=pict2
    text2 = canvas2.create_text(150, 350, text=im_path)
    canvas2.text=im_path

    add = Image.open(names[0])
    add = ImageOps.fit(add, (300, 300), Image.ANTIALIAS)
    pict1 = ImageTk.PhotoImage(add)
    canvas1 = Canvas(frame0, width=350, height=380, bd=2)
    canvas1.grid(row=1, column=2, columnspan=2)
    img1 = canvas1.create_image(30, 20, image=pict1, anchor=NW)
    canvas1.image=pict1
    word = "1\n" + names[0] + "\n" + str(match[0])
    text1= canvas1.create_text(150, 350, text=word)
    canvas1.text=word

    #frame2 = Frame(root, bg="white")
    #frame2.pack(fill=X)
    prev = Button(frame0, text="Prev", command=dec)
    prev.grid(row=2, column=1, padx=5, pady=50)
    nex = Button(frame0, text="Next", command=inc)
    nex.grid(row=2, column=2, padx=5, pady=50)

#def show_frame(cont):
#        if (cont == 0) :
#            currframe = frame0
#        elif (cont == 1) :
#            currframe = frame0
#        currframe.tkraise()

def inc() :
    global i
    global T
    if(i < (v.get()-1)) :
        i = i + 1
    add = Image.open(names[i])
    add = ImageOps.fit(add, (300, 300), Image.ANTIALIAS)
    pict1 = ImageTk.PhotoImage(add)
    canvas1.itemconfig(img1, image=pict1)
    canvas1.image=pict1
    x = str(i + 1) + "\n" + names[i] + "\n" + str(match[i])
    canvas1.itemconfig(text1, text=x)
    canvas1.text=x


def dec() :
    global i
    if(i > 0) :
        i = i - 1
    add = Image.open(names[i])
    add = ImageOps.fit(add, (300, 300), Image.ANTIALIAS)
    pict1 = ImageTk.PhotoImage(add)
    canvas1.itemconfig(img1, image=pict1)
    canvas1.image=pict1
    x = str(i + 1) + "\n" + names[i] + "\n" + str(match[i])
    canvas1.itemconfig(text1, text=x)
    canvas1.text=x

root = Tk()
root.title("Face Rocegnition")
firstPage()
root.mainloop()