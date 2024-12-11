class NodoDoble:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        pass


class ListaDoble:

    def __init__(self):
        self.first = None
        self.last = None


    def recorrer(self):
        nodoActual = self.first
        while nodoActual != None:
            print(nodoActual.data)
            nodoActual = nodoActual.next

    def addFirst(self, nuevoNodo):
        self.first.prev = nuevoNodo
        nuevoNodo.next = self.first
        self.first = nuevoNodo

    def addLast(self, nuevoNodo):
        self.last.next = nuevoNodo
        nuevoNodo.prev = self.last
        self.last = nuevoNodo

    def removeFirst(self):
        segundo = self.first.next
        segundo.prev = None
        self.first.next = None
        
        self.first = segundo

    
    def removeLast(self):
        penultimo = self.last.prev

        self.last.prev = None
        penultimo.next = None

        self.last = penultimo

    
    def remove(self, nodoObjetivo):

        datos = nodoObjetivo.data

        anterior = nodoObjetivo.prev
        siguiente = nodoObjetivo.next

        anterior.next = siguiente
        siguiente.prev = anterior
        
        return datos