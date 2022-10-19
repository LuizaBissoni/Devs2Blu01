from dojo.calculadora import salario

def menu():
    print('='*15, 'calculadora salario', '='*15, '\n')
    var = 'sim'
    while var == 'sim':
        n1 = float(input('salario 1: '))
        n2 = float(input('salario 2: '))
        n3 = float(input('salario 3: '))
        n4 = float(input('salario 4: '))

        resultado = salario(n1, n2, n3, n4)
        print('a soma dos salarios é: {:.2f}'.format(resultado))

        var = input('voce quer continuar? \nsim \nnão \n:>')
menu()
print('voce saiu')