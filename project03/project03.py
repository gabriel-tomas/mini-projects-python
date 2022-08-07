from posixpath import basename
from threading import Thread
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from pygame import mixer
from tkinter import ttk
import os
from datetime import date

import pygame

playlist = ''
try:
    with open("project03/musics_content/last_playlist.txt",
    'r', encoding='utf-8') as musics_add:
        playlist = musics_add.readline()
except:
    print(f'dont exist: project03/musics_content/last_playlist.txt')
try:
    try:
        with open("project03/musics_content/playlists.txt",
        'r', encoding='utf-8') as exist_playlist:
            exipl = exist_playlist.readlines()
    except:
        with open("project03/musics_content/playlists.txt",
        'w+', encoding='utf-8') as exist_playlist:
            exipl = exist_playlist.readlines()
    print(len(exipl))
    if len(exipl) == 0:
        window_create_playlist = Tk()
        window_create_playlist.geometry('300x100')
        window_create_playlist.config(background='#8c8c8c')
        label_name_playlist = Label(window_create_playlist, text='Name: ',
        background='#8c8c8c')
        label_name_playlist.config(font=('sans', 8))
        label_name_playlist.place(x=4, y=23)
        entry_name_playlist = Entry(window_create_playlist, width=35,
        highlightthickness=0, bd=0)
        entry_name_playlist.place(x=54, y=24)
        def create():
            global playlist

            try:
                name = str(entry_name_playlist.get())
                playlist = name
                if len(name) == 0:
                    name = f"Playlist {date.today()}"
                with open("project03/musics_content/last_playlist.txt",
                'w', encoding='utf-8') as w:
                    w.write(playlist)
            except:
                print('erro')
            with open("project03/musics_content/playlists.txt",
            'a', encoding='utf-8') as new_playlist:
                new_playlist.write(f"project03/playlists/{name}.txt\n")
            with open(f"project03/playlists/{name}.txt",
            'a+', encoding='utf-8') as creat_pllis:
                creat_pllis.read()
            window_create_playlist.destroy()
        def warning_closing():
            messagebox.showwarning("Warning", "Create a playlist")
        button_save = Button(window_create_playlist, text='save',
        highlightthickness=0, bd=0, background='#8c8c8c',
        activebackground='#8c8c8c', command=create)
        button_save.place(x=250, y=70)
        window_create_playlist.protocol('WM_DELETE_WINDOW', warning_closing)
        window_create_playlist.mainloop()
except:
    print('dont exist: playlist.txt')
song_state = 'nothing'
list_all_musics = []
list_queue_musics = []
music_passed = ''
line_vol = 0
state_music = False
started_music = False
quit_app = False
queue_state = False
paused_music = False
print(playlist)

def quit_program():
    global quit_app

    root.destroy()
    quit_app = True

