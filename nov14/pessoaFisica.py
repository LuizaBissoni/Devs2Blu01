from conta import Conta 
class PessoaFisica(Conta):
    __segundo_titular = ' '

    def __init__(self, titular, cpf, saldoInicial):
        super().__init__('1030', 'Pessoa Física')
        self.titular = titular
        self.cpf = cpf
        self.saldoInicial = saldoInicial
        print('Passando pelo construtor da classe Pessoa Fisica')

    @property
    def segundo_titular(self):
        return self.__segundo_titular

    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular

    def __str__(self):
        return f'{super().__str__()} {self.titular} {self.cpf} {self.saldoInicial}'

