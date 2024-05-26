#!/home/abeck/.virtualenvs/k36/bin/python
# -*- coding: utf-8 -*-
#author: Alvaro Adriano Beck
#notebook: boilerplate

__version__ = "0.1"

#kivy.require("1.10.0")
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.config import Config

from kivy.core.window import Window
from kivy.utils import get_color_from_hex

######
#from kivy.uix.image import Image
#from kivy.uix.widget import Widget
#from kivy.properties import ObjectProperty
#from kivy.uix.boxlayout import BoxLayout
#from kivy.core.window import Window
#from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
#from kivy.properties import NumericProperty
#from kivy.properties import ListProperty
from kivy.interactive import InteractiveLauncher
######

#força a aplicação a não iniciar em tela cheia
Config.set("graphics","fullscreen","0")

janela = None
glayout = None
Window.clearcolor = [1,.7,1,1]
#Window.clearcolor = get_color_from_hex("#FF01FF")



class JanelaApp(App):
    def build(self):
        return Builder.load_string( kvcode )


kvcode = """

#:import C kivy.utils.get_color_from_hex

<FVerde@FloatLayout>:
    size_hint: .3,.3
    canvas.before:
        Color:
            rgba: 0,1,0,1
            #rgba: C("FF01FF")
        Rectangle:
            pos: self.pos
            size: self.size

FloatLayout:
    FVerde:
        pos_hint: {"x":.4,"y":.4}

"""


janela = JanelaApp()
janela.run()



