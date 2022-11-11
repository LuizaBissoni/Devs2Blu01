# crie uma variável recebendo dados 
# esta variável deve reproduzir em uma aplicação console 
# se os dados que foram digitados estão presente 
# Existe espaço, caracter alfabético, alfanumerico e numerico 
# utilizando boolean

aleatorio = input('digite algo aleatório: ')

print('existeespaco: ', aleatorio.isspace())
print('existealfabeto: ', aleatorio.isalpha())
print('existenumero: ', aleatorio.isalnum())
print('existeletraenumero: ', aleatorio.isnumeric())
