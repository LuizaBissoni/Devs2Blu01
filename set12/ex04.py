import random

n1 =  str(input('nome do seu pet: '))
n2 =  str(input('um país: '))
n3 =  str(input('qual o nome da sua mãe? '))
n4 =  str(input('água ou coca? '))

lista = [n1, n2, n3, n4]

sorteado = random.choice(lista) 

print('o nome sorteado foi: {}!'.format(sorteado))

if sorteado == n1:
    print('primeiro da lista')
elif sorteado == n2:
    print('segundo da lista')
elif sorteado == n3:
    print('terceiro da lista')
else:
    print('quarto da lista') 