#coding: utf-8
#author: Alvaro A. Beck

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class RootWidget(FloatLayout):
    pass


class MedidaApp(App):
    def buid(self):
        return RootWidget()


class HelloApp(App):
    pass


#if __name__ == '__main__':
    #HelloApp().run()
MedidaApp().run()