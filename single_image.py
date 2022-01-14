from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font

root = Tk()
root.title("Single image")
root.geometry("800x500")

# Open img
img = Image.open("img/IMG_6694.JPG")

# Resize img
def resize_img(img, new_width):
    width, height = img.size
    ratio = height / width
    new_height = int(ratio * new_width)
    resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)
    return resized_img

resized = resize_img(img, 300)
new_img = ImageTk.PhotoImage(resized)

label = Label(root, image=new_img)
label.pack(pady=20)

# Button
button_font = font.Font(family="Helvetica", size=20, weight="bold")
exit_button = Button(root, text="Exit", fg="#7580eb", command=root.quit)
exit_button["font"] = button_font
exit_button.pack()

root.mainloop()