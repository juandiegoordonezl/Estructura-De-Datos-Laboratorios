from fecha import *
from direccion import *

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

    #Setters

    def setNombre(self, nombre: str):
        self.__nombre = nombre

    def setId(self, id: int):
        self.__id = id

    def setFecha_nacimiento(self, fecha: Fecha):
        self.__fecha_nacimiento = fecha

    def setCiudad_nacimiento(self, ciudad: str):
        self.__ciudad_nacimiento = ciudad

    def setTel(self, tel: int):
        self.__tel = tel

    def setEmail(self, email: str):
        self.__email = email

    def setDir(self, dir: Direccion):
        self.__dir = dir
        
    #getters
    def getNombre(self):
        return self.__nombre

    def getId(self):
        return self.__id

    def getFecha_nacimiento(self):
        return self.__fecha_nacimiento

    def getCiudad_nacimiento(self):
        return self.__ciudad_nacimiento

    def getTel(self):
        return self.__tel

    def getEmail(self):
        return self.__email

    def getDir(self):
        return self.__dir
    
    #Metodo toString()
    def __str__(self): 
        return "Nombre: "+self.__nombre+"Id: "+self.__id+"Fecha de nacimiento: "+self.__fecha_nacimiento+"Ciudad de nacimento: "+self.__ciudad_nacimiento+"Tel: "+ self.__tel+"Email: "+self.__email+"Direccion: "+ print(self.__dir)

