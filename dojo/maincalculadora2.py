from dojo.calculadora import soma, multi, divi, sub

def menu():
    print('*'*25, 'menu', '*'*25)

    cond = 'sim'
    while cond == 'sim':
        n1 = int(input('numero '))
        n2 = int(input('numero '))

        opcao = input('\n1 Somar \n2 Subtrair \n3 Multiplicar \n4 Dividir \nOperação :> ')
        resultado = 0
        
        match opcao:
            case '1':
                resultado = soma(n1, n2) #print(f'o resultado é {soma(n1, n2)}')
            case '2':
                resultado = sub(n1, n2)
            case '3':
                resultado = multi(n1, n2)
            case '4':
                resultado = divi(n1, n2)
            case _:
                print('opçao inválida')

        print('\nresultado: {}\n'.format(resultado))

        cond = str(input('deseja continuar?\nsim\nnão\n')) 

menu()
print('saiu')