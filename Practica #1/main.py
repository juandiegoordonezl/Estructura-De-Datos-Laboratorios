from gestorArchivos import GestorArchivos
from autenticacion import Autenticacion
from investigador import Investigador
from administrador import Administrador
from fecha import *

def main():
    # Cargar datos iniciales
    empleados = GestorArchivos.cargar_empleados("Practica #1/Empleados.txt")
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
                investigador.consultar_inventario()
            elif opcion == "2":
                nombre = input("Ingrese el nombre del equipo: ")
                placa = input("Ingrese la placa del equipo: ")
                fecha_compra = Fecha(*map(int, input("Ingrese la fecha de compra (dd/mm/aaaa): ").split("/")))
                valor = float(input("Ingrese el valor del equipo: "))
                investigador.solicitar_agregar_equipo(nombre, placa, fecha_compra, valor)
            elif opcion == "3":
                placa = input("Ingrese la placa del equipo a eliminar: ")
                justificacion = input("Ingrese la justificación para eliminar el equipo: ")
                investigador.solicitar_eliminar_equipo(placa, justificacion)
            elif opcion == "4":
                investigador.consultar_estado_solicitudes()
            elif opcion == "5":
                investigador.generar_archivo_inventario()
            elif opcion == "6":
                investigador.generar_archivo_solicitudes()
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
            print("1. Consultar solicitudes")
            print("2. Procesar solicitud")
            print("3. Agregar usuario")
            print("4. Eliminar usuario")
            print("5. Cambiar contraseñas")
            print("6. Cargar control de cambios")
            print("7. Generar archivo de control de cambios")
            print("8. Generar archivo de solicitudes para agregar")
            print("9. Generar archivo de solicitudes para eliminar")
            print("10. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                administrador.consultar_solicitudes()
            elif opcion == "2":
                administrador.consultar_solicitudes()
                indice = int(input("Seleccione el índice de la solicitud a procesar: "))
                aprobado = input("¿Aprobar la solicitud? (s/n): ").lower() == "s"
                current = administrador.solicitudes_pendientes.first()
                for _ in range(indice):
                    current = current.getNext()
                administrador.procesar_solicitud(current.getData(), aprobado)
            elif opcion == "3":
                administrador.agregar_usuario()
            elif opcion == "4":
                administrador.eliminar_usuario()
            elif opcion == "5":
                administrador.cambiar_contraseñas()
            elif opcion == "6":
                archivo = input("Ingrese el nombre del archivo para cargar: ")
                administrador.cargar_control_cambios(archivo)
            elif opcion == "7":
                archivo = input("Ingrese el nombre del archivo para guardar: ")
                administrador.guardar_control_cambios(archivo)
            elif opcion == "8":
                administrador.generar_archivo_solicitudes_agregar()
            elif opcion == "9":
                administrador.generar_archivo_solicitudes_eliminar()
            elif opcion == "10":
                print("Cerrando sesión...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    else:
        print("Rol no reconocido.")

if __name__ == "__main__":
    main()
