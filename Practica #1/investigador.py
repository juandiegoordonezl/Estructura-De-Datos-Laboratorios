from empleado import*
from solicitud import *
class Investigador(Empleado):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.solicitudes = DoubleList()

    def solicitar_agregar_equipo(self, nombre, placa, fecha_compra, valor):
        solicitud = Solicitud(tipo="agregar", nombre=nombre, placa=placa, fecha_compra=fecha_compra, valor=valor)
        self.solicitudes.addLast(solicitud)
        print(f"Solicitud para agregar equipo '{nombre}' (Placa: {placa}) enviada.")

    def solicitar_eliminar_equipo(self, placa, justificacion):
        solicitud = Solicitud(tipo="eliminar", placa=placa, justificacion=justificacion)
        self.solicitudes.addLast(solicitud)
        print(f"Solicitud para eliminar equipo (Placa: {placa}) enviada.")

