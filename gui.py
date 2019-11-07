import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps

root = tk.Tk()
# Title
root.title("Face Recognition")

# Icon
root.iconbitmap(r'icon.ico')

# Declare default
filename = None
labfile = None
label = None

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

    # Label Method
    greet = tk.Label(root, text="Choose a method :", font = ('Arial', 10))
    greet.grid(row=0, column=0)

    # Photo
    image = Image.open("view.gif")
    size = (125,125)
    newimage = ImageOps.fit(image, size, Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(newimage)
    label = tk.Label(root, image=photo)
    label.image = photo
    label.grid(row=0, column=3, rowspan=4, columnspan=2)

    # RadioButton
    var = tk.IntVar()
    button1 = tk.Radiobutton(root, text="Euclidean Distance", variable=var, value=0)
    button1.grid(row=1, column=0, columnspan=1)
    button2 = tk.Radiobutton(root, text="Cosine Similarity", variable=var, value=1)
    button2.grid(row=1, column=1, columnspan=1)

    # FileButton
    filebutton = tk.Button(root, text="Choose a photo", command=openFile)
    filebutton.grid(row = 2, column = 0, columnspan=2)

    # Entry Text
    labentry = tk.Label(root, text="Show Images :")
    labentry.grid(row=3,sticky=tk.E)

    # Entry Number
    v = tk.IntVar()
    entry = tk.Entry(root, textvariable=v)
    entry.grid(row=3,column=1)

    # Path
    labfile = tk.Label(root, text=filename, borderwidth=2, relief="groove", width=55)
    labfile.grid(row=4, columnspan=4)

    # Show Result
    showbutton = tk.Button(root, text="Show Result", command=None)
    showbutton.grid(row=5, columnspan=4)


firstPage()
root.mainloop()
