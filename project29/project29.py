from tkinter import *

#size of root window
ROOT_WIDTH = 800
ROOT_HEIGHT = 600

#root window and configurations
root = Tk()
root.title("A")
root.geometry(f"{ROOT_WIDTH}x{ROOT_HEIGHT}")
root.resizable(0, 0)
#widgets and configurations
label_name = Label(root, text="Name:")
label_name.config(font=("sans", 13, "bold"))
entry_name = Entry(root)
entry_name.config(width=28, font=("sans", 13))
label_password = Label(root, text="Password:")
label_password.config(font=("sans", 13, "bold"))
entry_password = Entry(root)
entry_password.config(width=28, font=("sans", 13))
button_send = Button(root, text="Send")
button_send.config(font=("sans", 12, "bold"))
#position of widgets
label_name.place(x=270, y=200)
entry_name.place(x=270, y=230)
label_password.place(x=270, y=260)
entry_password.place(x=270, y=290)
button_send.place(x=470, y=320)
root.mainloop()
