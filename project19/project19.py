from os import system
from tkinter import *
import os


def findURLFile():
    dirs = os.walk("project19/")
    for dir in dirs:
        for files in dir:
            for file in files:
                if "URL" in file:
                    print(f"Arquivo .URL encontrado: {file}")
                    return file

def runURLFile(file):
    system(f"cd project19 && {file}")

file = findURLFile()
runURLFile(file)

