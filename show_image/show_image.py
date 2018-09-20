#!/usr/bin/env python
import argparse
import sys
import tkinter
from PIL import Image, ImageTk

parser = argparse.ArgumentParser(description='show image')
parser.add_argument('path', metavar='P', type=str, help='image path')
args = parser.parse_args()

path = args.path

print(path)

image = Image.open(path)

root = tkinter.Tk()

root.title(path)
root.geometry('{}x{}'.format(image.size[0], image.size[1]))

photo = ImageTk.PhotoImage(image, master=root)
tkinter.Label(root, image=photo).pack()

root.mainloop()
