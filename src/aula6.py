a = None
while a == None:
    try:
        a = int(input("Digite um número: "))
    except ValueError:
        #print("Isso não é um número. Tente novamente!\n")
        pass
print(a, "\n")

##--------------------------------------------


def input_num(i,msg):
    while True:
        try:
            if i == "i":
                r = int(input(msg))
            elif i == "f":
                r = float(input(msg))
            else:
                print("Erro nos parâmetros. (M001)")
                break
        except (ValueError, ZeroDivisionError) as e:
            print(type(e))
            print(e.args)
            print(e)
            print("Número inválido!\n")
        except (TypeError, NameError):
            pass
        else:
            return r
        finally:
            print("Essa parte sempre é executada!")


a = input_num("i","Digite um número: ")
print(a, "\n")