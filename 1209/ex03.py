ambiente = float(input('digite uma nota para o ambiente: '))
atendimento = float(input('digite uma nota para o atendimento: '))

media = (ambiente + atendimento) /2

print(f'ambiente: {ambiente} \natendimento: {atendimento} \na média foi: {media}')

if media > 7:
    print('está acima da média')
elif media == 7:
    print('está na média')
elif media > 5 < 7:
    print('você pode pedir para reapurar a nota')
elif media >= 4 == 5:
    print('você precisa falar com quem fez a avaliação')
else:
    print('nao ta na media amigao') 

#dojô

n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
media =  (n1 + n2) / 2

print('-'*15, '\n a primeira nota é: {}\n a segunda nota é: {} sua média é {}\n'.format(n1,n2,media),'-'*15
