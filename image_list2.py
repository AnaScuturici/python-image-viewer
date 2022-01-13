from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Image viewer")
    
resized_images = iter([file for file in os.listdir("resized-img") if file.endswith(('JPG'))])

label = Label(root)
label.grid(row=0, column=0, columnspan=3)
        
def forward():
    try:
        img = next(resized_images)
    except StopIteration:
        forward_button["state"]=DISABLED
        back_button["state"]=NORMAL
        return

    img = ImageTk.PhotoImage(Image.open("resized-img/"+img))
    label.configure(image=img)
    label.image = img

# doesn't work 
def back():
    try:
        img = next(resized_images)
    except StopIteration:
        back_button["state"]=DISABLED
        forward_button["state"]=NORMAL
        return

    img = ImageTk.PhotoImage(Image.open("resized-img/"+img))
    label.configure(image=img)
    label.image = img

forward()

back_button = Button(root, text="<<", command=back, state=DISABLED)
exit_button = Button(root, text="Exit", command=root.quit)
forward_button = Button(root, text=">>", command=lambda: forward())

back_button.grid(row=1, column=0)
exit_button.grid(row=1, column=1)
forward_button.grid(row=1, column=2)


root.mainloop()