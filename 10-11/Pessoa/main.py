from pessoa import Pessoa

pessoa = Pessoa(str(input("Nome: ")), str(input('CPF: ')), int(input('Idade: ')), float(input('Altura: ')))

print('~'*5, 'Dados Peaple', '~'*5)
print(pessoa)
print('~'*5, 'É isso pexual', '~'*5)

pessoa2 = Pessoa(str(input("Nome: ")), str(input('CPF: ')), int(input('Idade: ')), float(input('Altura: ')))

print('~'*5, 'Dados Peaple', '~'*5)
print(pessoa2)
print('~'*5, 'É isso jovem', '~'*5)