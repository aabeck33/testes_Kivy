__all__ = ["lista", "funcao"]


def funcao():
    pass


def _lista_args(*args):
    print(args)


def lista_arg_assoc(**kwargs):
    print(kwargs)


def argumentos(*args, **kwargs):
    print(args)
    print(kwargs)


def func(a, b, c):
    print(a)
    print(b)
    print(c)


tupla = 11,10,12
lista = [11,10,12]
func(**dict(zip(("b","a","c"), lista)))

lista.sort()
func(*lista)

_l = [*tupla]
_l.sort()
func(*_l)

_lista_args(1,2,3,4,5,)
lista_arg_assoc(a=2,e=3,g=9)
argumentos(1,2,3,5,8,a=2,r=4,g=90)

if (True):
    pass
print(__file__)