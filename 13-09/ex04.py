CONSTANTE = 8

poli = "="*20

print(f"\n {poli} CABECALHO {poli} \n")

lista = []

soma = 0

for c in range(0, 3):
    numero = int(input("Digite um número: "))
    lista.append(numero)
    soma += numero

print(" {} + {} + {} = {} ".format(lista[0],lista[1],lista[2],soma))

print(f"\n {poli} RODAPE {poli} \n")

print(f"\n {poli} CABECALHO {poli} \n")

if soma > 10:
    print("A soma é maior que 10")
elif soma < 10:
    print("A soma é inferior a 10")
elif soma == 10:
    print("A soma é igual a 10")
elif soma != 10:
    print("A soma é diferente que 10")

print(f"\n {poli} RODAPE {poli} \n")