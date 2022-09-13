#estrutura de decisao

from html.entities import name2codepoint


n1 = float(input('digite uma nota para aula: '))
n2 = float(input('digite uma nota para o professor: '))

media = (n1 + n2) /2

print(f'a nota foi {media}')

if media >= 7:
    print('atingiu a média')
else:
    print('nao ta na media amigao') 