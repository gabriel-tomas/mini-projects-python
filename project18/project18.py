from ast import While
from threading import Thread
from tkinter import *
from os import walk
from os import remove
from os.path import join
from tkinter.filedialog import askopenfilename
from pygame.mixer import music
from pygame.mixer import init as mixer_init
from posixpath import basename
from tkinter import ttk


FONT_MAIN = 'Courier'
PATH_ICONS = 'project18/icons/'
PATH_PLAYLISTS = 'project18/Play Lists/'
BACKGROUND = '#396060'
BACKGROUND_LIST_BOX = '#4d8080'
X_ROOT = 900
Y_ROOT = 610
state_music = 'None'
lastSong = ''
listAllMusics = []
listAllPlaylists = []


def AddMusic():
    global Playlist

    music = askopenfilename().strip()
    listBoxMusic.insert(END, basename(music))
    listAllMusics.append(music)
    with open(Playlist, 'a+', encoding='utf-8') as addMusic:
        addMusic.write(f"{music}\n")


def LastPlaylist():
    global Playlist

    try:
        with open('project18/LastPlaylist.txt', 'r',
                encoding='utf-8') as lastPlaylist:
                Playlist = lastPlaylist.read()
    except:
        print('Não existe')


def LastPlaylistSelected():
    with open('project18/LastPlaylist.txt', 'w+',
                encoding='utf-8') as lastPlaylist:
                lastPlaylist.write(Playlist)


mixer_init()


def PauseSong():
    music.pause()


def PlaySong():
    global song

    music.load(song)
    music.play()


def UnpauseSong():
    music.unpause()



def PlayPauseSong_DoubleButton(pos):
    global song
    global state_music
    global lastSong

    song = listAllMusics[listBoxMusic.curselection()[0]]
    print(f'Musica tocando: {song}')

    if state_music == 'None' or lastSong != song:
        PlaySong()
        state_music = 'playing'
        playBtn.config(image=image_PauseBtn)

    elif state_music == 'playing':
        PauseSong()
        state_music = 'paused'
        playBtn.config(image=image_playBtn)

    elif state_music == 'paused':
        UnpauseSong()
        state_music = 'playing'
        playBtn.config(image=image_PauseBtn)

    lastSong = song

    StartAutomaticMusic()
    
def PlayPauseSong_Button():
    global song
    global state_music
    global lastSong

    song = listAllMusics[listBoxMusic.curselection()[0]]
    print(f'Musica tocando: {song}')

    if state_music == 'None' or song != lastSong:
        PlaySong()
        state_music = 'playing'
        playBtn.config(image=image_PauseBtn)

    elif state_music == 'playing':
        PauseSong()
        state_music = 'paused'
        playBtn.config(image=image_playBtn)

    elif state_music == 'paused':
        UnpauseSong()
        state_music = 'playing'
        playBtn.config(image=image_PauseBtn)

    lastSong = song



def NewPlaylist():
    BACKGROUND_NEWPLAYLIST = '#264040'

    
    def addNewPlaylist():
        global Playlist
        
        namePlaylist = entryNamePlaylist.get()
        Playlist = f"{PATH_PLAYLISTS}{namePlaylist}.txt"
        listboxPlaylist.insert(END, namePlaylist)
        listAllPlaylists.append(f"{namePlaylist.strip()}.txt")
        with open(f"{PATH_PLAYLISTS}{namePlaylist}.txt", 'w+',
                encoding="utf-8") as create_playlist:
            create_playlist.seek(0, 0)
        LastPlaylistSelected()
        LoadMusics()
        windowNewPlaylist.destroy()


    windowNewPlaylist = Frame(ROOT, width=400, height=200,
                            background=BACKGROUND_NEWPLAYLIST,
                            highlightthickness=2,
                            highlightbackground='#0a1010')
    windowNewPlaylist.place(x=270, y=200)

    
    createNewPlaylist = Button(windowNewPlaylist, image=image_createNewPlaylist,
                        background=BACKGROUND_NEWPLAYLIST,
                        activebackground=BACKGROUND_NEWPLAYLIST,
                        highlightthickness=0, bd=0,
                        command=addNewPlaylist)
    createNewPlaylist.place(x=360, y=165)


    labelNamePlaylist = Label(windowNewPlaylist, text="Name:",
                            background=BACKGROUND_NEWPLAYLIST)
    labelNamePlaylist.config(font=("sans", 11))
    labelNamePlaylist.place(x=180, y=60)


    entryNamePlaylist = Entry(windowNewPlaylist, highlightthickness=0, bd=0,
                            background='#396060', width=30, relief='solid')
    entryNamePlaylist.place(x=100, y=90, height=18)
    entryNamePlaylist.config(font=(FONT_MAIN, 9))
    
    returnButton = Button(windowNewPlaylist, image=image_returnButton,
                        highlightthickness=0, bd=0,
                        background=BACKGROUND_NEWPLAYLIST,
                        activebackground=BACKGROUND_NEWPLAYLIST,
                        command=windowNewPlaylist.destroy)
    returnButton.place(x=10, y=162)


