from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image")
root.iconbitmap("C:/Users/borbe/Pictures/code.ico")

img = ImageTk.PhotoImage(Image.open("C:/Users/borbe/Pictures/code.jpg"))
label = Label(image=img)
label.pack()


button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
