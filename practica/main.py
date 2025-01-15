class Serializador:
    separador = ';'
    
    @classmethod
    def guardar_txt(cls, datos, nombre_archivo, getAtributos):
        archivo = open(nombre_archivo, 'w')
        for objeto in datos:
            line = cls.separador.join(getAtributos(objeto)) + '\n'
            archivo.write(f"{line}\n")
        archivo.close()
        pass
    
    def cargar_txt(cls, instanciador, nombre_archivo):
        archivo = open(nombre_archivo, 'r')
        datos = []
        for line in archivo:
            atributos = line.strip().split(cls.separador)
            objeto = instanciador(*atributos)
            datos.append(objeto)
        archivo.close()
        return datos
    
    
    def cargar_array_txt(cls, nombre_archivo):
        archivo = open(nombre_archivo, 'r')
        datos = []
        for line in archivo:
            atributos = line.strip().split(cls.separador)
            datos.append(atributos)
        archivo.close()
        return datos
    
    def guardar_array_txt(cls, datos, nombre_archivo):
        archivo = open(nombre_archivo, 'w')
        for elementos in datos:
            line = cls.separador.join(elementos) + '\n'
            archivo.write(f"{line}\n")
        archivo.close()
        pass


class Usuario:
    def __init__(self, cedula, nombre, fecha_nacimiento, ciudad_nacimiento, telefono, correo, direccion):
        self.cedula = cedula
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.ciudad_nacimiento = ciudad_nacimiento
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion  # Instancia de la clase Dirección

class Password:
    
    serializerName = 'Password.txt'
    
    def __init__(self, documento, password, rol):
        self.documento = documento
        self.password = password
        self.rol = rol


class Empleado(Usuario):
    
    serializerName = 'Empleados.txt'
    
    def __init__(self, cedula, nombre, fecha_nacimiento, ciudad_nacimiento, telefono, correo, direccion, password, rol):
        super().__init__(cedula, nombre, fecha_nacimiento, ciudad_nacimiento, telefono, correo, direccion)
        self.password = password
        self.rol = rol
        
    def login(self, password):
        return self.password == password
        

class App:
    
    def __init__(self):
        self.usuario = None
    
    def login(self):
        cedula = input("Ingrese su cédula: ")
        password = input("Ingrese su contraseña: ")

        # Cargar empleados y contraseñas
        empleados = Serializador.cargar_txt(Empleado, Empleado.serializerName)
        passwords = Serializador.cargar_txt(Password, Password.serializerName)
        
        for i in range(len(empleados)):
            empleado = empleados[i]
            original_password = passwords[i]
            
            empleado.password = original_password.password
            if empleado.cedula == cedula and empleado.login(password):
                empleado.rol = original_password.rol
                self.usuario = empleado
                return True
            return False
    
    def start(self):
        
        print("Bienvenido al sistema")

        iniciado = False
        while not iniciado:
            iniciado = self.login()
            if not iniciado:
                print("Usuario o contraseña incorrectos")
        


def main():
    app = App()
    app.start()