from heap import *
from priorityQueue import*

import random

# Crear un arreglo de enteros aleatorios
random_numbers = [random.randint(1, 100) for _ in range(5)]

# Prueba de MAX-HEAP
heap = HEAP(5)
heap.build_max_heap(random_numbers)
print("MAX-HEAP construido:", heap.A)

# Prueba de PriorityQueue
pq = PriorityQueue(5)
for num in random_numbers:
    pq.max_heap_insert(num)
print("Máximo en la cola de prioridad:", pq.heap_maximum())
print("Extrayendo máximos de la cola de prioridad:")
while pq.size > 0:
    print(pq.heap_extract_max(), end=" ")

def test_heap_sort():
    # Generar 5 números aleatorios
    random_numbers = [random.randint(1, 100) for _ in range(5)]
    print("Arreglo original:", random_numbers)
    
    # Crear una instancia del HEAP y ordenar
    heap = HEAP(len(random_numbers))
    heap.build_max_heap(random_numbers)
    sorted_array = heap.heap_sort()
    
    # Imprimir el resultado ordenado
    print("Arreglo ordenado:", sorted_array)

# Ejecutar la prueba
test_heap_sort()