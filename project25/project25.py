from tkinter import *
from tkinter import ttk
from PIL import ImageGrab

color = "black"
list_colors = ("black", "red", "blue", "yellow", "green", "purple")
first_x, first_y = 0, 0

def Slct_Color(position):
    def Chng_Color(value):
        global color
        
        color = list_colors[list_color.curselection()[0]]
        list_color.destroy()
    
    for widgets in main_root.winfo_children():
        if widgets.widgetName == "listbox":
            list_box = True
            widgets.destroy()
        else:
            list_box = False
    if list_box == False:
        x = position.x
        y = position.y
        strvar = StringVar()
        strvar.set(list_colors)
        list_color = Listbox(main_root, listvariable=strvar, height=6)
        list_color.place(x=x, y=y)
        list_color.bind("<Double-Button-1>", Chng_Color)

    
def First_Cordenates(position):
    global first_x, first_y
    
    first_x, first_y = position.x, position.y

def Drawn(position):
    global first_x, first_y

    x = position.x
    y = position.y
    drawn_canvas.create_line(first_x, first_y, x, y, width=2, fill=color)
    first_x, first_y = x, y

def Save_Art():
    x = root.winfo_rootx()
    y = root.winfo_rooty()
    shot = ImageGrab.grab((x, y, x + 800, y + 600))
    shot.save("Art.png")

root = Tk()
root.title("Drawn Program")
root.geometry("800x600")
note = ttk.Notebook(root)
note.place(x=0,y=4)
button_save = Button(root, text="Save", width=5, command=Save_Art)
button_save.place(x=46, y=2)
main_root = Frame(note, width=800, height=600)
note.add(main_root, text="Drawn")
drawn_canvas = Canvas(main_root, width=800, height=600)
drawn_canvas.place(x=0, y=0)
drawn_canvas.bind("<Button-1>", First_Cordenates)
drawn_canvas.bind("<B1-Motion>", Drawn)
drawn_canvas.bind("<Button-3>", Slct_Color)
main_root.mainloop()
