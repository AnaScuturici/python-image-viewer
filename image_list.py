from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Image viewer")

label = Label(root)
label.pack(pady=20)

# function to resize photo
def resize_img(img, new_width):
    width, height = img.size
    ratio = height / width
    new_height = int(ratio * new_width)
    resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)
    return resized_img

# resize all photos in img folder, save in resized-img folder
images = [file for file in os.listdir("img") if file.endswith(('JPG'))]
for image in images:
    img = Image.open("img/"+image)
    im_resized = resize_img(img, 300)
    image_path = f"resized-img/{image}"
    im_resized.save(image_path)
    
# open resized-img, attach to label
resized_images = [file for file in os.listdir("resized-img") if file.endswith(('JPG'))]
resized_images = iter(resized_images)

def forward():
    try:
        img = next(resized_images)
    except StopIteration:
        return

    img = Image.open(img)
    img = ImageTk.PhotoImage(img)
    label.img = img
    label["image"] = img

forward()

def back():
    return


#back_button = Button(root, text="<<", padx=20, pady=20, command=lambda: back())
#exit_button = Button(root, text="Exit", padx=20, pady=20, command=root.quit)
forward_button = Button(root, text=">>", padx=20, pady=20, command=lambda: forward())

#back_button.grid(row=1, column=0)
#exit_button.grid(row=1, column=1)
forward_button.grid(row=1, column=2)

root.mainloop()