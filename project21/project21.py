from posixpath import basename
from tkinter import *
from pygame.mixer import music
from pygame import mixer
from tkinter.filedialog import askopenfilename

class Play_one_music:
    def __init__(self, root):
        self.window = root
        self.window.title("Player Music with POO")
        self.window.resizable(0, 0)
        self.window.geometry("300x400")
        self.button = Button(self.window, text="Play", command=self.Play_music)
        self.button.place(x=45, y=260)
        self.button.config(height=3, width=15, background="black",
                            foreground="white", font=("sans", 18),
                            activebackground="black", activeforeground="white")
        self.button_slct_file = Button(self.window, text="Select file",
                                        command=self.Select_file)
        self.button_slct_file.place(x=45, y=150)
        self.button_slct_file.config(height=3, width=15, background="black",
                                    foreground="white", font=("sans", 18),
                                    activebackground="black", activeforeground="white")
        self.name_music = Label(self.window, text="...",
                                wraplength=280, justify=CENTER)
        self.name_music.place(x=25, y=2)
        self.name_music.config(font=("sans", 23))
    def Run(self):
        mixer.init()
        music.set_volume(0.12)
        self.window.mainloop()
    def Select_file(self):
        self.music = askopenfilename()
    def Play_music(self):
        music.load(self.music)
        music.play()
        self.Name_music()
    def Name_music(self):
        music = self.music
        if len(music) >= 10:
            music = self.music[0:50] + "..."
        self.name_music["text"] = basename(music.replace(".mp3", ""))
        

Play_one_music(Tk()).Run()
        