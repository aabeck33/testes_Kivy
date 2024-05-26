#import aula4
from aula4 import *
import aula3
#import math
#from math import *
from pprint import pprint
import importlib

pprint(aula3.__dict__)
del(aula3.meus_dados)
aula3.meus_dados2 = {"sobrenome":"bECK","nome":"aLVARO","sexo":"m","idade":46}
pprint(aula3.__dict__)
importlib.reload(aula3)


from math import e, pi
from math import sqrt as raizq

print(e,pi)
print(raizq(9))

#aula4.funcao()
funcao()


#from sys import path as lpath
import sys

sys.path.insert(0,"c:\\temp\\")
sys.path.insert(0,"/home/abeck/modulos/")

pprint(sys.path)

"""
['/home/abeck/PycharmProjects/kivy/aulas', 
 '/home/abeck/PycharmProjects/kivy', 
 '/home/abeck/PycharmProjects/kivy/aulas', 
 '/home/abeck/.virtualenvs/k35/lib64/python35.zip', 
 '/home/abeck/.virtualenvs/k35/lib64/python3.5', 
 '/home/abeck/.virtualenvs/k35/lib64/python3.5/plat-linux', 
 '/home/abeck/.virtualenvs/k35/lib64/python3.5/lib-dynload', 
 '/usr/lib64/python3.5', 
 '/usr/lib/python3.5', 
 '/home/abeck/.virtualenvs/k35/lib/python3.5/site-packages']
"""

def func():
    print("Fala galera!")
import dis
dis.dis(func)

print(lista)