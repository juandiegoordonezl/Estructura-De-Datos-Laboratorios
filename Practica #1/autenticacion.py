class Autenticacion:
    def __init__(self, usuarios):
        self.usuarios = usuarios  # DoubleList que contiene los usuarios

    def iniciar_sesion(self, cedula, password):
        # Recorrer la lista doble para encontrar la cédula
        current = self.usuarios.first()
        while current:
            usuario = current.getData()
            if usuario["cedula"] == cedula and usuario["password"] == password:
                return usuario["rol"]
            current = current.getNext()
        return None
