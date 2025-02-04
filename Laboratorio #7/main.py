from heap import *
from priorityQueue import*

import random

# Crear un arreglo de enteros aleatorios
random_numbers = [random.randint(1, 100) for _ in range(20)]

# Prueba de MAX-HEAP
heap = HEAP(20)
heap.build_max_heap(random_numbers)
print("MAX-HEAP construido:", heap.A)

# Prueba de PriorityQueue
pq = PriorityQueue(20)
for num in random_numbers:
    pq.max_heap_insert(num)

print("Máximo en la cola de prioridad:", pq.heap_maximum())
print("Extrayendo máximos de la cola de prioridad:")
while pq.size > 0:
    print(pq.heap_extract_max(), end=" ")
