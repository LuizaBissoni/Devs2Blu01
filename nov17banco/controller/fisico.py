from model.pessoaFisica import PessoaFisica

def createPF(conta):
    contas = open('PessoaFísica.txt', 'a')
    contas.write(str(conta)+'\n')
    contas.close

def readPF():
    listaContas = []
    contas = open('PessoaFísica.txt', 'r')
    for conta in contas:

        conta = conta.strip()
        conta__objeto = conta.split(';')
        print(conta__objeto)

        pessoaFisica = PessoaFisica()
        pessoaFisica.agencia = conta__objeto[0]
        pessoaFisica.numeroAgencia = conta__objeto[1]
        
        pessoaFisica.titular = conta__objeto[2]
        pessoaFisica.CPF = conta__objeto[3]
        pessoaFisica.saldoInicial = conta__objeto[4]

        listaContas.append(conta)
    contas.close
    return listaContas