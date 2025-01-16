from empleado import *
from listas import *
from controldecambios import    *


class Administrador(Empleado):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.solicitudes_pendientes = DoubleList()  # Lista doble para solicitudes pendientes
        self.control_cambios = DoubleList()  # Lista doble para registrar los cambios

    def agregar_usuario(self, archivo_empleados, archivo_passwords):
        """
        Solicita los datos al usuario para agregar un nuevo empleado y lo guarda en los archivos correspondientes.
        """
        print("Ingrese los datos del nuevo empleado:")
        nombre = input("Nombre (ej. Juan-Perez): ")
        id_empleado = int(input("Cédula: "))
        fecha_nacimiento = Fecha(
            int(input("Día de nacimiento: ")),
            int(input("Mes de nacimiento: ")),
            int(input("Año de nacimiento: "))
        )
        ciudad_nacimiento = input("Ciudad de nacimiento: ")
        tel = int(input("Teléfono: "))
        email = input("Correo electrónico: ")
        dir_empleado = Direccion(
            calle=input("Calle: "),
            nomenclatura=input("Nomenclatura: "),
            barrio=input("Barrio: "),
            ciudad=input("Ciudad: "),
            edificio=input("Edificio (opcional, enter para omitir): ") or None,
            apto=input("Número de apartamento (opcional, enter para omitir): ") or None
        )
        password = input("Contraseña: ")
        rol = input("Rol (administrador/investigador): ").lower()

        # Crear empleado
        empleado = Empleado(nombre, id_empleado, fecha_nacimiento, ciudad_nacimiento, tel, email, dir_empleado)

        try:
            # Guardar en archivo Empleados.txt
            with open(archivo_empleados, "a") as emp_file:
                emp_file.write(
                    f"\n{empleado.getNombre} {empleado.getId} {empleado.getFecha_nacimiento.get_Dia} "
                    f"{empleado.getFecha_nacimiento.get_Mes} {empleado.getFecha_nacimiento.get_A} "
                    f"{empleado.getCiudad_nacimiento} {empleado.getTel} {empleado.getEmail} "
                    f"{empleado.getDir}\n"
                )

            # Guardar en archivo Password.txt
            with open(archivo_passwords, "a") as pass_file:
                pass_file.write(f"\n{empleado.getId} {password} {rol}\n")

            print(f"Usuario {empleado.getNombre} agregado correctamente.")
        except Exception as e:
            print(f"Error al agregar usuario: {e}")

    def eliminar_usuario(self, archivo_empleados, archivo_passwords):
        """
        Solicita la cédula del usuario a eliminar y actualiza los archivos correspondientes.
        """
        cedula = int(input("Ingrese la cédula del usuario a eliminar: "))

        try:
            # Actualizar archivo Empleados.txt
            with open(archivo_empleados, "r") as emp_file:
                lines = emp_file.readlines()
            with open(archivo_empleados, "w") as emp_file:
                for line in lines:
                    if not line.split()[1] == str(cedula):
                        emp_file.write(line)

            # Actualizar archivo Password.txt
            with open(archivo_passwords, "r") as pass_file:
                lines = pass_file.readlines()
            with open(archivo_passwords, "w") as pass_file:
                for line in lines:
                    if not line.startswith(str(cedula)):
                        pass_file.write(line)

            print(f"Usuario con cédula {cedula} eliminado correctamente.")
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")

    def modificar_contraseña(self, archivo_passwords):
        """
        Solicita la cédula y la nueva contraseña del usuario y actualiza el archivo Password.txt.
        """
        cedula = int(input("Ingrese la cédula del usuario: "))
        nueva_password = input("Ingrese la nueva contraseña: ")

        try:
            with open(archivo_passwords, "r") as pass_file:
                lines = pass_file.readlines()
            with open(archivo_passwords, "w") as pass_file:
                for line in lines:
                    if line.startswith(str(cedula)):
                        datos = line.strip().split()
                        pass_file.write(f"{datos[0]} {nueva_password} {datos[2]}\n")
                    else:
                        pass_file.write(line)

            print(f"Contraseña del usuario con cédula {cedula} modificada correctamente.")
        except Exception as e:
            print(f"Error al modificar contraseña: {e}")
    
         
    @classmethod
    def cargar_inventario_administrador(cls, archivo_inventario, cedula):
        """
        Método de clase para filtrar el inventario general y obtener los objetos asignados
        a un administrador específico, excluyendo el nombre y la cédula, y ordenados de menor a mayor por número de placa.
        :param archivo_inventario: Ruta del archivo InventarioGeneral.txt.
        :param cedula: Cédula del administrador.
        :return: Lista doble con los objetos filtrados y ordenados.
        """
        from gestorArchivos import GestorArchivos  # Importación local para evitar circularidad
        try:
            # Cargar inventario general como lista doble
            inventario_general = GestorArchivos.cargar_inventario_general(archivo_inventario)

            # Crear una lista doble para el inventario del administrador
            inventario_administrador = DoubleList()

            # Filtrar objetos correspondientes a la cédula
            current = inventario_general.first()
            while current:
                equipo = current.getData()
                if equipo.cedula_empleado == cedula:
                    # Crear una copia del equipo excluyendo el nombre y la cédula
                    equipo_sin_nombre_cedula = {
                        "nombre_equipo": equipo.nombre_equipo,
                        "numero_placa": equipo.numero_placa,
                        "fecha_compra": equipo.fecha_compra,
                        "valor_compra": equipo.valor_compra,
                    }
                    inventario_administrador.addLast(equipo_sin_nombre_cedula)
                current = current.getNext()

            # Ordenar la lista del administrador
            inventario_administrador.sort(key=lambda equipo: equipo["numero_placa"])

            return inventario_administrador

        except Exception as e:
            print(f"Error al cargar el inventario del administrador: {e}")
            return None

    def consultar_solicitudes(self, archivo_agregar, archivo_eliminar):
        """
        Muestra todas las solicitudes pendientes, separándolas por tipo (adicionar o eliminar),
        leyendo directamente de los archivos de solicitudes.
        :param archivo_agregar: Ruta del archivo de solicitudes de adición.
        :param archivo_eliminar: Ruta del archivo de solicitudes de eliminación.
        """
        print("Solicitudes pendientes:")

        # Leer solicitudes para adicionar equipos
        try:
            with open(archivo_agregar, "r") as file:
                solicitudes_adicionar = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            print("\nNo se encontró el archivo de solicitudes para adicionar equipos.")
            solicitudes_adicionar = []
        except Exception as e:
            print(f"\nError al leer el archivo {archivo_agregar}: {e}")
            solicitudes_adicionar = []

        # Leer solicitudes para eliminar equipos
        try:
            with open(archivo_eliminar, "r") as file:
                solicitudes_eliminar = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            print("\nNo se encontró el archivo de solicitudes para eliminar equipos.")
            solicitudes_eliminar = []
        except Exception as e:
            print(f"\nError al leer el archivo {archivo_eliminar}: {e}")
            solicitudes_eliminar = []

        # Mostrar solicitudes de adicionar equipos
        if solicitudes_adicionar:
            print("\nSolicitudes para adicionar equipos:")
            for solicitud in solicitudes_adicionar:
                print(f"  - {solicitud}")
        else:
            print("\nNo hay solicitudes para adicionar equipos.")

        # Mostrar solicitudes para eliminar equipos
        if solicitudes_eliminar:
            print("\nSolicitudes para eliminar equipos:")
            for solicitud in solicitudes_eliminar:
                print(f"  - {solicitud}")
        else:
            print("\nNo hay solicitudes para eliminar equipos.")

    def procesar_solicitud(self, solicitud, aprobado: bool, archivo_agregar, archivo_eliminar, archivo_cambios):
        """
        Procesa una solicitud, aprobándola o rechazándola.
        :param solicitud: Objeto Solicitud a procesar.
        :param aprobado: True para aprobar la solicitud, False para rechazarla.
        :param archivo_agregar: Ruta del archivo para solicitudes de adición.
        :param archivo_eliminar: Ruta del archivo para solicitudes de eliminación.
        :param archivo_cambios: Ruta del archivo para el control de cambios.
        """
        if aprobado:
            solicitud.estado = "aprobada"
            investigador = solicitud.investigador

            if solicitud.tipo == "adicionar":
                # Agregar equipo al inventario del investigador
                investigador.inventario.addLast({
                    "nombre_equipo": solicitud.nombre,
                    "numero_placa": solicitud.placa,
                    "fecha_compra": solicitud.fecha_compra,
                    "valor_compra": solicitud.valor,
                })
                print(f"Equipo '{solicitud.nombre}' (Placa: {solicitud.placa}) agregado al inventario de {investigador.getNombre}.")

            elif solicitud.tipo == "eliminar":
                # Eliminar equipo del inventario del investigador
                current = investigador.inventario.first()
                encontrado = False
                while current:
                    equipo = current.getData()
                    if equipo["numero_placa"] == solicitud.placa:
                        investigador.inventario.remove(current)
                        print(f"Equipo con placa {solicitud.placa} eliminado del inventario de {investigador.getNombre}.")
                        encontrado = True
                        break
                    current = current.getNext()

                if not encontrado:
                    print(f"No se encontró el equipo con placa {solicitud.placa} en el inventario de {investigador.getNombre}.")
            
            # Registrar en el control de cambios
            self.registrar_cambio(
                tipo_cambio="Agregar" if solicitud.tipo == "adicionar" else "Eliminar",
                placa=solicitud.placa,
                investigador_id=solicitud.investigador.getId,
                estado="Aprobado",
                archivo_cambios=archivo_cambios
            )

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

        # Actualizar archivos de solicitudes pendientes
        self.actualizar_archivos_solicitudes(archivo_agregar, archivo_eliminar)


    def registrar_cambio(self, tipo_cambio, placa, investigador_id, estado, archivo_cambios):
        """
        Registra un cambio en el control de cambios y lo escribe en un archivo.
        :param tipo_cambio: Tipo de cambio ("Agregar" o "Eliminar").
        :param placa: Placa del equipo.
        :param investigador_id: ID del investigador.
        :param estado: Estado del cambio ("Aprobado").
        :param archivo_cambios: Ruta del archivo donde se registrarán los cambios.
        """
        from datetime import datetime
        cambio = ControlCambio(
            tipo_cambio=tipo_cambio,
            placa=placa,
            investigador_id=investigador_id,
            estado=estado
        )
        self.control_cambios.addLast(cambio)

        # Escribir el cambio en el archivo
        try:
            with open(archivo_cambios, "a") as file:  # Abrir en modo append
                file.write(
                    f"{cambio.investigador_id} {cambio.placa} {cambio.tipo_cambio} "
                    f"{cambio.fecha_hora.strftime('%Y-%m-%d %H:%M:%S')}\n"
                )
            print(f"Cambio registrado: {cambio}")
        except Exception as e:
            print(f"Error al registrar el cambio en {archivo_cambios}: {e}")

    
    def actualizar_archivos_solicitudes(self, archivo_agregar, archivo_eliminar):
        """
        Actualiza los archivos de solicitudes pendientes para adicionar y eliminar equipos.
        :param archivo_agregar: Ruta del archivo para solicitudes de adición.
        :param archivo_eliminar: Ruta del archivo para solicitudes de eliminación.
        """
        try:
            # Abrir los archivos en modo de escritura
            with open(archivo_agregar, "w") as agregar_file, open(archivo_eliminar, "w") as eliminar_file:
                current = self.solicitudes_pendientes.first()
                
                while current:
                    solicitud = current.getData()
                    
                    if solicitud.tipo == "adicionar":
                        # Escribir en el archivo de solicitudes de adición
                        agregar_file.write(
                            f"{solicitud.investigador.getNombre} {solicitud.investigador.getId} "
                            f"{solicitud.nombre} {solicitud.placa} "
                            f"{solicitud.fecha_compra.get_Dia} {solicitud.fecha_compra.get_Mes} {solicitud.fecha_compra.get_A} "
                            f"{solicitud.valor}\n"
                        )
                    elif solicitud.tipo == "eliminar":
                        # Escribir en el archivo de solicitudes de eliminación
                        eliminar_file.write(
                            f"{solicitud.investigador.getNombre} {solicitud.investigador.getId} "
                            f"{solicitud.placa} {solicitud.justificacion}\n"
                        )
                    
                    current = current.getNext()

            print(f"Archivos actualizados:\n - {archivo_agregar}\n - {archivo_eliminar}")
        except Exception as e:
            print(f"Error al actualizar los archivos de solicitudes: {e}")

    def generar_archivo_inventario_investigador(self, cedula, archivo, empleados):
        """
        Genera un archivo con el inventario de un investigador específico.
        :param cedula: Número de identificación del investigador.
        :param archivo: Ruta del archivo donde se guardará el inventario.
        :param empleados: Lista de empleados para buscar al investigador.
        """
        investigador = None
        current = empleados.first()
        while current:
            empleado = current.getData()
            if empleado.getId == cedula:
                investigador = empleado
                break
            current = current.getNext()

        if not investigador:
            print(f"No se encontró un investigador con la cédula {cedula}.")
            return

        investigador.generar_archivo_inventario(archivo)
        
    def generar_archivo_inventario_general(self, archivo):
        """
        Genera un archivo con el inventario general discriminado por investigador.
        :param archivo: Ruta del archivo donde se guardará el inventario general.
        """
        from gestorArchivos import GestorArchivos
        try:
            with open(archivo, "w") as file:
                inventario = GestorArchivos.cargar_inventario_general("InventarioGeneral.txt")
                current = inventario.first()
                if not current:
                    file.write("El inventario general está vacío.\n")
                    print("El inventario general está vacío. Archivo generado con un mensaje informativo.")
                    return

                while current:
                    equipo = current.getData()
                    file.write(f"{equipo.nombre_empleado} {equipo.cedula_empleado} {equipo.nombre_equipo} "
                            f"{equipo.numero_placa} {equipo.fecha_compra} {equipo.valor_compra}\n")
                    current = current.getNext()

            print(f"Archivo de inventario general generado: {archivo}")
        except Exception as e:
            print(f"Error al generar el archivo de inventario general: {e}")

    def generar_archivo_control_cambios(self, archivo):
        """
        Genera un archivo con el control de cambios.
        :param archivo: Ruta del archivo donde se guardará el control de cambios.
        """
        try:
            with open(archivo, "w") as file:
                current = self.control_cambios.first()
                if not current:
                    file.write("No hay cambios registrados.\n")
                    print("No hay cambios registrados. Archivo generado con un mensaje informativo.")
                    return

                while current:
                    cambio = current.getData()
                    file.write(f"{cambio.investigador_id} {cambio.placa} {cambio.tipo_cambio} "
                            f"{cambio.fecha_hora}\n")
                    current = current.getNext()

            print(f"Archivo de control de cambios generado: {archivo}")
        except Exception as e:
            print(f"Error al generar el archivo de control de cambios: {e}")
