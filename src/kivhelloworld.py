'''

'''

### Imports:
from kivy.app import App
from kivy.lang import Builder
import requests

### Init
GUI = Builder.load_file('telahelloworld.kv')

### Clasess:
class MeuAplicativo(App):
    def build(self):
        return GUI
    
    def on_start(self):
        self.root.ids['label1'].text = f'Dólar: R$ {self.pegar_cotacao("USD")}' #self.root é o GUI, ou seja, a minha janela
        self.root.ids['label2'].text = f'Euro: R$ {self.pegar_cotacao("EUR")}'
        self.root.ids['label3'].text = f'Bitcoin: R$ {self.pegar_cotacao("BTC")}'
        self.root.ids['label4'].text = f'Etherium: R$ {self.pegar_cotacao("ETH")}'

    def pegar_cotacao(self, moeda):
        link = f'https://economia.awesomeapi.com.br/last/{moeda}-BRL'
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao_moeda = dic_requisicao[f'{moeda}BRL']['bid']
        print(dic_requisicao)
        return cotacao_moeda

### Main:
MeuAplicativo().run()