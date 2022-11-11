from time import sleep
media = 0
while media < 7:

    nome = str(input('qual seu nome, jovem: '))
    sobrenome = str(input('diga seu sobrenome: '))
    idade = int(input('quntos anos tu tem? '))
    listanotas = []

    for c in range(0, 2):
        nota = int(input('digite uma nota: '))
        listanotas.append(nota)
        
    media = sum(listanotas) / len(listanotas)

    #print(media)

    situacao = 'Reprovado'

    if media >=7:
        for i in range(0,6):
            sleep(2)
            print('*')
        situacao = 'aprovado'

    dicionario_alunos = {'nome': nome, 'sobrenome': sobrenome, 'idade': idade, 'situacao': situacao, 'media': media}
    print(f'{dicionario_alunos["nome"]} {dicionario_alunos["sobrenome"]} {dicionario_alunos["idade"]} {dicionario_alunos["situacao"]} {dicionario_alunos["media"]}')