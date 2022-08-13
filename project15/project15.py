import subprocess
from tkinter import *
from threading import Thread
from time import sleep as sp
from youtube_dl import YoutubeDL
import os

info = False

def Path():
    user = User_Name()
    os.startfile(f'C:/Users/{user}/Downloads')

def User_Name():
    local = 'C:/Users'
    c = 0
    for dirs, subdirs, archives in os.walk(local):
        if c == 1:
            break
        user = os.path.join(subdirs[1])
        c += 1
    return user

def Info_music():
    infos = YoutubeDL().extract_info(url=link_get.get(),
    download=False)
    txt_info['text'] = infos['title']
    path_downloaded['text'] = f'Path: C:/Users/{User_Name()}/Downloads/{infos["title"]}'
    return infos
    
def Download_Music():
    global info

    link = link_get.get()
    user = User_Name()
    dow_vid = f'youtube-dl {link} --extract-audio --audio-quality 0 --audio-format mp3 -o C:/"Users"/"{user}"/Downloads/%(title)s.%(ext)s'
    CREATE_NO_WINDOW = 0x08000000
    subprocess.call(dow_vid, creationflags=CREATE_NO_WINDOW)
    info = True

def Info_state():
    global info

    while True:
        txt_info_dow['text'] = 'State: Downloading.'
        sp(0.3)
        txt_info_dow['text'] = 'State: Downloading..'
        sp(0.3)
        txt_info_dow['text'] = 'State: Downloading...'
        sp(0.3)
        if info:
            info = False
            txt_info_dow['text'] = 'State: Finish'
            break

def Start_Services():
    Thread(target=Info_music).start()
    Thread(target=Download_Music).start()
    Thread(target=Info_state).start()
 

root = Tk()
root.title('Yt Downloader')
root.geometry('400x200')
root.resizable(0, 0)
link_get = Entry(root, width=30)
link_get.place(x=65, y=80, height=25)
link_get.config(font=(10))
btn = Button(root, text='Download', command=Start_Services)
btn.config(font=('Courier', 10))
btn.place(x=310, y=163)
txt_info_dow = Label(root, text='State: None')
txt_info_dow.config(font=('Courier', 10))
txt_info_dow.place(x=10, y=173)
txt_info = Label(root, text='', wraplength=340)
txt_info.config(font=('Courier', 12))
txt_info.place(x=55, y=20)
btn_path = Button(root, text='Path', command=Path)
btn_path.config(font=('Courier', 10))
btn_path.place(x=260, y=163)
path_downloaded = Label(root, text='Path: ', justify=LEFT, wraplength=280)
path_downloaded.config(font=('Courier', 10))
path_downloaded.place(x=10, y=123)
root.mainloop()
