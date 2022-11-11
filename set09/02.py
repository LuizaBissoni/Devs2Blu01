#Crie Variáveis utilizando a função que solicita inserção de dados, fica a seu critério a utilização de nomes de variáveis, 
#crie no mínimo 5 variáveis usando o conceito dinâmico onde o python usa sua semântica para identificar o tipo da variável 
#usando a função de impressão de dados use o conceito de interpolação e imprima os dados atribuídos na chamada!

nome = input('qual o seu nome, meliante? ')
sobrenome = input('e seu sobrenome? ')
idade = int(input('quantos anos? '))
cargo = input('trabalha com que? ')
cidade = input('mora onde? ')

print('nome', type(nome), '\n', 'sobrenome', type(sobrenome), '\n', 
      'idade', type(idade), '\n', 'cargo', type(cargo), '\n', 'cidade', type(cidade)
      )  