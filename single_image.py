from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image viewer")
root.geometry("800x500")

# Open img
img = Image.open("img/IMG_6870.JPG")

# Resize img

"""
print(img)  
<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=768x1024 at 0x10DF1D450>
"""

def resize_img(img, new_width):
    width, height = img.size
    ration = height / width
    new_height = int(ration * new_width)
    resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)
    return resized_img

resized = resize_img(img, 300)
new_img = ImageTk.PhotoImage(resized)

label = Label(root, image=new_img)
label.pack(pady=20)

exit_button = Button(root, text="Exit", command=root.quit)
exit_button.pack()

root.mainloop()