import urllib, io

from Tkinter import *
from PIL import Image, ImageTk


root = Tk()

fd = urllib.urlopen("http://www.google.com/images/srpr/logo11w.png")
imgFile = io.BytesIO(fd.read())
im = ImageTk.PhotoImage(Image.open(imgFile)) # <-- here
image = Label(root, image = im)
image.grid(row = 7, column = 1)

root.mainloop()