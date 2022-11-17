from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica

pessoaFisica = PessoaFisica(input('Nome:> '), input('CPF:> '), float(input('Saldo inicial:> ')))

print('~'*5, 'pessoa física', '~'*5)

print(pessoaFisica)

print('~'*5, 'segundo títular', '~'*5)

pessoaFisica.segundo_titular = 'Lu'
print(pessoaFisica)


pessoaJuridica= PessoaJuridica(input('Nome:> '), input('CPF:> '), float(input('Saldo inicial:> ')))

print('~'*5, 'pessoa jurídica', '~'*5)

print(pessoaJuridica)

print('~'*5, 'segundo títular', '~'*5)

pessoaJuridica.segundo_titular = 'Lu'
print(pessoaJuridica)