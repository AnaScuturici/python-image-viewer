from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image viewer")
root.geometry("800x500")

# Open img
img = Image.open("img/IMG_6870.JPG")

# Resize img
resized = img.resize((350, 400), Image.ANTIALIAS)

resized_img = ImageTk.PhotoImage(resized)

# Img size
label = Label(root, image=resized_img)
label.pack(pady=20)

exit_button = Button(root, text="Exit", command=root.quit)
exit_button.pack()

root.mainloop()