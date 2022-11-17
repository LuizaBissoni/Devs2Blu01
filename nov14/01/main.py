from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica

pessoaFisica = PessoaFisica("abacate",'09157771936',13.00)
pessoaJuridica =PessoaJuridica("sr abacate",'13131313',13000.00)
print(pessoaFisica)

segundaPf = pessoaFisica.segundo_titular = "Lu"
print(segundaPf)

print(pessoaJuridica)

segundaPj = pessoaJuridica.segundo_titular = "Molly"

print(segundaPj)