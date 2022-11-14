# 1- função imutável procedimento
def mensagem():
    print('hello word')

def mensagem2():
    print('hello word dinovo')

mensagem()
mensagem2()

def soma():
    n1 = 1
    n2 = 2
    resultado = n1 + n2

    print(resultado) # return resultado

soma() # print(soma())

def soma2(numero1, numero2):
    return numero1 + numero2

print(soma2(10, 10))