from model import Conta

def create(conta):
    contas = open('contas.txt', 'a')
    contas.write(str(conta) + '\n')
    contas.close

def read():
    listaContas = []
    contas = open('contas.txt', 'r')

    for conta in contas:
        conta = conta.strip()
        contaObjeto = conta.split(';')
        print(contaObjeto)

        conta = Conta()
        conta.titular = contaObjeto[0]
        conta.numero = contaObjeto[1]
        conta.saldo = contaObjeto[2]
        listaContas.append(conta)

    contas.close
    return listaContas

def update(contaUpdate:Conta):
    listaContas = []
    contas = open('contas.txt','r')
    for conta in contas:
        contaLimpa = conta.strip()
        contaObjeto = contaLimpa.split(';')

        if contaUpdate.numero == int(contaObjeto[1]):
            listaContas.append(str(contaUpdate) + '\n') 
        else:
            listaContas.append(conta)
    contas.close()

    contas = open('contas.txt','w')
    contas.write(str(listaContas))
    contas.close()

def delete(numeroConta):
    listaContas = []
    contas = open('contas.txt', 'r')
    for conta in contas:
        contaLimpa = conta.strip()
        contaObjeto = contaLimpa.split(';')

        if numeroConta != int(contaObjeto[1]):
            listaContas.append(conta)

    contas.close()
    contas = open('contas.txt','w')
    contas.writelines(listaContas)
    contas.close()

    
