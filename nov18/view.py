from model import Conta
from controller import create, read, update, delete

abacate = Conta()

abacate.titular = 'sss'
abacate.numero = 123
abacate.saldo = 3000.0

#create(abacate)

#listaAbacates = read()
#print(listaAbacates)

#for c in listaAbacates:
#    print(c)

update(abacate)
#delete(123)