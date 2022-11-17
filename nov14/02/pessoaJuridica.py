from conta import Conta

class PessoaJuridica:
    __segundo_titular = ' '

    def __init__(self, titular, cnpj, saldo):
        super().__init__('1313', 'conta Pessoa Jurídica')
        self.__titular = titular
        self.__cnpj = cnpj
        self.__saldo = saldo
        print('Passando pelo construtor da classe Pessoa Jurídica')
        
    @property 
    def segundo_titular(self):
        return self.__segundo_titular
    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular

    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self, titular):
        self.__titular = titular.title()
    
    @property
    def cnpj(self):
        return self.__cnpj
    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    def __str__(self):
        return f'{super().__str__()}\n Titular: {self.titular} \nCNPJ: {self.cnpj} \nSaldo Inicial: {self.saldo} \nSegundo Titular: {self.segundo_titular}'




    
    