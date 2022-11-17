from conta import Conta

class PessoaFisica(Conta):
    __segundo_titular = ' '
    
    def __init__(self, titular, cpf, saldo):
        super().__init__("500", "pessoafisica")
        self.__titular = titular
        self.__cpf = cpf
        self.__saldo = saldo
        print('Passando pelo construtor pessoa física.')
    @property
    def segundo_titular(self):
        return self.__segundo_titular
    
    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular
        
    def __str__(self):
        return f'{super().__str__()} {self.__titular} {self.__cpf} {self.__saldo}'