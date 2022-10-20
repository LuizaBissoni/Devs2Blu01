def salvar(name):
    with open('dojo/pessoas.txt', 'a') as arquivo:
        arquivo.write(f'{name}\n')

def listar():
    nomes = []
    with open('dojo/pessoas.txt', 'r') as arquivo:
        for name in arquivo:
            name = name.strip()
            nomes.append(name)

    return nomes

#salvar('felipe ')
print('lista nomes',listar())