#Trabalho Hotel
#Função horário saudação:
#Import Datetime;
#Import Sleep da lib time;
#Mostre na tela "Bom Dia", "Boa tarde" ou "Boa noite" de acordo com o hoário do sistema;
#Função Menu:
#1-Fazer check-In
#2-Relatório Hospedes
#3-Procurar Hospedes
#4-Fazer Check-Out
#5-Fizalizar Atendimento
#Função Check-In:
#Crie uma lista para o cadastro de pessoas: nome, sobrenome e idade.
from controller import *

#FUNÇÃO HORÁRIO SAUDAÇÃO
from doctest import OutputChecker
from re import A
from xmlrpc.client import DateTime
from time import sleep
#colocar um while para retornar 
hora = input("Digite o horário atual (hh:mm): ")

x = hora.split(':')
h = x[0]
m = x[1]

if (int(h) < 0 or int(h) > 24) or (int(m) < 0 or int(m) > 59):
    print(f'Horário inválido, digite novamente HH:MM')

else:
    if (int(h) >= 0 and int(h) <= 11):
        print("Bodiia! Seja bem-vindo!")

    if (int(h) >= 12 and int(h) <= 17):
        print("Boa tarde! Seja bem-vindo")

    else:
        print("Boa noite! Seja bem-vindo!")

#FUNÇÃO MENU
print('''
        Escolha uma opção
        [1] - Fazer Check-In
        [2] - Relatório Hóspedes
        [3] - Buscar Hóspede
        [4] - Fazer Check-Out
        [5] - Finalizar Atendimento
    ''')

poli = "="*20
cabecalho = print(f'\n{poli} Hostel Abacatis {poli}\n')

escolha = str(input('Escolha uma opção: '))

checkin = "1"
relatorio = "2"
buscar = "3"
checkout = "4"
finalizar = "5"

if escolha == "1":
    cliente = {}
    cliente["nome"] = input(("Digite seu nome: "))
    cliente["sobrenome"] = input(("Digite seu sobrenome: "))
    cliente["idade"] = input(("Digite sua idade: "))
    cadastro(cliente)
    
if escolha == "2":
    print(listar())
    
if escolha == "3":
    clienteFind()
    
if escolha == "4":
    fazerCheckout(clienteFind)