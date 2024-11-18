class Direccion:
    #Atributos
    def __init__(self,calle=None,nomenclatura=None,barrio=None,ciudad=None,edificio=None,apto=None):      
        self.__calle = calle
        self.__nomenclatura = nomenclatura
        self.__barrio = barrio
        self.__ciudad = ciudad 
        self.__edificio = edificio
        self.__apto = apto
        
    # Getters y Setters
    def get__Calle(self):
        return self.__calle

    def set__Calle(self, calle):
        self.__calle = calle
        
    def get_Ciudad(self):
        return self.__ciudad

    def set_Ciudad(self, ciudad):
        self.__ciudad = ciudad
        
    def get_Nomenclatura(self):
        return self.__nomenclatura

    def set_Nomenclatura(self, nomenclatura):
        self.__nomenclatura = nomenclatura
    
    def get_Edificio(self):
        return self.__edificio

    def set_Edificio(self, edificio):
        self.__edificio = edificio
    
    def get_Barrio(self):
        return self.__barrio

    def set_Barrio(self, barrio):
        self.__barrio = barrio
        
    def get_Apto(self):
        return self.__apto

    def set_Apto(self, apto):
        self.__apto= apto

    def __str__(self):
        return self.__calle+self.__nomenclatura+self.__barrio+self.__ciudad+self.__edificio+self.__apto