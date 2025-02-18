import random
from listas import SimpleList, SimpleNode, DoubleNode
from usuario import Usuario
from fecha import Fecha
from direccion import Direccion
from pilasycolas import*


# Main para probar los problemas
if __name__ == "__main__":
    # Problema 1: Prueba de Stack
    print("---- PROBLEMA 1: PILA ----")
    stack = Stack()
    for num in [2, 4, 6, 8, 10]:
        stack.push(num)

    print("Elementos en la pila:")
    stack.print_stack()

    print("\nExtrayendo elementos con pop():")
    while not stack.isEmpty():
        print(stack.pop())

    # Problema 2: Prueba de Queue
    print("\n---- PROBLEMA 2: COLA ----")
    queue = Queue()
    for num in [2, 4, 6, 8, 10]:
        queue.enqueue(num)

    print("Elementos en la cola:")
    queue.print_queue()

    print("\nExtrayendo elementos con dequeue():")
    while not queue.isEmpty():
        print(queue.dequeue())