def playlist_musics():
    
    frame_playlist = Frame(root, background='#8c8c8c',
    height=600, width=200, highlightbackground='#4d4d4d',
    highlightthickness=2)
    frame_playlist.place(x=0, y=0)
    button_back = Button(frame_playlist, text='return',
    background='#8c8c8c', activebackground='#8c8c8c',
    highlightthickness=0, bd=0, command=frame_playlist.destroy)
    button_back.place(x=4, y=4)
    list_playlists = Listbox(frame_playlist, background='#8c8c8c',
    highlightthickness=2, bd=0, highlightbackground='#4d4d4d')
    scroll_playlists = Scrollbar(list_playlists, background='#8c8c8c')
    list_playlists.config(yscrollcommand=scroll_playlists.set)
    scroll_playlists.config(command=list_playlists.yview)
    list_playlists.pack(ipadx=100, ipady=257, pady=30)
    scroll_playlists.pack(fill=Y, side=RIGHT)
    def playlist_selected(position):
        global playlist
        
        playlist = list_playlists.get(list_playlists.curselection()[0])
        with open(f"project03/playlists/{playlist}.txt",
        'r', encoding='utf-8') as open_file:
            lines = open_file.readlines()
        list_musics.delete(0, END)
        list_all_musics.clear()
        for i, line in enumerate(lines):
            list_all_musics.append(line.strip())
            list_musics.insert(i, basename(line))
        with open("project03/musics_content/last_playlist.txt",
        'w', encoding='utf-8') as w:
            w.write(playlist)

        frame_playlist.destroy()
        print(playlist)
        print(list_all_musics)
    list_playlists.bind("<Double-Button-1>", playlist_selected)
    
    try:
        with open("project03/musics_content/playlists.txt",
        'r', encoding='utf-8') as playlist:
            lines_playlists = playlist.readlines()
        for i, line_playlist in enumerate(lines_playlists):
            list_playlists.insert(i, basename(line_playlist)[:-5])
    except:
        print('file not exist')
    def remove_playlist():
        remove_play_name = list_playlists.get(list_playlists.curselection()[0])
        try:
            os.remove(f"project03/playlists/{remove_play_name}.txt")
        except:
            print('file not exist')
        with open("project03/musics_content/playlists.txt",
        'r', encoding='utf-8') as remove_play:
            lines = remove_play.readlines()
        if len(lines) <= 1:
            create_playlist()
        with open("project03/musics_content/playlists.txt",
        'w', encoding='utf-8') as remove_play_line:
            for i, line in enumerate(lines):
                if basename(line[:-5]) != remove_play_name:
                    remove_play_line.write(line)
                else:
                    list_playlists.delete(i)

    def create_playlist():
        frame_create_playlist = Frame(root, background='#8c8c8c',
        height=100, width=300, highlightbackground='#4d4d4d',
        highlightthickness=2)
        frame_create_playlist.place(x=220, y=0)
        label_name_playlist = Label(frame_create_playlist, text='Name: ',
        background='#8c8c8c')
        label_name_playlist.config(font=('sans', 8))
        label_name_playlist.place(x=4, y=23)
        entry_name_playlist = Entry(frame_create_playlist, width=35,
        highlightthickness=0, bd=0)
        entry_name_playlist.place(x=54, y=24)
        def create():
            global playlist
            
            try:
                name = str(entry_name_playlist.get())
            except:
                print('erro')
            playlist = name
            list_playlists.insert(END, name)
            with open("project03/musics_content/playlists.txt",
            'a', encoding='utf-8') as new_playlist:
                new_playlist.write(f"project03/playlists/{name}.txt\n")
            with open(f"project03/playlists/{name}.txt",
            'a+', encoding='utf-8') as creat_pllis:
                creat_pllis.read()
            with open("project03/musics_content/last_playlist.txt",
            'w', encoding='utf-8') as w:
                w.write(name)
            list_musics.delete(0, END)
            list_all_musics.clear()
            frame_create_playlist.destroy()
            frame_playlist.destroy()
        button_save = Button(frame_create_playlist, text='save',
        highlightthickness=0, bd=0, background='#8c8c8c',
        activebackground='#8c8c8c', command=create)
        button_save.place(x=250, y=70)
        button_return_create_playlist = Button(frame_create_playlist, text='return',
        highlightthickness=0, bd=0, background='#8c8c8c',
        activebackground='#8c8c8c', command=frame_create_playlist.destroy)
        button_return_create_playlist.place(x=8, y=70)
    button_create_playlist = Button(frame_playlist,
    text='create playlist', background='#8c8c8c',
    activebackground='#8c8c8c', highlightthickness=0,
    bd=0, command=create_playlist)
    button_create_playlist.place(x=140, y=4)
    button_remove_playlist = Button(frame_playlist, text='remove',
    highlightthickness=0, bd=0, background='#8c8c8c',
    activebackground='#8c8c8c', command=remove_playlist)
    button_remove_playlist.place(x=80, y=4)
def volume_music(value):
    value = float(value)/100
    mixer.music.set_volume(value)
    with open("project03/musics_content/last_volume.txt",
    'w', encoding='utf-8') as vol_wri:
        vol_wri.write(str(value))

def add_music():
    global playlist

    print(playlist)
    path = askopenfilename()
    with open(f"project03/playlists/{playlist}.txt",
    'a+', encoding='utf-8') as new_music:
        new_music.write(f"{path.strip()}\n")
    list_musics.insert(END, basename(path))
    list_all_musics.append(path.strip())

def delete_music():
    global playlist

    line_delete_selected_i = list_musics.curselection()[0]
    
    with open(f"project03/playlists/{playlist}.txt",
    'w', encoding='utf-8') as w_musics:
        for i, line_w in enumerate(list_all_musics):
            if i != line_delete_selected_i:
                w_musics.write(f"{line_w.strip()}\n")
            else:
                list_musics.delete(i)
    list_all_musics.pop(line_delete_selected_i)
    print(list_all_musics)

def start_status_music_play():
    Thread(target=status_music_play).start()

def start_automatic_queue():
    Thread(target=automatic_queue).start()

def start_queue():
    Thread(target=queue).start()

def add_queue():
    global queue_state

    queue_state = True
    music_index = list_musics.curselection()[0]
    for i, music in enumerate(list_all_musics):
        if i == music_index:
            list_queue_musics.append(music)
    print(list_queue_musics)

def queue():
    global queue_state

    for music in list_queue_musics:
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()
        while True:
            state = pygame.mixer.music.get_busy()
            print(f'\033[33m{state}\033[m')
            if state == False:
                break
            if quit_app:
                print('\033[31mQuit app queue\033[m')
                break
    queue_state = False
    list_queue_musics.clear()

