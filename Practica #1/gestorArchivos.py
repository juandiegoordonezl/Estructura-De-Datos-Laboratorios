from listas import DoubleList  # Se asume que las clases DoubleNode y DoubleList están en este archivo
from empleado import Empleado
from fecha import Fecha
from direccion import Direccion
from  equipo import Equipo
from administrador import Administrador
from investigador import Investigador


class GestorArchivos:
    def cargar_usuarios(archivo_empleados, archivo_passwords):
        """
        Carga usuarios desde los archivos Empleados.txt y Password.txt.
        Retorna una lista doble con instancias de Administrador e Investigador.
        """
        empleados = DoubleList()
        contraseñas = {}

        # Cargar contraseñas y roles desde Password.txt
        try:
            with open(archivo_passwords, "r") as pass_file:
                for linea in pass_file:
                    datos = linea.strip().split()
                    if len(datos) == 3:
                        contraseñas[int(datos[0])] = {"password": datos[1], "rol": datos[2]}
        except FileNotFoundError:
            print(f"Error: El archivo {archivo_passwords} no existe.")
            return empleados
        except Exception as e:
            print(f"Error inesperado al cargar contraseñas: {e}")
            return empleados

        # Cargar empleados desde Empleados.txt
        try:
            with open(archivo_empleados, "r") as emp_file:
                for linea in emp_file:
                    try:
                        datos = linea.strip().split()
                        if len(datos) < 8:
                            raise ValueError("Datos insuficientes en línea.")

                        nombre = datos[0]
                        cedula = int(datos[1])
                        fecha_nacimiento = Fecha(int(datos[2]), int(datos[3]), int(datos[4]))
                        ciudad_nacimiento = datos[5]
                        telefono = int(datos[6])
                        email = datos[7]
                        direccion = Direccion(
                            datos[8], datos[9], datos[10], datos[11],
                            datos[12] if len(datos) > 12 else None,
                            datos[13] if len(datos) > 13 else None
                        )

                        # Verificar rol del usuario
                        if cedula in contraseñas:
                            rol = contraseñas[cedula]["rol"]
                            if rol == "administrador":
                                usuario = Administrador(nombre, cedula, fecha_nacimiento, ciudad_nacimiento, telefono, email, direccion)
                            else:  # investigador
                                usuario = Investigador(nombre, cedula, fecha_nacimiento, ciudad_nacimiento, telefono, email, direccion)

                            empleados.addLast(usuario)
                        else:
                            print(f"No se encontró rol para el usuario con cédula {cedula}.")
                    except ValueError as ve:
                        print(f"Error al procesar línea: '{linea.strip()}'. Detalle: {ve}")
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

    @staticmethod
    def cargar_inventario_general(archivo_inventario):
        inventario = DoubleList()

        try:
            with open(archivo_inventario, "r") as archivo:
                for linea in archivo:
                    try:
                        # Dividir línea en partes y validar
                        datos = linea.strip().split(" ")
                        if len(datos) != 8:
                            raise ValueError("Línea con datos insuficientes")
                        
                        # Extraer datos de la línea
                        nombre_empleado = datos[0]
                        cedula_empleado = int(datos[1])
                        nombre_equipo = datos[2]
                        numero_placa = int(datos[3])
                        fecha_compra = Fecha(int(datos[4]), int(datos[5]), int(datos[6]))
                        valor_compra = float(datos[7])

                        # Crear objeto Equipo
                        equipo = Equipo(nombre_empleado, cedula_empleado, nombre_equipo, numero_placa, fecha_compra, valor_compra)
                        
                        # Agregar a la lista doble directamente
                        inventario.addLast(equipo)
                    except (ValueError, IndexError) as e:
                        print(f"Error al procesar línea: '{linea.strip()}'. Detalle: {e}")

            # Ordenar la lista doble por número de placa
            inventario.sort(key=lambda equipo: equipo.getNumeroPlaca())

        except FileNotFoundError:
            print(f"Error: El archivo {archivo_inventario} no existe.")
        except Exception as e:
            print(f"Error inesperado: {e}")

        return inventario

    