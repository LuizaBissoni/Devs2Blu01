from criar_doc import salvar, listar

def menu():
    print('*'*20, 'menu', '*'*20)

    cond = 'sim'
    while cond == 'sim':
        nome = salvar(input('digite o nome: '))
        cond = str(input('continuar? \nsim \nnão \n:> '))

menu()
print('lista de nomes\n', listar())