def PlaylistSelected(pos):
    global Playlist

    selected = listboxPlaylist.get(listboxPlaylist.curselection()[0])
    Playlist = f"{PATH_PLAYLISTS}{selected}.txt"
    LastPlaylistSelected()
    LoadMusics()


def LoadPlaylists():
    try:
        listAllPlaylists.clear()
        listboxPlaylist.delete(0, END)
        path_playlist = walk(PATH_PLAYLISTS)
        for files_paths in path_playlist:
            for files in files_paths:
                if type(files) is list:
                    for file in files:
                        listboxPlaylist.insert(END,
                        basename(file).replace('.txt', ''))
                        listAllPlaylists.append(file)
    except:
        print('Não existe')


def LoadMusics():
    global Playlist
    
    try:
        listAllMusics.clear()
        listBoxMusic.delete(0, END)
        with open(Playlist, 'r+', encoding='utf-8') as load:
            songs = load.readlines()
        for song in songs:
            listAllMusics.append(song.strip())
            listBoxMusic.insert(END, basename(song.strip()))
        print(listAllMusics)
    except:
        print('Não existe')



def SetVolum(value):
    music.set_volume(float(value))
    with open('project18/LastVolum.txt', 'w+',
            encoding='utf-8') as volum_write:
            volum_write.write(value)


def LastVolum():
    try:
        with open('project18/LastVolum.txt', 'r',
                encoding='utf-8') as LastVol:
                lastVol = LastVol.read()
        lastVol = float(lastVol)
        return lastVol

    except:
        print('Não existe')
        lastVol = 0
        return lastVol


def LastVolPygameMusic():
    lastVolu = LastVolum()
    music.set_volume(lastVolu)


def Volum():
    lastVolu = LastVolum()
    styleScale = ttk.Style()
    styleScale.configure('TScale', background=BACKGROUND)
    scale_volum = ttk.Scale(ROOT, orient='horizontal', from_=0,
                            to=1,style='TScale', value=lastVolu,
                            command=SetVolum)
    scale_volum.place(x=760, y=580)

    def DestroyBtns():
        scale_volum.destroy()
        exitBtn.destroy()

    exitBtn = Button(ROOT, image=image_volBtn, background=BACKGROUND,
                activebackground=BACKGROUND, highlightthickness=0,
                bd=0, command=DestroyBtns)
    exitBtn.place(x=870, y=580)


def DeleteMusic():
    global Playlist

    with open(Playlist, 'r+', encoding='utf-8') as lines:
        musics = lines.readlines()

    song_to_delete = listAllMusics[listBoxMusic.curselection()[0]]

    with open(Playlist, 'w+', encoding='utf-8') as lines:
        lines.truncate(0)

    with open(Playlist, 'a+', encoding='utf-8') as write_musics:
        for music in musics:
            if music.strip() != song_to_delete.strip():
                write_musics.write(f'{music.strip()}\n')
                
    LoadMusics()

    
def DeletePlaylist():
    file = join(PATH_PLAYLISTS, listAllPlaylists[listboxPlaylist.curselection()[0]])
    remove(file)

    LoadPlaylists()


def AutomaticQueue():
    for i, song in enumerate(listAllMusics):
        if i > listBoxMusic.curselection()[0]:
            print(song)
            music.load(song)
            music.play()
            GetStateAutomaticQueue()           

def GetStateAutomaticMusic():
    global state_music

    while True:
        if state_music == "playing":
            busy = music.get_busy()
            if not busy:
                state_music = "None"
                AutomaticQueue()
                break
        
