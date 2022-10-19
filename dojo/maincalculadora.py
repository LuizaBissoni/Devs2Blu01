from dojo.calculadora import soma, multi, divi, sub

def menu():
    print('*'*25, 'menu', '*'*25)

    cond = 'sim'
    while cond == 'sim':
        n1 = int(input('numero '))
        n2 = int(input('numero '))

        Soma = soma(n1, n2)
        Subtracao = sub(n1, n2)
        Divisao = divi(n1, n2)
        Multiplicacao = multi(n1, n2)
    
        print('a soma entre os numeros é: {}\n subtracao entre os numeros é: {}\na divisao entre os numeros é: {}\na multiplicacao entre os numeros é: {}\n'.format(Soma, Subtracao, Multiplicacao, Divisao))

        cond = str(input('deseja continuar?\nsim\nnão')) 

menu()
print('saiu')