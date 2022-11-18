from model.pessoaJuridica import PessoaJuridica

def createPJ(conta):
    contas = open('PessoaJurídica.txt', 'a')
    contas.write(str(conta)+'\n')
    contas.close

def readPJ():
    listaContas = []
    contas = open('PessoaJurídica.txt', 'r')
    for conta in contas:

        conta = conta.strip()
        conta__objeto = conta.split(';')
        print(conta__objeto)

        pessoaJuridica = PessoaJuridica()
        pessoaJuridica.agencia = conta__objeto[0]
        pessoaJuridica.numeroAgencia = conta__objeto[1]
        pessoaJuridica.titular = conta__objeto[2]
        pessoaJuridica.CNPJ = conta__objeto[3]
        pessoaJuridica.saldoInicial = conta__objeto[4]

        listaContas.append(conta)
    contas.close
    return listaContas