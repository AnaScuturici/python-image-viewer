from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Image viewer")
    
images = [file for file in os.listdir("resized-img") if file.endswith(('JPG'))]

label = Label(root)
label.grid(row=0, column=0, columnspan=3)

# create an iterable list
class cycle:
    def __init__(self, c):
        self._c = c
        self._index = -1

    def __next__(self):
        self._index += 1
        if self._index>=len(self._c):
            self._index = 0
        return self._c[self._index]

    def previous(self):
        self._index -= 1
        if self._index < 0:
            self._index = len(self._c)-1
        return self._c[self._index]
        
images = cycle(images)

def forward():
    img = next(images)
    img = ImageTk.PhotoImage(Image.open("resized-img/"+img))
    label.configure(image=img)
    label.image = img
        
def back():
    img = images.previous()
    img = ImageTk.PhotoImage(Image.open("resized-img/"+img))
    label.configure(image=img)
    label.image = img

forward()

back_button = Button(root, text="<<", command=lambda: back())
exit_button = Button(root, text="Exit", command=root.quit)
forward_button = Button(root, text=">>", command=lambda: forward())

back_button.grid(row=1, column=0)
exit_button.grid(row=1, column=1)
forward_button.grid(row=1, column=2)

root.mainloop()