#dicionario
from contextlib import AbstractAsyncContextManager


dic = {}

nome = str(input('diga seu nome: '))
sobrenome = str(input('diga seu sobrenome: '))
idade = int(input('quntos anos tu tem? '))

dic['nome'] = nome
dic['sobrenome'] = sobrenome
dic['idade'] = idade

#print(dic)

print(dic[nome])