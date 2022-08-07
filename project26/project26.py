from tkinter import *
from time import sleep
from threading import Thread

widget_animation_enter = False
widget_animation_leave = False

def WidgetPointEnter():
    global widget_animation_enter

    w = frame_text.winfo_width()
    for c in range(1, 15):
        w += 12
        sleep(0.0001)
        frame_text.config(width=w)
        
    widget_animation_enter = False

def WidgetPointLeave():
    global widget_animation_leave

    w = 468
    for c in range(1, 15):
        w -= 12
        sleep(0.0001)
        frame_text.config(width=w)
    widget_animation_leave = False

def StaEnter(pos):
    global widget_animation_enter
    
    if widget_animation_leave == False:
        Thread(target=WidgetPointEnter).start()
        widget_animation_enter = True

def StaLeave(pos):
    global widget_animation_leave

    if widget_animation_leave == False:
        Thread(target=WidgetPointLeave).start()
        widget_animation_leave = True

main_window = Tk()
main_window.geometry("800x600")
frame_text = Frame(main_window, width=300, height=600, background="yellow")
frame_text.place(x=0, y=0)
frame_text.bind("<Leave>", StaLeave)
frame_text.bind("<Enter>", StaEnter)
main_window.mainloop()