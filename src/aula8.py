#coding: utf-8
__author__ = "Alvaro Adriano Beck"

##############
### Estudo ###
##############


class Bichos:

    qnt_bichos = 0

    def __init__(self):
        self.add_bicho()

    def __del__(self):
        self.del_bicho()
        if self.qnt_bichos == 0:
            print("Todos os bichos foram mortos!")

    @classmethod
    def add_bicho(cls):
        cls.qnt_bichos += 1

    @classmethod
    def del_bicho(cls):
        cls.qnt_bichos -= 1

class MEstaticos:

    @staticmethod
    def func1():
        print("Func1()")

    @staticmethod
    def func2(x, y):
        print("Função '{}' invocada.\nParams=({}|{})".format("func2", x, y))

    @staticmethod
    def func3(a, b, c):
        info = """
        Nome da função: {nome}
        Quantidade de Args: {quantidade}
        Args: {args}
        """
        info = info.format(
            nome = MEstaticos.func3.__name__,
            quantidade = MEstaticos.func3.__code__.co_argcount,
            args = MEstaticos.func3.__code__.co_varnames
        )
        print(info)


class MinhaClasse:
    membro_cls = 50

    def __init__(self):
        self.membro_inst = -10

    def func(self):
        print(self.membro_inst)
        print(self.membro_cls)
        print(MinhaClasse.membro_cls)


i1 = MinhaClasse()
i2 = MinhaClasse()
MinhaClasse.membro_inst = 500
MinhaClasse.membro_cls = 100

print(i1.membro_cls, i1.membro_inst)
print(i2.membro_cls, i2.membro_inst)

#-------

print(Bichos.qnt_bichos)
b1 = Bichos()
print(Bichos.qnt_bichos)
b2 = Bichos()
print(Bichos.qnt_bichos)
b3 = Bichos()
print(Bichos.qnt_bichos)
del(b1)
print(Bichos.qnt_bichos)
del(b2)
print(Bichos.qnt_bichos)
del(b3)
print(Bichos.qnt_bichos)

#-------

me = MEstaticos()
me.func1()
me.func2(20, 40)
me.func3(10, 20, 30)