from conta import Conta 
class PessoaJuridica(Conta):
    __segundo_titular = ' '

    def __init__(self, titular, CNPJ, saldoInicial):
        super().__init__('1030', 'Pessoa Jurídica')
        self.titular = titular
        self.CNPJ = CNPJ
        self.saldoInicial = saldoInicial
        print('Passando pelo construtor da classe Pessoa Jurídica')

    @property
    def segundo_titular(self):
        return self.__segundo_titular

    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular

    def __str__(self):
        return f'{super().__str__()} {self.titular} {self.CNPJ} {self.saldoInicial}'