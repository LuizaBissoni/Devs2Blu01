# importar as 4 operações matemáticas do controller. 
# crie uma função print solicitando dados ao usuário (esta funcao deve ser com tipo predefinido tipo flutuante) 
# deve ser utilizado o conceito de interpolação para criar um cabeçalho de um menu, dentro deste menu deve conter a 
# possibilidade de fazer a impressão dos dados inseridos pelo usuário, permitindo assim o usuário escolher uma das 4 operações 
# matemáticas importadas, consequentemente imprimindo assim o resultado desejado dos dados inseridos.
from controller import soma
from controller import subtracao
from controller import multiplicacao
from controller import divisao

poli = "~" * 10

opcao=1

while opcao:
    print (f'\n {poli} Qual operação jovem? :) {poli} ')
    print("1 Somar")
    print("2 Subtrair")
    print("3 Multiplicação")
    print("4 Divisão ")

    opcao = int(input("Opção: "))

    if(opcao==1):
        soma()
    if(opcao==2):
        subtracao()
    if(opcao==3):
        multiplicacao()
    if(opcao==4):
        divisao()



