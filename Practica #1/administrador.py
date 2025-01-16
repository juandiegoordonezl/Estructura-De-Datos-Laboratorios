from empleado import *
from listas import *
from controldecambios import    *
class Administrador(Empleado):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.solicitudes_pendientes = DoubleList()
        self.control_cambios = DoubleList()

    def consultar_solicitudes(self):
        print("Solicitudes pendientes:")
        self.solicitudes_pendientes.printData()

    def procesar_solicitud(self, solicitud, aprobado: bool):
        if aprobado:
            solicitud.estado = "aprobada"
            self.control_cambios.addLast({
                "tipo": solicitud.tipo,
                "placa": solicitud.placa,
                "fecha_procesada": Fecha()
            })
            print(f"Solicitud para {solicitud.tipo} equipo (Placa: {solicitud.placa}) aprobada.")
        else:
            solicitud.estado = "rechazada"
            print(f"Solicitud para {solicitud.tipo} equipo (Placa: {solicitud.placa}) rechazada.")

        # Eliminar la solicitud procesada de pendientes
        current = self.solicitudes_pendientes.first()
        while current:
            if current.getData() == solicitud:
                self.solicitudes_pendientes.remove(current)
                break
            current = current.getNext()
    

    def registrar_cambio(self, tipo_cambio, placa, investigador_id, estado):
        """
        Registra un cambio en el control de cambios.
        """
        cambio = ControlCambio(tipo_cambio, placa, investigador_id, estado)
        self.control_cambios.addLast(cambio)
        print(f"Cambio registrado: {cambio}")

    def guardar_control_cambios(self, archivo):
        """
        Guarda el control de cambios en un archivo.
        """
        try:
            with open(archivo, "w") as file:
                current = self.control_cambios.first()
                while current:
                    file.write(
                        f"{current.getData().tipo_cambio},{current.getData().placa},"
                        f"{current.getData().investigador_id},{current.getData().estado},"
                        f"{current.getData().fecha_hora}\n"
                    )
            print(f"Control de cambios guardado en {archivo}.")
        except Exception as e:
            print(f"Error al guardar el control de cambios: {e}")

    def cargar_control_cambios(self, archivo):
        """
        Carga el control de cambios desde un archivo.
        """
        try:
            with open(archivo, "r") as file:
                for linea in file:
                    tipo_cambio, placa, investigador_id, estado, fecha_hora = linea.strip().split(",")
                    cambio = ControlCambio(
                        tipo_cambio=tipo_cambio,
                        placa=placa,
                        investigador_id=int(investigador_id),
                        estado=estado,
                        fecha_hora=datetime.fromisoformat(fecha_hora)
                    )
                    self.control_cambios.addLast(cambio)
            print(f"Control de cambios cargado desde {archivo}.")
        except FileNotFoundError:
            print(f"El archivo {archivo} no existe. No se cargaron cambios.")
        except Exception as e:
            print(f"Error al cargar el control de cambios: {e}")