def StartAutomaticMusic():
    Thread(target=GetStateAutomaticMusic).start()

def GetStateAutomaticQueue():
    global state_music

    while True:
        if state_music == "None":
            busy = music.get_busy()
            if not busy:
                break





ROOT = Tk()
ROOT.geometry(f'{X_ROOT}x{Y_ROOT}')
ROOT.resizable(0, 0)
ROOT.config(background=BACKGROUND)
ROOT.title('Player')


line_division = Frame(ROOT, height=1, width=200)
line_division.place(x=700, y=490)


image_playBtn = PhotoImage(file=(f'{PATH_ICONS}Play.png'))
image_PauseBtn = PhotoImage(file=(f'{PATH_ICONS}Pause.png'))
playBtn = Button(ROOT, image=image_playBtn, background=BACKGROUND,
                activebackground=BACKGROUND, highlightthickness=0,
                bd=0, command=PlayPauseSong_Button)
playBtn.place(x=790, y=540)


image_addMusic = PhotoImage(file=(f'{PATH_ICONS}Add.png'))
addMusicBtn = Button(ROOT, image=image_addMusic,
                    background=BACKGROUND, activebackground=BACKGROUND,
                    highlightthickness=0, bd=0, command=AddMusic)
addMusicBtn.place(x=870, y=500)


image_NewPlaylist = PhotoImage(file=(f'{PATH_ICONS}NewPlaylist.png'))
NewPlaylistBtn = Button(ROOT, image=image_NewPlaylist,
                    background=BACKGROUND, activebackground=BACKGROUND,
                    highlightthickness=0, bd=0, command=NewPlaylist)
NewPlaylistBtn.place(x=870, y=4)


listboxPlaylist = Listbox(ROOT, background=BACKGROUND,
                highlightthickness=0, bd=0)
listboxPlaylist.pack(side=RIGHT, ipadx=91, ipady=204, anchor=N, pady=30)
scroll_listBox = Scrollbar(listboxPlaylist)
scroll_listBox.pack(side=RIGHT, fill=Y)
listboxPlaylist.config(font=(FONT_MAIN, 11),
                        yscrollcommand=scroll_listBox.set)
scroll_listBox.config(command=listboxPlaylist.yview)
listboxPlaylist.bind("<Double-Button-1>", PlaylistSelected)


listBoxMusic = Listbox(ROOT, background=BACKGROUND_LIST_BOX,
                        highlightthickness=0, bd=1)
listBoxMusic.pack(side=LEFT, fill=Y, ipadx=340)
scroll_listBox = Scrollbar(listBoxMusic)
scroll_listBox.pack(side=RIGHT, fill=Y)
listBoxMusic.config(font=('Courier', 11), 
                    yscrollcommand=scroll_listBox.set)
scroll_listBox.config(command=listBoxMusic.yview)
listBoxMusic.bind("<Double-Button-1>", PlayPauseSong_DoubleButton)


image_volBtn = PhotoImage(file=(f'{PATH_ICONS}Volum.png'))
volBtn = Button(ROOT, image=image_volBtn, background=BACKGROUND,
                activebackground=BACKGROUND, highlightthickness=0,
                bd=0, command=Volum)
volBtn.place(x=870, y=580)


image_deleteMusicBtn = PhotoImage(file=(f'{PATH_ICONS}Delete.png'))
deleteMusicBtn = Button(ROOT, image=image_deleteMusicBtn, background=BACKGROUND,
                activebackground=BACKGROUND, highlightthickness=0,
                bd=0, command=DeleteMusic)
deleteMusicBtn.place(x=703, y=500)


image_deletePlaylistBtn = PhotoImage(file=(f'{PATH_ICONS}DeletePlaylist.png'))
deletePlaylistBtn = Button(ROOT, image=image_deletePlaylistBtn, background=BACKGROUND,
                    activebackground=BACKGROUND, highlightthickness=0,
                    bd=0, command=DeletePlaylist)
deletePlaylistBtn.place(x=703, y=4)


image_createNewPlaylist = PhotoImage(file=(f'{PATH_ICONS}createNewPlaylist.png'))
image_returnButton = PhotoImage(file=(f'{PATH_ICONS}Return.png'))


LastPlaylist()
LoadPlaylists()
LoadMusics()
LastVolPygameMusic()

ROOT.mainloop()
