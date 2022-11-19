from model.conta import Conta

class PessoaJuridica(Conta):
    __segundoTitular = ''
    __titular = ''
    __CNPJ = ''
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
    def CNPJ(self):
        return self.__CNPJ
    @CNPJ.setter
    def CNPJ(self, CNPJ):
        self.__CNPJ = CNPJ

    @property
    def saldoInicial(self):
        return self.__saldoInicial
    @saldoInicial.setter
    def saldoInicial(self, saldoInicial):
        self.__saldoInicial = saldoInicial

    def __str__(self):
        return f'{super().__str__()};{self.segundoTitular};{self.CNPJ};{self.titular};{self.saldoInicial}'
