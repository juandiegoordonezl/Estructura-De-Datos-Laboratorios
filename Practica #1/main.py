from gestorArchivos import GestorArchivos
from autenticacion import Autenticacion
from investigador import Investigador
from administrador import Administrador
from fecha import *

def main():
    # Cargar datos iniciales
    empleados = GestorArchivos.cargar_usuarios("Practica #1/Empleados.txt", "Practica #1/Password.txt")
    usuarios = GestorArchivos.cargar_passwords("Practica #1/Password.txt")

    # Crear instancia de autenticación
    auth = Autenticacion(usuarios)

    print("Empleados cargados:")
    empleados.printData()

    node = usuarios.first()
    while node:
        print(node.getData())
        node = node.getNext()

    print("Bienvenido al sistema de inventario del centro de investigación.")
    cedula = int(input("Ingrese su número de identificación: "))
    password = input("Ingrese su contraseña: ")

    # Autenticación
    rol = auth.iniciar_sesion(cedula, password)
    if not rol:
        print("Credenciales incorrectas. Por favor, intente de nuevo.")
        return

    # Identificar rol del usuario
    empleado = None
    current = empleados.first()
    while current:
        if current.getData().getId == cedula:
            empleado = current.getData()
            break
        current = current.getNext()

    if not empleado:
        print("No se encontró un empleado con la cédula ingresada.")
        return

    if rol == "investigador":
        print(f"Bienvenido, Investigador {empleado.getNombre}.")
        investigador = empleado
        while True:
            print("\nOpciones de Investigador:")
            print("1. Consultar inventario")
            print("2. Solicitar agregar equipo")
            print("3. Solicitar eliminar equipo")
            print("4. Consultar estado de solicitudes")
            print("5. Generar archivo de inventario asignado")
            print("6. Generar archivo de solicitudes vigentes")
            print("7. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print("Consultando inventario asignado...")
                inventario_asignado = Investigador.cargar_inventario_investigador(
                    "Practica #1/InventarioGeneral.txt", investigador.getId
                )
                if inventario_asignado:
                    print("Inventario asignado al investigador (sin nombre ni cédula):")
                    current = inventario_asignado.first()
                    while current:
                        equipo = current.getData()
                        print(f"Equipo: {equipo['nombre_equipo']}, Placa: {equipo['numero_placa']}, "
                            f"Fecha de Compra: {equipo['fecha_compra']}, Valor: ${equipo['valor_compra']:.2f}")
                        current = current.getNext()
                else:
                    print("No se encontró inventario asignado o hubo un error.")
                    
            elif opcion == "2":
                print("Solicitud para adicionar equipo:")
                nombre = input("Nombre del equipo: ")
                placa = input("Placa del equipo: ")
                fecha_compra = Fecha(*map(int, input("Fecha de compra (dd/mm/aaaa): ").split("/")))
                valor = float(input("Valor del equipo: "))
                cedula_administrador = int(input("Ingrese la cédula del administrador: "))
                investigador.solicitar_adicionar_equipo(nombre, placa, fecha_compra, valor, cedula_administrador, empleados)

            elif opcion == "3":
                print("Solicitud para eliminar equipo:")
                placa = input("Placa del equipo a eliminar: ")
                justificacion = input("Justificación para eliminar el equipo: ")
                cedula_administrador = int(input("Ingrese la cédula del administrador: "))
                investigador.solicitar_eliminar_equipo(placa, justificacion, cedula_administrador, empleados)


            elif opcion == "4":
                cedula_administrador = int(input("Ingrese la cédula del administrador: "))
                print("Consultando estado de tus solicitudes:")
                investigador.consultar_estado_solicitudes(
                    cedula_administrador,
                    "Solicitudes_agregar.txt",
                    "Solicitudes_eliminar.txt",
                    "Control_de_cambios.txt",
                    empleados
                 )

            elif opcion == "5":
                archivo = f"{investigador.getNombre}_{investigador.getId}.txt"
                investigador.generar_archivo_inventario(archivo,investigador.getId)
                print(f"Archivo de inventario generado: {archivo}")

            elif opcion == "6":
                archivo = f"Solicitudes{investigador.getNombre}_{investigador.getId}.txt"
                cedula_administrador = int(input("Ingrese la cédula del administrador: "))
                investigador.generar_archivo_solicitudes(archivo,cedula_administrador,
                    "Solicitudes_agregar.txt",
                    "Solicitudes_eliminar.txt",
                    "Control_de_cambios.txt",
                    empleados)
                print(f"Archivo de solicitudes generado: {archivo}")

            elif opcion == "7":
                print("Cerrando sesión...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    elif rol == "administrador":
        print(f"Bienvenido, Administrador {empleado.getNombre}.")
        administrador = empleado
        while True:
            print("\nOpciones de Administrador:")
            print("1. Consultar inventario asignado")
            print("2. Consultar solicitudes")
            print("3. Procesar solicitud")
            print("4. Agregar usuario")
            print("5. Eliminar usuario")
            print("6. Cambiar contraseñas")
            print("7. Consultar inventario general")
            print("8. Cargar control de cambios")
            print("9. Guardar control de cambios")
            print("10. Generar archivo de inventario investigador")
            print("11. Generar archivo de inventario general")
            print("12. Generar archivo de solicitudes para agregar")
            print("13. Generar archivo de solicitudes para eliminar")
            print("14. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print("Consultando inventario asignado...")
                inventario_asignado = Administrador.cargar_inventario_administrador(
                    "Practica #1/InventarioGeneral.txt", administrador.getId
                )
                if inventario_asignado:
                    print("Inventario asignado al administrador:")
                    current = inventario_asignado.first()
                    while current:
                        equipo = current.getData()
                        print(f"Equipo: {equipo['nombre_equipo']}, Placa: {equipo['numero_placa']}, "
                            f"Fecha de Compra: {equipo['fecha_compra']}, Valor: ${equipo['valor_compra']:.2f}")
                        current = current.getNext()
                else:
                    print("No se encontró inventario asignado o hubo un error.")

                                    
            elif opcion == "2":
                print("Consultando solicitudes pendientes...")
                administrador.consultar_solicitudes("Solicitudes_agregar.txt", "Solicitudes_eliminar.txt")

                
            elif opcion == "3":
                print("Procesar una solicitud:")

                # Mostrar solicitudes pendientes desde los archivos
                administrador.consultar_solicitudes("Solicitudes_agregar.txt", "Solicitudes_eliminar.txt")

                tipo_solicitud = input("\n¿Desea procesar una solicitud para 'adicionar' o 'eliminar' equipos? (adicionar/eliminar): ").lower()

                # Verificar el tipo de solicitud
                if tipo_solicitud == "adicionar":
                    archivo_solicitud = "Solicitudes_agregar.txt"
                elif tipo_solicitud == "eliminar":
                    archivo_solicitud = "Solicitudes_eliminar.txt"
                else:
                    print("Tipo de solicitud no válido. Operación cancelada.")
                    continue

                try:
                    # Leer el archivo correspondiente
                    with open(archivo_solicitud, "r") as file:
                        solicitudes = [line.strip() for line in file if line.strip()]
                

                    if not solicitudes:
                        print(f"No hay solicitudes pendientes para {tipo_solicitud}.")
                        continue

                    # Mostrar las solicitudes con índices
                    print(f"\nSolicitudes para {tipo_solicitud}:")
                    for idx, solicitud in enumerate(solicitudes, start=1):
                        print(f"{idx}. {solicitud}")

                    # Seleccionar una solicitud para procesar
                    indice = int(input("\nSeleccione el índice de la solicitud a procesar (0 para cancelar): "))
                    if indice == 0:
                        print("Operación cancelada.")
                        continue

                    # Validar el índice seleccionado
                    if indice < 1 or indice > len(solicitudes):
                        print("Índice no válido. Operación cancelada.")
                        continue

                    # Procesar la solicitud seleccionada
                    solicitud = solicitudes[indice - 1]
                    decision = input(f"¿Aprobar solicitud '{solicitud}'? (s/n): ").lower()
                    aprobado = decision == "s"
                except FileNotFoundError:
                    print(f"Archivo {archivo_solicitud} no encontrado. Operación cancelada.")
                except ValueError:
                    print("Índice no válido. Operación cancelada.")
                except Exception as e:
                    print(f"Error al procesar la solicitud: {e}")
                    # Eliminar la solicitud del archivo
                    with open(archivo_solicitud, "w") as file:
                        for idx, line in enumerate(solicitudes, start=1):
                            if idx != indice:  # Escribir todas excepto la seleccionada
                                file.write(line + "\n")

                    if aprobado:
                        solicitud_partes = solicitud.split()
                        investigador_nombre, investigador_id = solicitud_partes[0], int(solicitud_partes[1])

                        if tipo_solicitud == "adicionar":
                            # Extraer información del equipo
                            nombre_equipo = solicitud_partes[2]
                            numero_placa = solicitud_partes[3]
                            dia, mes, anio = map(int, solicitud_partes[4:7])
                            fecha_compra = Fecha(dia, mes, anio)
                            valor = float(solicitud_partes[7])

                            # Agregar al inventario general
                            with open("InventarioGeneral.txt", "a") as inventario_general:
                                inventario_general.write(f"{investigador_nombre} {investigador_id} {nombre_equipo} {numero_placa} "
                                                        f"{dia} {mes} {anio} {valor}\n")

                            # Agregar al inventario del investigador
                            current = empleados.first()
                            investigador = None
                            while current:
                                empleado = current.getData()
                                if empleado.getId == investigador_id:
                                    investigador = empleado
                                    break
                                current = current.getNext()

                            if investigador:
                                investigador.inventario.addLast({
                                    "nombre_equipo": nombre_equipo,
                                    "numero_placa": numero_placa,
                                    "fecha_compra": fecha_compra,
                                    "valor_compra": valor
                                })
                                print(f"Equipo '{nombre_equipo}' (Placa: {numero_placa}) agregado al inventario del investigador {investigador_nombre}.")

                                # Registrar en el control de cambios
                                administrador.registrar_cambio(
                                    tipo_cambio="Agregar",
                                    placa=numero_placa,
                                    investigador_id=investigador_id,
                                    estado="Aprobado",
                                    archivo_cambios="Control_de_cambios.txt"
                                )
                                print(f"Solicitud '{solicitud}' aprobada y registrada en el control de cambios.")
                
       
                                
                            elif tipo_solicitud == "eliminar":
                                # Extraer información de la solicitud
                                solicitud_partes = solicitud.split()
                                investigador_nombre, investigador_id = solicitud_partes[0], int(solicitud_partes[1])
                                numero_placa = solicitud_partes[2]

                                # Buscar al investigador
                                current = empleados.first()
                                investigador = None
                                while current:
                                    empleado = current.getData()
                                    if empleado.getId == investigador_id:
                                        investigador = empleado
                                        break
                                    current = current.getNext()

                                if not investigador:
                                    print(f"No se encontró al investigador con ID {investigador_id}.")
                                    continue

                                # Buscar y eliminar el equipo del inventario del investigador
                                current = investigador.inventario.first()
                                encontrado = False
                                while current:
                                    equipo = current.getData()
                                    if equipo["numero_placa"] == numero_placa:
                                        investigador.inventario.remove(current)
                                        print(f"Equipo con placa {numero_placa} eliminado del inventario del investigador {investigador_nombre}.")
                                        encontrado = True
                                        break
                                    current = current.getNext()

                                if not encontrado:
                                    print(f"Equipo con placa {numero_placa} no encontrado en el inventario del investigador.")
                                    continue

                                # Eliminar el equipo del archivo InventarioGeneral.txt
                            try:
                                    with open("InventarioGeneral.txt", "r") as inventario_file:
                                        lineas = inventario_file.readlines()

                                    with open("InventarioGeneral.txt", "w") as inventario_file:
                                        for linea in lineas:
                                            if numero_placa not in linea:
                                                inventario_file.write(linea)

                                    print(f"Equipo con placa {numero_placa} eliminado del Inventario General.")
                            except FileNotFoundError:
                                print(f"Archivo {archivo_solicitud} no encontrado. Operación cancelada.")
                            except ValueError:
                                print("Índice no válido. Operación cancelada.")
                            except Exception as e:
                                print(f"Error al procesar la solicitud: {e}")

                                # Registrar el cambio en el archivo Control_de_cambios.txt
                                administrador.registrar_cambio(
                                    tipo_cambio="Eliminar",
                                    placa=numero_placa,
                                    investigador_id=investigador_id,
                                    estado="Aprobado",
                                    archivo_cambios="Control_de_cambios.txt"
                                )
                                print(f"Solicitud '{solicitud}' aprobada y registrada en el control de cambios.")



                
            elif opcion == "4":
                administrador.agregar_usuario("Practica #1/Empleados.txt", "Practica #1/Password.txt")
            elif opcion == "5":
                administrador.eliminar_usuario("Practica #1/Empleados.txt", "Practica #1/Password.txt")
            elif opcion == "6":
                administrador.modificar_contraseña("Practica #1/Password.txt")
            elif opcion == "7":
                inventario = GestorArchivos.cargar_inventario_general("Practica #1/InventarioGeneral.txt")
                node = inventario.first()
                while node:
                    print(node.getData())
                    node = node.getNext()
            elif opcion == "9":
                archivo = "Control_de_cambios.txt"
                administrador.generar_archivo_control_cambios(archivo)
                print(f"Archivo de control de cambios generado: {archivo}")

            elif opcion == "10":
                cedula_investigador = int(input("Ingrese la cédula del investigador: "))

                # Buscar al investigador por su cédula
                nombre_investigador = None
                current = empleados.first()
                while current:
                    empleado = current.getData()
                    if empleado.getId == cedula_investigador:
                        nombre_investigador = empleado.getNombre.replace(" ", "-")
                        break
                    current = current.getNext()

                if not nombre_investigador:
                    print(f"No se encontró un investigador con la cédula {cedula_investigador}.")
                else:
                    archivo = f"{nombre_investigador}_{cedula_investigador}.txt"
                    administrador.generar_archivo_inventario_investigador(cedula_investigador, archivo, empleados)
                    print(f"Archivo de inventario generado para el investigador {nombre_investigador}: {archivo}")


            elif opcion == "11":
                archivo = "InventarioGeneral.txt"
                administrador.generar_archivo_inventario_general(archivo)
                print(f"Archivo de inventario general generado: {archivo}")

            elif opcion == "12":
                archivo = "Solicitudes_agregar.txt"
                administrador.generar_archivo_solicitudes_pendientes(archivo, tipo="adicionar")
                print(f"Archivo de solicitudes para agregar generado: {archivo}")

            elif opcion == "13":
                archivo = "Solicitudes_eliminar.txt"
                administrador.generar_archivo_solicitudes_pendientes(archivo, tipo="eliminar")
                print(f"Archivo de solicitudes para eliminar generado: {archivo}")

            elif opcion == "14":
                print("Cerrando sesión...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    else:
        print("Rol no reconocido.")


if __name__ == "__main__":
    main()
