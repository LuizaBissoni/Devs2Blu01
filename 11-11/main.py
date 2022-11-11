from conta import Conta

print('~'*5, 'Conta', '~'*5)

                #atributo titular
conta = Conta(input('Nome: '), 
#atributo Numero Conta
int(input('Conta: ')),
#atributo Saldo Conta
float(input('Saldo: ')),
#atributo limite Conta
float(input('Limite: ')))



print('~'*5, 'Conta', '~'*5)
print('Titular {} Conta {} Saldo {} Limite {}'.format(conta.titular, conta.numero, conta.saldo, conta.limite))