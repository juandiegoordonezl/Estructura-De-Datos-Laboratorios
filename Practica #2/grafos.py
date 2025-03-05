import csv
import numpy as np

class Grafo:
    def __init__(self, archivo):
        """Inicializa el grafo cargando datos desde un archivo CSV."""
        self.ciudades = []  # Lista de ciudades
        self.indices = {}  # Diccionario para mapear ciudades a índices en la matriz
        self.matriz_km = None  # Matriz de adyacencia para distancias en km
        self.matriz_min = None  # Matriz de adyacencia para tiempos en minutos
        self.cargar_datos(archivo)  # Llamamos al método para cargar los datos
    
    def cargar_datos(self, archivo):
        """Carga los datos del archivo CSV y los traduce a una matriz de adyacencia."""
        with open(archivo, newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)  # Saltamos la cabecera
            datos = list(reader)
            
            # Obtener lista única de ciudades
            ciudades = set()
            for fila in datos:
                ciudades.add(fila[0].strip())
                ciudades.add(fila[1].strip())
            
            # Ordenamos las ciudades para mantener un orden consistente en la matriz
            self.ciudades = sorted(ciudades)
            self.indices = {ciudad: i for i, ciudad in enumerate(self.ciudades)}
            
            # Creamos matrices de adyacencia con infinito como valor inicial
            n = len(self.ciudades)
            self.matriz_km = np.full((n, n), np.inf)
            self.matriz_min = np.full((n, n), np.inf)
            np.fill_diagonal(self.matriz_km, 0)  # Distancia de una ciudad a sí misma es 0
            np.fill_diagonal(self.matriz_min, 0)  # Tiempo de una ciudad a sí misma es 0
            
            # Rellenamos la matriz con los datos del archivo
            for fila in datos:
                ciudad1, ciudad2, km, minutos = fila[0].strip(), fila[1].strip(), int(fila[2]), int(fila[3])
                i, j = self.indices[ciudad1], self.indices[ciudad2]
                self.matriz_km[i][j] = self.matriz_km[j][i] = km  # Grafo no dirigido
                self.matriz_min[i][j] = self.matriz_min[j][i] = minutos  # Grafo no dirigido
    
    def estan_conectadas(self, ciudad1, ciudad2):
        """Verifica si dos ciudades están conectadas por una carretera directa."""
        if ciudad1 in self.indices and ciudad2 in self.indices:
            i, j = self.indices[ciudad1], self.indices[ciudad2]
            return self.matriz_km[i][j] != np.inf  # Si hay un valor distinto de infinito, hay conexión
        return False  # Alguna de las ciudades no existe en el grafo
    
    def dijkstra(self, origen, destino, por_tiempo=False):
        """Implementa el algoritmo de Dijkstra para encontrar el camino más corto entre dos ciudades."""
        if origen not in self.indices or destino not in self.indices:
            return None, np.inf  # Si una de las ciudades no está, retornamos None
        
        n = len(self.ciudades)
        matriz = self.matriz_min if por_tiempo else self.matriz_km  # Elegimos la matriz según la opción
        
        # Inicializamos estructuras de Dijkstra
        dist = np.full(n, np.inf)  # Distancias iniciales en infinito
        dist[self.indices[origen]] = 0  # La distancia desde el origen es 0
        visitado = np.full(n, False)  # Para marcar los nodos visitados
        anterior = [None] * n  # Para reconstruir el camino
        
        for _ in range(n):
            # Seleccionar el nodo no visitado con la menor distancia
            u = np.argmin(np.where(visitado, np.inf, dist))
            if dist[u] == np.inf:
                break  # Si no hay más nodos alcanzables, terminamos
            visitado[u] = True  # Marcamos el nodo como visitado
            
            # Relajamos las aristas adyacentes
            for v in range(n):
                if matriz[u][v] != np.inf and not visitado[v]:  # Solo si hay conexión y no está visitado
                    nueva_dist = dist[u] + matriz[u][v]
                    if nueva_dist < dist[v]:  # Si encontramos una ruta más corta, actualizamos
                        dist[v] = nueva_dist
                        anterior[v] = u  # Guardamos el nodo anterior en el camino óptimo
        
        # Reconstrucción del camino
        camino, actual = [], self.indices[destino]
        while actual is not None:
            camino.insert(0, self.ciudades[actual])  # Agregamos la ciudad al camino
            actual = anterior[actual]  # Seguimos hacia atrás en el camino óptimo
        
        return camino if camino[0] == origen else None, dist[self.indices[destino]]  # Retornamos el camino y la distancia