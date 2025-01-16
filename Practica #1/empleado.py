from usuario import Usuario  # Importar la clase Usuario
from fecha import *
from direccion import *
from listas import *

class Empleado(Usuario):
    def __init__(self, nombre: str = None, id: int = None, fecha_nacimiento: Fecha = Fecha(),
                 ciudad_nacimiento: str = None, tel: int = None, email: str = None,
                 dir: Direccion = Direccion()):
        super().__init__(nombre, id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir)
        self.inventario = DoubleList()

    def agregar_equipo(self, equipo: str):
        self.inventario.addLast(equipo)
        print(f"Equipo '{equipo}' agregado al inventario.")

    def eliminar_equipo(self, equipo: str):
        current = self.inventario.first()
        while current:
            if current.getData() == equipo:
                self.inventario.remove(current)
                print(f"Equipo '{equipo}' eliminado del inventario.")
                return
            current = current.getNext()
        print(f"El equipo '{equipo}' no se encuentra en el inventario.")

    def consultar_inventario(self):
        print(f"Inventario de {self.getNombre}:")
        self.inventario.printData()

 
