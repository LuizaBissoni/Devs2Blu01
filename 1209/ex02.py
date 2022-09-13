from random import shuffle

fruta =  str(input('fruta preferida: '))
refrigerante =  str(input('escolha um refrigerante: '))
comida =  str(input('quer massa ou risoto? '))
estacao =  str(input('primavera ou outono? '))

lista = [fruta, refrigerante, comida, estacao]

shuffle(lista)

print(lista)

#dojô

import random

fruta =  str(input('fruta preferida: '))
refrigerante =  str(input('escolha um refrigerante: '))
comida =  str(input('quer massa ou risoto? '))
estacao =  str(input('primavera ou outono? '))

lista = [fruta, refrigerante, comida, estacao]

print('-' * 8, 'console', '-' *8)

print(f'lista normal: {lista}')

random.shuffle(lista)

print(f'lista embaralhada: {lista}')