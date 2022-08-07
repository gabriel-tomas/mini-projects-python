from ast import arg
from tkinter import *
from threading import Thread
from time import sleep
import gtts
from numpy import int16
from playsound import playsound
from scipy.io.wavfile import read
import os

stop_mouth = False

def Talk():
    global stop_mouth

    text = "9?, 99?, 999?, 9999?, 999999?, 999999?, 999999999999?"
    talk = gtts.gTTS(text, lang="pt")
    talk.save("audio.mp3")
    Thread(target=MoveMout).start()
    playsound("audio.mp3",)
    stop_mouth = True
    
def ToWav(file=""):
    os.system(f"ffmpeg -i {file} audio.wav")

def MoveMout():
    y1 = 280
    y2 = 290
    pos_y1 = -1
    pos_y2 = 1
    c = 0
    data = read("audio.wav")
    audio = data[1]

    while True:
        c += 1
        audio = float(audio)[c]
        print(audio)
        


root = Tk()
root.title("Face")
root.geometry("400x400")
canvas = Canvas(root, width=400, height=400, background="grey")
canvas.pack()
face = canvas.create_oval(23, 23, 380, 380, fill="red")
mouth = canvas.create_oval(110, 260, 290, 310, fill="black", outline="red")
Thread(target=Talk).start()
root.mainloop()
