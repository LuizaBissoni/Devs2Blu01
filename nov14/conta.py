class Conta:
    def __init__(self,numero,tipo):
        self.numero = numero
        self.tipo = tipo
        print('passando pelo construtor da classe mãe')

    def __str__(self):
        return f'Conta: {self.numero} Tipo de Conta: {self.tipo}'

