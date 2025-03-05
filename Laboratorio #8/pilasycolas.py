from listas import*

class Stack:
    def __init__(self):
        self.data = SimpleList()
    
    def size(self):
        return self.data.size()
    
    def isEmpty(self):
        return self.data.isEmpty()
    
    def push(self, e):
        self.data.addFirst(e)
    
    def pop(self):
        if self.isEmpty():
            raise IndexError("La cola esta vacia")
        return self.data.removeFirst()
    
    def top(self):
        if self.isEmpty():
            raise IndexError("La cola esta vacia")
        return self.data.first().getData()
    
    def print_stack(self):
        """Imprime los elementos de la pila."""
        self.data.printData()




class Queue:
    def __init__(self):
        self.data = SimpleList()

    def size(self):
        return self.data.size()

    def isEmpty(self):
        return self.data.isEmpty()

    def enqueue(self, e):
        self.data.addLast(e)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("La cola está vacía")
        return self.data.removeFirst()

    def first(self):
        if self.isEmpty():
            raise IndexError("La cola está vacía")
        return self.data.first().getData()

    def print_queue(self):
        self.data.printData()


