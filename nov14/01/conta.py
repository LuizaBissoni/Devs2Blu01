class Conta:
    def __init__(self,numero,tipo):
        self.numero = numero
        self.tipo = tipo
        print('passando pelo construtor da classe Conta')

    def __str__(self):
        return f'Conta: {self.numero} Tipo de Conta: {self.tipo}'

