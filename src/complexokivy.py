#enconding: utf-8
#author: Alvaro Adriano Beck

import kivy
kivy.require("1.10.0")
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


def funcSelf(x):
    print("funcSelf")

Button.funcSelf = funcSelf


class MinhaTela(BoxLayout):
    def funcRoot(self):
        print("funcRoot")
        #self.ids.bt1.text = "aaBeck"
        #self.ids.bt2.text = "Teste 2"
        #self.ids.bt3.text = "Teste 3"


class Estudo2App(App):
    def funcApp(self):
        print("funcApp")


janela = Estudo2App()
janela.run()