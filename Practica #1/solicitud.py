from datetime import datetime

class Solicitud:
    def __init__(self, tipo, nombre=None, placa=None, fecha_compra=None, valor=None, justificacion=None):
        self.tipo = tipo  # "agregar" o "eliminar"
        self.nombre = nombre  # Solo para "agregar"
        self.placa = placa
        self.fecha_compra = fecha_compra  # Solo para "agregar"
        self.valor = valor  # Solo para "agregar"
        self.justificacion = justificacion  # Solo para "eliminar"
        self.estado = "pendiente"  # "pendiente", "aprobada", "rechazada"
        self.fecha_solicitud = datetime.now()

    def __str__(self):
        return f"Tipo: {self.tipo}, Placa: {self.placa}, Estado: {self.estado}, Fecha: {self.fecha_solicitud}"
