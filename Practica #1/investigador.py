from empleado import*
class Investigador(Empleado):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.solicitudes = DoubleList()
        
    @classmethod
    def cargar_inventario_investigador(cls, archivo_inventario, cedula):
        """
        Método de clase para filtrar el inventario general y obtener los objetos asignados
        a un investigador específico, excluyendo el nombre y la cédula, y ordenados de menor a mayor por número de placa.
        :param archivo_inventario: Ruta del archivo InventarioGeneral.txt.
        :param cedula: Cédula del investigador.
        :return: Lista doble con los objetos filtrados y ordenados.
        """
        from gestorArchivos import GestorArchivos  # Importación local para evitar circularidad
        try:
            # Cargar inventario general como lista doble
            inventario_general = GestorArchivos.cargar_inventario_general(archivo_inventario)

            # Crear una lista doble para el inventario del investigador
            inventario_investigador = DoubleList()

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
                    inventario_investigador.addLast(equipo_sin_nombre_cedula)
                current = current.getNext()

            # Ordenar la lista del investigador
            inventario_investigador.sort(key=lambda equipo: equipo["numero_placa"])

            return inventario_investigador

        except Exception as e:
            print(f"Error al cargar el inventario del investigador: {e}")
            return None

    def solicitar_adicionar_equipo(self, nombre, placa, fecha_compra, valor, cedula_administrador, empleados):
        """
        Crea una solicitud para adicionar un equipo y la envía al administrador correspondiente.
        :param nombre: Nombre del equipo.
        :param placa: Placa del equipo.
        :param fecha_compra: Fecha de compra del equipo.
        :param valor: Valor del equipo.
        :param cedula_administrador: Cédula del administrador al que se enviará la solicitud.
        :param empleados: Lista de empleados para buscar al administrador.
        """
        from solicitud import Solicitud  # Importación para evitar circularidad
        from administrador import Administrador

        # Buscar el administrador correspondiente
        administrador = None
        current = empleados.first()
        while current:
            empleado = current.getData()
            if isinstance(empleado, Administrador) and empleado.getId == cedula_administrador:
                administrador = empleado
                break
            current = current.getNext()

        if not administrador:
            print(f"No se encontró un administrador con la cédula {cedula_administrador}.")
            return

        # Crear y enviar la solicitud
        solicitud = Solicitud(
            tipo="adicionar",
            nombre=nombre,
            placa=placa,
            fecha_compra=fecha_compra,
            valor=valor,
            investigador=self  # Pasar referencia al investigador
        )
        administrador.solicitudes_pendientes.addLast(solicitud)
        administrador.actualizar_archivos_solicitudes("Solicitudes_agregar.txt", "Solicitudes_eliminar.txt")
        print(f"Solicitud para adicionar equipo '{nombre}' (Placa: {placa}) enviada al administrador {administrador.getNombre}.")

    def solicitar_eliminar_equipo(self, placa, justificacion, cedula_administrador, empleados):
        """
        Crea una solicitud para eliminar un equipo y la envía al administrador correspondiente.
        :param placa: Placa del equipo.
        :param justificacion: Justificación para eliminar el equipo.
        :param cedula_administrador: Cédula del administrador al que se enviará la solicitud.
        :param empleados: Lista de empleados para buscar al administrador.
        """
        from solicitud import Solicitud  # Importación para evitar circularidad

        # Buscar el administrador correspondiente
        administrador = None
        current = empleados.first()
        while current:
            empleado = current.getData()
            if empleado.getId == cedula_administrador:
                administrador = empleado
                break
            current = current.getNext()

        if not administrador:
            print(f"No se encontró un administrador con la cédula {cedula_administrador}.")
            return

        # Crear y enviar la solicitud
        solicitud = Solicitud(
            tipo="eliminar",
            placa=placa,
            justificacion=justificacion,
            investigador=self  # Pasar referencia al investigador
        )
        administrador.solicitudes_pendientes.addLast(solicitud)
        administrador.actualizar_archivos_solicitudes("Solicitudes_agregar.txt", "Solicitudes_eliminar.txt")
        print(f"Solicitud para eliminar equipo con placa {placa} enviada al administrador {administrador.getNombre}.")


    def consultar_estado_solicitudes(self, cedula_administrador, archivo_agregar, archivo_eliminar, archivo_cambios, empleados):
        """
        Muestra el estado de todas las solicitudes realizadas por el investigador.
        :param cedula_administrador: Cédula del administrador que gestiona las solicitudes.
        :param archivo_agregar: Ruta del archivo de solicitudes de adición.
        :param archivo_eliminar: Ruta del archivo de solicitudes de eliminación.
        :param archivo_cambios: Ruta del archivo de control de cambios.
        :param empleados: Lista de empleados para buscar al administrador.
        """
        # Buscar al administrador correspondiente
        administrador = None
        current = empleados.first()
        while current:
            empleado = current.getData()
            if empleado.getId == cedula_administrador:
                administrador = empleado
                break
            current = current.getNext()

        if not administrador:
            print(f"No se encontró un administrador con la cédula {cedula_administrador}.")
            return

        # Mostrar estado de solicitudes
        print("\nEstado de tus solicitudes:")

        # Solicitudes Pendientes
        print("\nSolicitudes pendientes:")
        try:
            solicitudes_pendientes = []
            # Leer solicitudes de adición
            with open(archivo_agregar, "r") as file:
                for line in file:
                    if str(self.getId) in line:
                        solicitudes_pendientes.append(line.strip())
            # Leer solicitudes de eliminación
            with open(archivo_eliminar, "r") as file:
                for line in file:
                    if str(self.getId) in line:
                        solicitudes_pendientes.append(line.strip())

            if solicitudes_pendientes:
                for solicitud in solicitudes_pendientes:
                    print(f"  - {solicitud}")
            else:
                print("  - No tienes solicitudes pendientes.")
        except FileNotFoundError:
            print("  - No se encontraron archivos de solicitudes.")
        except Exception as e:
            print(f"  - Error al leer los archivos de solicitudes: {e}")

        # Cambios Aprobados
        print("\nCambios aprobados:")
        try:
            cambios_aprobados = []
            # Leer el archivo de control de cambios
            with open(archivo_cambios, "r") as file:
                for line in file:
                    if str(self.getId) in line:
                        cambios_aprobados.append(line.strip())

            if cambios_aprobados:
                for cambio in cambios_aprobados:
                    investigador_id, placa, tipo_cambio, fecha, hora = cambio.split()
                    print(
                        f"  - {tipo_cambio} equipo con placa {placa} "
                        f"(Fecha: {fecha}, Hora: {hora})"
                    )
            else:
                print("  - No tienes cambios aprobados.")
        except FileNotFoundError:
            print("  - No se encontró el archivo de control de cambios.")
        except Exception as e:
            print(f"  - Error al leer el archivo de control de cambios: {e}")
            
    def generar_archivo_solicitudes(self, archivo, cedula_administrador, archivo_agregar, archivo_eliminar, archivo_cambios, empleados):
        """
        Genera un archivo con el estado de las solicitudes realizadas por el investigador.
        :param archivo: Ruta del archivo donde se guardará el estado de las solicitudes.
        :param cedula_administrador: Cédula del administrador que gestiona las solicitudes.
        :param archivo_agregar: Ruta del archivo de solicitudes de adición.
        :param archivo_eliminar: Ruta del archivo de solicitudes de eliminación.
        :param archivo_cambios: Ruta del archivo de control de cambios.
        :param empleados: Lista de empleados para buscar al administrador.
        """
        try:
            # Abrir el archivo para escritura
            with open(archivo, "w") as file:
                # Llamar a consultar_estado_solicitudes para obtener el estado
                print(f"Generando archivo de solicitudes en: {archivo}")
                print("\nEstado de tus solicitudes:\n", file=file)
                self.consultar_estado_solicitudes(cedula_administrador, archivo_agregar, archivo_eliminar, archivo_cambios, empleados)
                
                # Recopilar solicitudes pendientes
                if self.solicitudes.isEmpty():
                    file.write("No hay solicitudes realizadas.\n")
                    print("No hay solicitudes realizadas. Archivo generado con un mensaje informativo.")
                    return

                # Iterar sobre solicitudes pendientes y escribir en el archivo
                file.write("Solicitudes pendientes:\n")
                current = self.solicitudes.first()
                while current:
                    solicitud = current.getData()
                    file.write(f"  Tipo: {solicitud.tipo}, Placa: {solicitud.placa}, "
                            f"Estado: {solicitud.estado}, Fecha: {solicitud.fecha_solicitud}\n")
                    current = current.getNext()

                # Cambios aprobados
                file.write("\nCambios aprobados:\n")
                try:
                    with open(archivo_cambios, "r") as cambios_file:
                        cambios = [line.strip().split() for line in cambios_file if line.strip()]
                        cambios_investigador = [cambio for cambio in cambios if cambio[0] == str(self.getId)]

                        if not cambios_investigador:
                            file.write("  No tienes cambios aprobados.\n")
                        else:
                            for cambio in cambios_investigador:
                                investigador_id, placa, tipo_cambio, fecha, hora = cambio
                                file.write(f"  - {tipo_cambio} equipo con placa {placa} "
                                        f"(Fecha: {fecha}, Hora: {hora})\n")
                except FileNotFoundError:
                    file.write("  No se encontró el archivo de control de cambios.\n")
                except Exception as e:
                    file.write(f"  Error al leer el archivo de control de cambios: {e}\n")

            print(f"Archivo de estado de solicitudes generado correctamente en: {archivo}")
        except Exception as e:
            print(f"Error al generar el archivo de estado de solicitudes: {e}")

