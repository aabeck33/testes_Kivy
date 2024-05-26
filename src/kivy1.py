#coding: utf-8
#author: Alvaro A. Beck

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window


class MinhaJanela(App):
    def _click():
        print("Texto da janela de texto:\n", ti.text)

    def _build(self):
        # Label
        lb = Label()
        lb.text = "Curso de Python e Kyvi"
        lb.italic = True
        lb.font_size = 24
        lb.color = 1, 0, 1, 0
        lb.size_hint = None, None
        lb.height = 30
        lb.width = 250
        lb.x = 70
        lb.y = 450
        # Button
        bt = Button()
        bt.text = "Clique aqui"
        bt.on_press = MinhaJanela._click
        bt.color = 1, 0, 0, 0
        bt.size_hint = None, None
        bt.height = 15
        bt.width = 150
        bt.x = 120
        bt.y = 5
        #TextInput
        global ti
        ti = TextInput()
        ti.text = "Janela de texto."
        ti.color = 0, 0, 1, 1
        ti.size_hint = None, None
        ti.height = 350
        ti.width = 250
        ti.x = 70
        ti.y = 60
        # Layout
        Window.size = 400,500
        layout = FloatLayout()
        layout.add_widget(lb)
        layout.add_widget(ti)
        layout.add_widget(bt)

        return layout

    App.build = _build

    #janela = App()
    #janela.build = build
    #janela.run()


minha_janela = MinhaJanela()
minha_janela.title = "Exercícios de programação Python - AABeck"

minha_janela.run()