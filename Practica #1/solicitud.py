from datetime import datetime

class Solicitud:
    def __init__(self, tipo, nombre=None, placa=None, fecha_compra=None, valor=None, justificacion=None, investigador=None):
        """
        Constructor para crear una solicitud.
        :param tipo: Tipo de solicitud ("adicionar" o "eliminar").
        :param nombre: Nombre del equipo (solo para "adicionar").
        :param placa: Placa del equipo.
        :param fecha_compra: Fecha de compra del equipo (solo para "adicionar").
        :param valor: Valor del equipo (solo para "adicionar").
        :param justificacion: Justificación para eliminar el equipo (solo para "eliminar").
        :param investigador: Referencia al investigador que creó la solicitud.
        """
        self.tipo = tipo
        self.nombre = nombre
        self.placa = placa
        self.fecha_compra = fecha_compra
        self.valor = valor
        self.justificacion = justificacion
        self.investigador = investigador  # Nueva referencia al investigador
        self.estado = "pendiente"  # "pendiente", "aprobada", "rechazada"
        self.fecha_solicitud = datetime.now()

    def __str__(self):
        if self.tipo == "adicionar":
            return (f"Solicitud: Adicionar equipo '{self.nombre}' (Placa: {self.placa}), "
                    f"Estado: {self.estado}, Fecha: {self.fecha_solicitud}")
        elif self.tipo == "eliminar":
            return (f"Solicitud: Eliminar equipo (Placa: {self.placa}), "
                    f"Justificación: {self.justificacion}, Estado: {self.estado}, Fecha: {self.fecha_solicitud}")
