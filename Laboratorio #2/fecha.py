class Fecha:
    #Atributos
    def __init__(self, dd: int =1, mm: int =1, aa: int =1900):
        self.__dd = dd
        self.__mm = mm
        self.__aa = aa

    #Setters y Getters
    
    def set_Dia(self, dd: int):
        self.__dd = dd

    def set_Mes(self, mm: int):
        self.__mm = mm

    def set_A(self, aa):
        self.__aa = aa
    
    @property
    def get_Dia(self):
        return self.__dd
    @property
    def get_Mes(self):
        return self.__mm
    @property
    def get_A(self):
        return self.__aa

    def __str__(self) -> str:
        return f"{self.get_Dia} / {self.get_Mes} / {self.get_A}"

