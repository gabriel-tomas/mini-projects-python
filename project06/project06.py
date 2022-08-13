from re import M
from tkinter import *
from threading import Thread
from time import sleep

c_time = 0

def time_start():
    Thread(target=time).start()

def time():
    global c_time

    s = 0
    m = 0
    h = 0
    while True:
        label_time['text'] = f'{h:0>2}:{m:0>2}:{s:0>2}'
        s += 1
        if c_time * 60 <= s:
            print('asdasd')
            break
        if s == 60:
            s = 0
            m += 1
        if m == 60:
            m = 0
            h += 1
        if h == 24:
            h = 0
        sleep(1)
        
def custom_time():
    global c_time

    c_time = float(entry_custom_time.get())

window = Tk()
window.geometry('300x170')
label_time = Label(window, text='00:00:00')
label_time.place(x=70, y=45)
label_time.config(font=('Courier',26))
entry_custom_time = Entry(window, width=12)
entry_custom_time.place(x=200, y=105)
button_set_custom_time = Button(window,
text='start cus. tim.', command=custom_time)
button_set_custom_time.place(x=200, y=130)
button_start = Button(window,
text='Start',width=8, height=2,
command = time_start)
button_start.place(x=125, y=105)
window.mainloop()
