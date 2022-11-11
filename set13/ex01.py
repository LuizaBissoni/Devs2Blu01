agua = int(input('quantos copos de água você bebeu hoje? '))
resto = agua % 2

print(f'sobrou {resto}')

if resto == 0:
    print('nº par')
else:
    print('nº ímpar')
