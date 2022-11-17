from model import Conta
from controller import create, read

abacate = Conta()
abacate.titular = 'luiza'
abacate.numero = '123'
abacate.saldo = 3000.0

create(abacate)

lista_abacate = read()
print(lista_abacate)

for c in lista_abacate:
    print(c)