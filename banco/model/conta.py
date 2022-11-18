class Conta:
    __agencia = 'pomerode'
    __numeroAgencia = '001'

    @property
    def agencia(self):
        return self.__agencia
    @agencia.setter
    def agencia(self,agencia):
        self.__agencia = agencia
    
    @property
    def numeroAgencia(self):
        return self.__numeroAgencia
    @numeroAgencia.setter
    def numeroAgencia(self,numeroAgencia):
        self.__numeroAgencia = numeroAgencia

    def __str__(self):
        return f'{self.agencia};{self.numeroAgencia}'