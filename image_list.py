"""
tutorial: https://www.youtube.com/watch?v=zg4c92pNFeo&ab_channel=Codemy.com
"""

from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Image viewer")
    
# open resized-img, attach to label
img1 = ImageTk.PhotoImage(Image.open("resized-img/IMG_6689.JPG"))
img2 = ImageTk.PhotoImage(Image.open("resized-img/IMG_6694.JPG"))
img3 = ImageTk.PhotoImage(Image.open("resized-img/IMG_6721.JPG"))
img4 = ImageTk.PhotoImage(Image.open("resized-img/IMG_6870.JPG"))
img5 = ImageTk.PhotoImage(Image.open("resized-img/IMG_6887.JPG"))

image_list = [img1, img2, img3, img4, img5]

label = Label(image=img1)
label.grid(row=0, column=0, columnspan=3)

def forward(img_no):
    global label
    global forward_button
    global back_button

    # clear screen
    label.grid_forget()

    label = Label(image=image_list[img_no-1])
    label.grid(row=0, column=0, columnspan=3)
    forward_button = Button(root, text=">>", command=lambda: forward(img_no + 1))

    if img_no == 5:
        forward_button = Button(root, text=">>", state=DISABLED)

    back_button = Button(root, text="<<", command=lambda: back(img_no - 1))

    back_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=1)
    forward_button.grid(row=1, column=2)

def back(img_no):
    global label
    global forward_button
    global back_button

    label.grid_forget()

    label = Label(image=image_list[img_no - 1])
    label.grid(row=0, column=0, columnspan=3)
    forward_button = Button(root, text=">>", command=lambda: forward(img_no + 1))
    back_button = Button(root, text="<<", command=lambda: back(img_no - 1))

    if img_no == 1:
        back_button = Button(root, text="<<", state=DISABLED)

    back_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=1)
    forward_button.grid(row=1, column=2)

back_button = Button(root, text="<<", command=back, state=DISABLED)
exit_button = Button(root, text="Exit", command=root.quit)
forward_button = Button(root, text=">>", command=lambda: forward(2))

back_button.grid(row=1, column=0)
exit_button.grid(row=1, column=1)
forward_button.grid(row=1, column=2)

root.mainloop()