#enconding: utf-8
#author: Alvaro Adriano Beck

import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Tela1(BoxLayout):
    def on_press_bt(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Tela2())


class Tela2(BoxLayout):
    def on_press_bt(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Tela1())


class KVvsPY2App(App):
    pass
    #def build(self):
    #    return Tela1()


janela = KVvsPY2App()
janela.run()