def automatic_queue():
    global state_music
    global quit_app

    last_music = ''
    music_position = 0
    print('automatic queue ------')
    try:
        music_position = list_musics.curselection()[0]
    except:
        for i, music in enumerate(list_all_musics):
            print(i, music)
            if music == last_music:
                music_position = i
            print(music_position)
    for i, music in enumerate(list_all_musics):
        last_music = music
        print(music)
        if i > music_position:
            pygame.mixer.music.load(music)
            pygame.mixer.music.play()
        while True:
            state = pygame.mixer.music.get_busy()
            if state == False:
                break
            if quit_app:
                print('\033[31mQuit app automatic queue\033[m')
                break
        
def status_music_play():
    global state_music
    global started_music
    global quit_app
    global queue_state
    global paused_music

    while True:
        state = pygame.mixer.music.get_busy()
        print(state)
        if state == False:
            paused_music = False
            state_music = True
            if started_music and queue_state == False:
                started_music = False
                start_automatic_queue()
            break
        if quit_app:
            print('\033[31mQuit app only one music\033[m')
            break

def play_music():
    global song_state
    global music_passed
    global started_music
    global queue_state
    global paused_music
    
    music_load = list_musics.curselection()[0]
    music_load = list_all_musics[music_load]
    
    if song_state == 'nothing' and queue_state == False or music_load != music_passed and queue_state == False:
        print('song nothing')
        music_passed = music_load
        song_state = 'playing'
        button_play.config(image=image_pause)
        mixer.music.load(music_load)
        mixer.music.play()
        started_music = True
        start_status_music_play()

    elif song_state == 'playing':
        song_state = 'paused'
        button_play.config(image=image_play)
        paused_music = True
        mixer.music.pause()

    elif song_state == 'paused':
        song_state = 'playing'
        button_play.config(image=image_pause)
        mixer.music.unpause()
        start_status_music_play()
    
    if queue_state:
        print('Starting queue')
        start_queue()
    print(f'\033[33msong_state = {song_state}\033[m')

mixer.init()
root = Tk()
root.geometry('800x600')
root.config(background='#708090')
root.resizable(0, 0)
frame_list_musics = Frame(root, height=470, width=800)
frame_list_musics.place(x=0, y=0)
image_play = PhotoImage(file=("project03/icons/play.png"))
image_pause = PhotoImage(file=("project03/icons/stop.png"))
button_play = Button(root, image=image_play,
background='#708090', activebackground='#708090',
highlightthickness=0, bd=0, command=play_music)
button_play.place(x=388, y=520)
list_musics = Listbox(frame_list_musics)
scroll_list_musics = Scrollbar(list_musics)
scroll_list_musics.pack(fill=Y, side=RIGHT)
list_musics.pack(ipadx=391, ipady=210)
list_musics.config(highlightthickness=0, bd=0,
background='#8c99a6', yscrollcommand=scroll_list_musics.set)
scroll_list_musics.config(command=list_musics.yview)
try:
    with open(f"project03/playlists/{playlist}.txt",
    'r', encoding='utf-8') as add_recents:
        lines = add_recents.readlines()
    for i, line in enumerate(lines):
        list_musics.insert(i, basename(line))
        list_all_musics.append(line.strip())
except:
    print("archive nothing exist")
try:
    with open("project03/musics_content/last_volume.txt",
    'r', encoding='utf-8') as vol:
        line_vol = vol.readline()
    mixer.music.set_volume(float(line_vol))
except:
    print("archive not exist")
image_add = PhotoImage(file=("project03/icons/add.png"))
button_add_music = Button(root, image=image_add,
background='#708090', activebackground='#708090',
highlightthickness=0, bd=0, command=add_music)
button_add_music.place(x=770, y=480)
style_scale = ttk.Style()
style_scale.configure('TScale', background='#708090')
scale_volume = ttk.Scale(root, from_=0, to=100,
value=float(line_vol)*100,
orient='horizontal', style='TScale',
command=volume_music)
scale_volume.place(x=690, y=560)
image_delete = PhotoImage(file=("project03/icons/delete.png"))
button_delete = Button(root, image=image_delete,
background='#708090', activebackground='#708090',
highlightthickness=0, bd=0, command=delete_music)
button_delete.place(x=770, y=510)
button_playlists = Button(root, text='Playlist',
background='#708090', activebackground='#708090',
highlightthickness=0, bd=0, command=playlist_musics)
button_playlists.place(x=4, y=480)
button_add_queue = Button(root, text='Add queue',
background='#708090', activebackground='#708090',
highlightthickness=0, bd=0, command=add_queue)
button_add_queue.place(x=4, y=505)
root.protocol('WM_DELETE_WINDOW', quit_program)
root.mainloop()
