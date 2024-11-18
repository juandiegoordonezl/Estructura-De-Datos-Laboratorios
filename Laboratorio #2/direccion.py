class Direccion:
    #Atributos
    def __init__(self,calle="No tiene una direccion registrada",nomenclatura="",barrio="",ciudad="",edificio="",apto=""):      
        self.__calle = calle
        self.__nomenclatura = nomenclatura
        self.__barrio = barrio
        self.__ciudad = ciudad 
        self.__edificio = edificio
        self.__apto = apto
        
    # Getters y Setters
    def getCalle(self):
        return self.__calle

    def setCalle(self, calle):
        self.__calle = calle
        
    def getCiudad(self):
        return self.__ciudad

    def setCiudad(self, ciudad):
        self.__ciudad = ciudad
        
    def getNomenclatura(self):
        return self.__nomenclatura

    def setNomenclatura(self, nomenclatura):
        self.__nomenclatura = nomenclatura
    
    def getEdificio(self):
        return self.__edificio

    def setEdificio(self, edificio):
        self.__edificio = edificio
    
    def getBarrio(self):
        return self.__barrio

    def setBarrio(self, barrio):
        self.__barrio = barrio
        
    def getApto(self):
        return self.__apto

    def setApto(self, apto):
        self.__apto= apto
        
    #Metodo toString()
    def __str__(self): 
        return self.__calle+" "+self.__nomenclatura+" "+self.__barrio+" "+self.__ciudad+" "+self.__edificio+" "+self.__apto
