from sre_constants import IN
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.filechooser import FileChooser
from pygame.mixer import music
import pygame

pygame.init()
local = 'project14/window.kv'
Interface = Builder.load_file(local)
run_music = False
state_music = 'None'

def play_music(instace):
        global run_music
        global state_music
        
        if state_music == 'None':
            music.load("C:/Users/Biel/Music/MV 화사(Hwa Sa) - 덤덤해지네_160k.mp3")
            pygame.mixer.music.play()
            state_music = 'Playing'

        elif state_music == 'Paused':
            print('musica rodando...')
            pygame.mixer.music.unpause()
            state_music = 'Playing'

        elif state_music == 'Playing':
            pygame.mixer.music.pause()
            state_music = 'Paused'
        


        print(state_music)

        instace.text = state_music
        if run_music == False:
            run_music = True
            Interface.add_widget(Label(text='MV 화사(Hwa Sa)'))


class MyApp(App):
    pop = ObjectProperty(None)

    def build(self):
        return Interface
  
    def on_start(self):
        button = self.root.ids['play_music']
        button.bind(on_press=play_music)
        return super().on_start()

        


        
MyApp().run()