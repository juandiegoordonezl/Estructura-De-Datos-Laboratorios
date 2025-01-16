class Equipo:
    def __init__(self, nombre_empleado, cedula_empleado, nombre_equipo, numero_placa, fecha_compra, valor_compra):
        self.nombre_empleado = nombre_empleado
        self.cedula_empleado = cedula_empleado
        self.nombre_equipo = nombre_equipo
        self.numero_placa = numero_placa
        self.fecha_compra = fecha_compra
        self.valor_compra = valor_compra
    
    def getNumeroPlaca(self):
        """Retorna el número de placa del equipo."""
        return self.numero_placa
        
    def __str__(self):
        return f"{self.nombre_empleado} {self.cedula_empleado} {self.nombre_equipo} {self.numero_placa} {self.fecha_compra} {self.valor_compra}"
