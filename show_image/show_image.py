import sys
import tkinter
from PIL import Image, ImageTk

argv = sys.argv
path = argv[1]

image = Image.open(path)

root = tkinter.Tk()

root.title(path)
root.geometry('{}x{}'.format(image.size[0], image.size[1]))

photo = ImageTk.PhotoImage(image, master=root)
tkinter.Label(root, image=photo).pack()

root.mainloop()
