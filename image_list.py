from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Image viewer")

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
# resized_images = [file for file in os.listdir("resized-img") if file.endswith(('JPG'))]

img1 = ImageTk.PhotoImage(Image.open("resized-img/IMG_6689.JPG"))
img2 = ImageTk.PhotoImage(Image.open("resized-img/IMG_6694.JPG"))
img3 = ImageTk.PhotoImage(Image.open("resized-img/IMG_6721.JPG"))
img4 = ImageTk.PhotoImage(Image.open("resized-img/IMG_6870.JPG"))
img5 = ImageTk.PhotoImage(Image.open("resized-img/IMG_6887.JPG"))

image_list = [img1, img2, img3, img4, img5]

label = Label(root, image=img1)
label.grid(row=0, column=0, columnspan=3)

def forward(img_num):
    global label
    global forward_button
    global back_button

    #delete the currently displayed photo
    label.grid_forget()
    # recreate all widgets
    label = Label(image=image_list[img_num - 1])
    forward_button = Button(root, text=">>", command=lambda: forward_button(img_num + 1))
    back_button = Button(root, text="<<", command=lambda: back_button(img_num - 1))
    
    # stop after last photo
    if img_num == 5:
        forward_button = Button(root, text=">>", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    forward_button.grid(row=1, column=2)


def back(img_num):
    global label
    global forward_button
    global back_button

    label.grid_forget()

    label = Label(image=image_list[img_num + 1])
    forward_button = Button(root, text=">>", command=lambda: forward_button(img_num + 1))
    back_button = Button(root, text="<<", command=lambda: back_button(img_num - 1))

    if img_num == 1:
        back_button = Button(root, text="<<", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    forward_button.grid(row=1, column=2)


back_button = Button(root, text="<<", command=lambda: back(3))
exit_button = Button(root, text="Exit", command=root.quit)
forward_button = Button(root, text=">>", command=lambda: forward(2))

back_button.grid(row=1, column=0)
exit_button.grid(row=1, column=1)
forward_button.grid(row=1, column=2)

root.mainloop()