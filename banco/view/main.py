from model.pessoaFisica import PessoaFisica
from model.pessoaJuridica import PessoaJuridica

from controller.juridico import createPJ, readPJ
from controller.fisico import createPF, readPF

def menu():
    menu=1
    while menu!=0:
        print('~'*20)
        print('\nAbacatis Agiotagem\n')
        menuInicial = int(input('[1] Pessoa Física\n[2] Pessoa Jurídica\n[3] Estou no lugar errado\n:> '))
        
        match menuInicial:
            case 1:
                print('~'*2, 'Conta Pessoa Física', '~'*2)
                menu = print(int(input('[1] Criar Conta\n[2] Listar Conta\n[3] Sair\n:> ')))
                match menu:
                    case 1:
                        conta = PessoaFisica()
                        conta.titular = input('Titular da Conta: ')
                        conta.CPF = input('CPF: ')
                        conta.saldoInicial = input('Saldo: ')

                        segundo = input('Cadastrar Segundo Titular?\nsim ou não\n:>')
                        if segundo == 'sim':
                            conta.segundoTitular = input('Segundo Titular: ')
                        createPF(conta)
                    case 2:
                        readPF()
            case 2:
                print('~'*2, 'Conta Pessoa Jurídica', '~'*2)
                menu = print(int(input('[1] Criar Conta\n[2] Listar Conta\n[3] Sair\n:> ')))
                match menu:
                    case 1:
                        conta = PessoaJuridica()
                        conta.titular = input('Titular da Conta: ')
                        conta.CNPJ = input('CNPJ: ')
                        conta.saldoInicial = input('Saldo: ')

                        segundo = input('Cadastrar Segundo Titular?\nsim ou não\n:>')
                        if segundo == 'sim':
                            conta.segundoTitular = input('Segundo Titular: ')
                        createPJ(conta)
                    case 2:
                        readPJ()   
            case 3:
                break
            













