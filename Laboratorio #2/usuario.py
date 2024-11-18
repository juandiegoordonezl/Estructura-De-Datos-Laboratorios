class Usuario:
    #Atributos

    def __init__(self, nombre: str = "", id: int = 0, fecha_nacimiento: Fecha = Fecha(), 
                 ciudad_nacimiento: str = "", tel: int = 0, email: str = "", dir: Direccion = Direccion()):
        
        self.__nombre = nombre
        self.__id = id
        self.__fecha_nacimiento = fecha_nacimiento
        self.__ciudad_nacimiento = ciudad_nacimiento
        self.__tel = tel
        self.__email = email
        self.__dir = dir