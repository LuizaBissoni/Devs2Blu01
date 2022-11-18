from model.conta import Conta

class PessoaFisica(Conta):
    __segundoTitular = ''
    __titular = ''
    __CPF = ''
    __saldoInicial = 0

    @property
    def segundoTitular(self):
        return self.__segundoTitular
    @segundoTitular.setter
    def segundoTitular(self, segundoTitular):
        self.__segundoTitular = segundoTitular
    
    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    
    @property
    def CPF(self):
        return self.__CPF
    @CPF.setter
    def CPF(self, CPF):
        self.__CPF = CPF

    @property
    def saldoInicial(self):
        return self.__saldoInicial
    @saldoInicial.setter
    def saldoInicial(self, saldoInicial):
        self.__saldoInicial = saldoInicial

    def __str__(self):
        return f'{super().__str__()};{self.titular};{self.CPF};{self.saldoInicial};{self.segundoTitular}'
