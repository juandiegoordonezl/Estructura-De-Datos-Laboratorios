from grafos import *
class main:
    if __name__ == "__main__":
        archivo_csv = "Practica #2\Datos vias.csv"
        grafo = Grafo(archivo_csv)
        print(grafo.ciudades)
        
        while True:
            print("\nOpciones:")
            print("1. Verificar si dos ciudades están conectadas")
            print("2. Encontrar el camino más corto en KM")
            print("3. Encontrar el camino más corto en Minutos")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                ciudad1 = input("Ingrese la primera ciudad: ").strip()
                ciudad2 = input("Ingrese la segunda ciudad: ").strip()
                if grafo.estan_conectadas(ciudad1, ciudad2):
                    print(f"Sí, {ciudad1} y {ciudad2} están conectadas por una carretera.")
                else:
                    print(f"No, {ciudad1} y {ciudad2} NO están conectadas por una carretera.")
            
            elif opcion == "2":
                ciudad1 = input("Ingrese la ciudad de origen: ").strip()
                ciudad2 = input("Ingrese la ciudad de destino: ").strip()
                camino, distancia = grafo.dijkstra(ciudad1, ciudad2, por_tiempo=False)
                if camino:
                    print(f"Camino más corto en KM: {' -> '.join(camino)} (Distancia: {distancia} km)")
                else:
                    print("No hay conexión entre las ciudades.")
            
            elif opcion == "3":
                ciudad1 = input("Ingrese la ciudad de origen: ").strip()
                ciudad2 = input("Ingrese la ciudad de destino: ").strip()
                camino, tiempo = grafo.dijkstra(ciudad1, ciudad2, por_tiempo=True)
                if camino:
                    print(f"Camino más corto en Minutos: {' -> '.join(camino)} (Tiempo: {tiempo} minutos)")
                else:
                    print("No hay conexión entre las ciudades.")
            
            elif opcion == "4":
                print("Saliendo del programa...")
                break
            
            else:
                print("Opción inválida. Intente de nuevo.")
