from datetime import datetime

class ControlCambio:
    def __init__(self, tipo_cambio, placa, investigador_id, estado, fecha_hora=None):
        self.tipo_cambio = tipo_cambio  # "Agregar" o "Eliminar"
        self.placa = placa
        self.investigador_id = investigador_id
        self.estado = estado  # "Aprobado" o "Rechazado"
        self.fecha_hora = fecha_hora if fecha_hora else datetime.now()

    def __str__(self):
        return (f"Tipo: {self.tipo_cambio}, Placa: {self.placa}, "
                f"Investigador ID: {self.investigador_id}, Estado: {self.estado}, "
                f"Fecha y Hora: {self.fecha_hora}")
