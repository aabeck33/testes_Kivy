def opera(op="doma",v1=0,v2=0):
    r = v1 + v2
    return r

def dados_pessoais(nome, sobrenome, idade,sexo):
    print("Nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {}".format(nome,sobrenome,idade,sexo))

def func():
    return 3, 6

j = func()
m,n = func()
print(j,m,n)

meus_dados = ("Alvaro","Beck",45,"M")
meus_dados2 = {"sobrenome":"Beck","nome":"Alvaro","sexo":"M","idade":45}
dados_pessoais(*meus_dados)
dados_pessoais(**meus_dados2)

dados_pessoais(nome="alvaro",idade=45,sobrenome="Beck",sexo="M")
t = opera(v1=2,v2=22)
print(t)

s = "Isso é um teste de strings."

for c in s:
    print(c)

for i in range(len(s)):
    print(s[i])

ind = 0
while ind < len(s):
    print(ind, s[ind])
    ind += 1

for k,v in enumerate(s):
    print(k,v)

