import random

fruta =  str(input('fruta preferida: '))
refrigerante =  str(input('escolha um refrigerante: '))
comida =  str(input('quer massa ou risoto? '))
estacao =  str(input('primavera ou outono? '))

lista = [fruta, refrigerante, comida, estacao]

sorteado = random.choice(lista) 

print('escolho: {}!'.format(sorteado))