from model import Conta
from controller import create, read

abacate = Conta()
abacate.titular = 'luiza'
abacate.numero = '123'
abacate.saldo = 3000.0

create(abacate)

listaAbacates = read()
print(listaAbacates)

for c in listaAbacates:
    print(c)