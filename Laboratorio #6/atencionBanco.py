import random
from listas import SimpleList, SimpleNode, DoubleNode
from usuario import Usuario
from fecha import Fecha
from direccion import Direccion
from pilasycolas import*
from turnousuario import TurnoUsuario


# Pruebas sugeridas
if __name__ == "__main__":
    sistema = TurnoUsuario()
    
    usuarios = [
        Usuario("Juan", "101"),
        Usuario("Maria", "102"),
        Usuario("Carlos", "103"),
        Usuario("Ana", "104"),
        Usuario("Luis", "105")
    ]
    
    for usuario in usuarios:
        sistema.registrar(usuario)
    
    sistema.toFile()  # Guarda los 5 usuarios en usuariospendientes.txt
    
    sistema.atenderSiguiente()
    sistema.atenderSiguiente()
    
    sistema.toFile()
