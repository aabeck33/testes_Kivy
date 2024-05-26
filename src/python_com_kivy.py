#!/home/abeck/.virtualenvs/k36/bin/python
# -*- coding: utf-8 -*-
#author: Alvaro Adriano Beck
#arquivo: python_com_kivy.py

__version__ = "0.1"

import kivy
kivy.require("1.10.0")
from kivy.app import App
from kivy.lang import Builder

######

from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import NumericProperty
from kivy.properties import ListProperty

######

code = """

BoxLayout:
    orientation: "vertical"

    Button:
        id: bt1
        opacity: 0.2
        text: str(self.opacity)
        color: 1,1,0,1
    Button:
        id: bt2
        text: root.orientation
        color: 1,0,1,1
    Button:
        id: bt3
        text: app.name
        background_color: 0,1,1,1

"""
#Builder.load_file()

class Estudo4App(App):
    def build(self):
        return Builder.load_string(code)


if __name__ == '__main__':
    janela = Estudo4App()
    janela.run()