from listas import DoubleList  # Se asume que las clases DoubleNode y DoubleList están en este archivo
from empleado import Empleado
from fecha import Fecha
from direccion import Direccion


class GestorArchivos:
    @staticmethod
    def cargar_empleados(archivo_empleados):
        empleados = DoubleList()
        try:
            with open(archivo_empleados, "r") as archivo:
                for linea in archivo:
                    try:
                        # Dividir la línea usando espacios y limpiar
                        datos = [dato.strip() for dato in linea.strip().split()]
                        
                        # Validar cantidad mínima de campos
                        if len(datos) < 7:
                            raise ValueError("Línea con datos insuficientes")
                        
                        # Extraer datos básicos
                        nombre = datos[0]
                        cedula = int(datos[1])
                        fecha = Fecha(*map(int, datos[2:5]))
                        ciudad = datos[5]
                        telefono = int(datos[6])
                        email = datos[7]
                        
                        # Procesar dirección
                        direccion_partes = datos[8:]
                        direccion = Direccion(
                            direccion_partes[0],
                            direccion_partes[1],
                            direccion_partes[2],
                            direccion_partes[3],
                            direccion_partes[4] if len(direccion_partes) > 4 else None,
                            direccion_partes[5] if len(direccion_partes) > 5 else None,
                        )

                        # Crear empleado y agregarlo a la lista
                        empleado = Empleado(nombre, cedula, fecha, ciudad, telefono, email, direccion)
                        empleados.addLast(empleado)
                    except (IndexError, ValueError) as e:
                        print(f"Error al procesar línea: '{linea.strip()}'. Detalle: {e}")
        except FileNotFoundError:
            print(f"Error: El archivo {archivo_empleados} no existe.")
        except Exception as e:
            print(f"Error inesperado al cargar empleados: {e}")
        return empleados

    @staticmethod
    def cargar_passwords(archivo_passwords):
        usuarios = DoubleList()
        try:
            with open(archivo_passwords, "r") as archivo:
                for linea in archivo:
                    try:
                        # Dividir la línea usando espacios
                        datos = [dato.strip() for dato in linea.strip().split()]
                        
                        # Validar cantidad exacta de campos
                        if len(datos) != 3:
                            raise ValueError("Formato incorrecto en línea")
                        
                        cedula = int(datos[0])
                        password = datos[1]
                        rol = datos[2]

                        usuario = {"cedula": cedula, "password": password, "rol": rol}
                        usuarios.addLast(usuario)
                    except (IndexError, ValueError) as e:
                        print(f"Error al procesar línea: '{linea.strip()}'. Detalle: {e}")
        except FileNotFoundError:
            print(f"Error: El archivo {archivo_passwords} no existe.")
        except Exception as e:
            print(f"Error inesperado al cargar contraseñas: {e}")
        return usuarios
