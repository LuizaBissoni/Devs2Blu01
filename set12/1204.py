
n1 = float(input('digite uma nota para aula: '))
n2 = float(input('digite uma nota para o professor: '))

media = (n1 + n2) /2

print(f'a nota foi {media}')

print('tá dentro da média:' if media >= 7 else'não tá na média amigão')