pergunta_nome = 'Diga-me seu nome: '
alerta_nome = 'Impossível! conte-me a verdade meu chapa!'
pergunta_idade = 'Em que ano tu nasceu? '
alerta_idade = 'tem que se os 4 dígitos, pow '

def valida_numero(numero):
    try:
        numero = int(numero)
        return True
    except ValueError:
        return False
        
def perguntar(texto):
    valor = input(texto)
    return valor

while True:
    nome = str(perguntar(pergunta_nome))
    if len(nome) < 2:
        print(alerta_nome)
    else:
        break
        
while True:
    idade = perguntar(pergunta_idade)
    if valida_numero(idade) == True:
        idade = int(idade)
        if int(idade) < 1000:
            print(alerta_idade)
        else:
            break
    else:
        print('tá de sacanagem')

from datetime import date

current_date = date.today()
data_actual = current_date.year
idade = data_actual-idade 

print('Salve', nome)
print('Cê tem', idade, 'anos')

if idade >= 60:
  print('Chegastes na melhor idade ein')
elif idade >= 30:
  print('Tá ficando velho, Kk')
elif idade >= 24:
  print('Daqui pra frente, só pra trás bixo')
elif idade >= 18:
  print('Já pode ser preso, fica ligado')