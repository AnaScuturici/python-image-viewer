from tkinter import *
from PIL import Image
import os

root = Tk()

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