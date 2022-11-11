class Animal:

    def __init__(self, especie, raca, porte, cor):
        self.__especie = especie
        self.__raca = raca
        self.__porte = porte
        self.__cor = cor
    
    def set_especie(self, especie):
        self.__especie = especie
    def get_especie(self):
        return self.__especie
    
    def set_raca(self, raca):
        self.__raca = raca
    def get_raca(self):
        return self.__raca

    def set_porte(self, porte):
        self.__porte = porte
    def get_porte(self):
        return self.__porte
    
    def set_cor(self, cor):
        self.__cor = cor
    def get_cor(self):
        return self.__cor

    def __str__(self):
        return f'especie: {self.get_especie()}\nraca: {self.get_raca()}\nporte: {self.get_porte()}\ncor: {self.get_cor()}'

        