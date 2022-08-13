from tkinter import *
from threading import Thread
from time import sleep
from tkinter.filedialog import askopenfilename
from PIL import Image

collid = 0

def AddImage():
    canvas.delete("all")
    file = askopenfilename()
    ResizeImage(file)
    image_tk.config(file="project27/image_300x150.png")
    label_canvas.destroy()
    image_slct = canvas.create_image(60, 60, image=image_tk)
    Thread(target=MoveImage, args=(image_slct,)).start()

def ResizeImage(file):
    image_resize = Image.open(file)
    image_resized = image_resize.resize((150, 150))
    image_resized.save("project27/image_300x150.png")

def MoveImage(image):
    global collid

    direction_x = 3
    direction_y = 3
    while True:
        canvas.move(image, direction_x, direction_y)
        sleep(0.01)
        print(canvas.coords(image))
        if canvas.coords(image)[0] >= 730:
            direction_x = -3
            collid += 1
            label_colid_wall["text"] = collid
        if canvas.coords(image)[1] >= 535:
            direction_y = -3
            collid += 1
            label_colid_wall["text"] = collid
        if canvas.coords(image)[0] <= 70:
            direction_x = 3
            collid += 1
            label_colid_wall["text"] = collid
        if canvas.coords(image)[1] <= 65:
            direction_y = 3
            collid += 1
            label_colid_wall["text"] = collid


def MoveLabel():
    global collid

    x = 0
    y = 0
    direction_x = 3
    direction_y = 3
    while True:
        x += direction_x
        y += direction_y
        label_canvas.place(x=x, y=y)
        sleep(0.0000001)
        print(x, y)
        if label_canvas.winfo_x() >= 670:
            direction_x = -3
            collid += 1
            label_colid_wall["text"] = collid
        if label_canvas.winfo_y() >= 580:
            direction_y = -3
            collid += 1
            label_colid_wall["text"] = collid
        if label_canvas.winfo_x() <= -2:
            direction_x = 3
            collid += 1
            label_colid_wall["text"] = collid
        if label_canvas.winfo_y() <= -2:
            direction_y = 3
            collid += 1
            label_colid_wall["text"] = collid

tk = Tk()
tk.geometry("800x600")
tk.config(background="black")
canvas = Canvas(tk, width=800, height=600, background="black")
canvas.place(x=-2, y=-2)
label_colid_wall = Label(tk, text="0", foreground="white",
                        background="black")
label_colid_wall.config(font=("Courier", 23))
label_colid_wall.pack(anchor=CENTER, expand=1)
image_tk = PhotoImage()
button_image = Button(tk, text="Image", command=AddImage)
button_image.config(font=("Courier", 10))
button_image.place(x=1, y=1)
label_canvas = Label(canvas, text="Hello, World!", foreground="white",
            background="black")
label_canvas.config(font=("Courier", 13))
label_canvas.place(x=0, y=0)
Thread(target=MoveLabel).start()
tk.mainloop()