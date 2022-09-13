#Crie variáveis com tipos predefinidos, utilizando a função de inserção de dados, 
#fica a seu critério a utilização de nomes de variáveis, crie no mínimo 4 variáveis, 
#usando máscara de substituição atribua estas variáveis as suas respectivas descrições

bolacha = str(input('qual sua bolacha preferida: '))
qntbolacha = float(input('come quantas por mês? '))
bebida = str(input('diga-me seu nome: '))
qntbebida = int(input('quantos anos tu tem? '))

print('quer dizer que teu nome é {}, tu ganha {:.2f} e tens {} anos!'.format(bolacha, qntbolacha, bebida, qntbebida))