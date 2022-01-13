from tkinter import *
from PIL import ImageTk, Image
import os
from itertools import cycle

root = Tk()
root.title("Slideshow1")
    
images = [file for file in os.listdir("resized-img") if file.endswith(('JPG'))]
open_img = cycle(ImageTk.PhotoImage(Image.open("resized-img/"+img)) for img in images)

label = Label(root)
label.grid(row=0, column=0, columnspan=3)
        
def forward():
    img = next(open_img)
    label.configure(image=img)
    label.image = img
    label.after(3000, forward)

forward()

exit_button = Button(root, text="Exit", command=root.quit)
exit_button.grid(row=1, column=1)

root.mainloop()