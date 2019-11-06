import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
frame = tk.Frame(root)
root.title("Face Recognition")
root.iconbitmap(r'icon.ico')

def openFile():
    global filename
    filename = filedialog.askopenfilename()
    print(filename)

def firstPage():
    greet = tk.Label(root, text="Face recognition program use euclidean distance and cosine similarity", font = ('Comic Sans MS', 12))
    greet.pack()
    filebutton = tk.Button(frame, text="Choose a photo", command=openFile)
    filebutton.pack()

firstPage()
frame.pack()
root.mainloop()
