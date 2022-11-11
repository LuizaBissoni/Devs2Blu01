from random import shuffle

n1 =  str(input('digite um nome, meu aliado: '))
n2 =  str(input('digite um nome, meu aliado: '))
n3 =  str(input('digite um nome, meu aliado: '))
n4 =  str(input('digite um nome, meu aliado: '))

lista = [n1, n2, n3, n4]

shuffle(lista)

print(lista)