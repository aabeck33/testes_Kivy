#coding: utf-8
__author__ = "Alvaro Adriano Beck"

##############
### Estudo ###
##############

class Retangulo:

    def __init__(self, largura, altura):
        self._altura = 0
        self._largura =0
        self.altura = altura
        self.largura = largura

    @property
    def altura(self):
        return self._altura
    @altura.setter
    def altura(self, num):
        if (not(isinstance(num, int) and (num > 0))):
            raise ValueError("Altura inválida: {}".format(num))
        self._altura = num

    @property
    def largura(self):
        return self._largura
    @largura.setter
    def largura(self, num):
        if (not(isinstance(num, int) and (num > 0))):
            raise ValueError("Largura inválida: {}".format(num))
        self._largura = num

    @property
    def area(self):
        return self._altura * self._largura

    @property
    def perimetro(self):
        return 2 * self._altura + 2 * self._largura


r = Retangulo(3,7)
a1 = r.area
r.altura = 5
r.largura = 9
a2 = r.area

r = None
r2 = Retangulo(1,2)
#r2 = None

print(a1, a2, r2.area, r2.perimetro)