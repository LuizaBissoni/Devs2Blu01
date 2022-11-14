from conta import Conta

print('~'*5, 'Conta', '~'*5)

               
conta = Conta(input('Nome: '), 

int(input('Conta: ')),

float(input('Saldo: ')),

float(input('Limite: ')))



print('~'*5, 'Conta', '~'*5)
print('Titular {} Conta {} Saldo {} Limite {}'.format(conta.titular, conta.numero, conta.saldo, conta.limite))