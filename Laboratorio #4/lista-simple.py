class NodoSimple:
    def __init__(self, nombreInicial):
        self.data = nombreInicial
        self.next = None
        pass

class ListaSimple:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
        pass

    def removeFirst(self):
        self.first = self.first.enlace
        self.size -= 1
        pass

    def removeLast(self):

        nodoActual = self.first
        while nodoActual != None:
            
            if nodoActual.enlace == self.last:
                datosLast = self.last.data

                nodoActual.enlace = None
                self.last = nodoActual
                self.size -= 1
                return datosLast

            nodoActual = nodoActual.enlace

    def addLast(self, nuevoNodo):
        if self.size == 0:
            self.first = nuevoNodo
            self.last = nuevoNodo
            self.size += 1
            return

        self.last.enlace = nuevoNodo
        self.last = nuevoNodo


    def addAfter(self, nodoObjetivo, nuevoNodo):
        nodoActual = self.first
        while nodoActual != None:

            if nodoActual == nodoObjetivo:
                siguiente = nodoObjetivo.enlace
                nodoObjetivo.enlace = nuevoNodo
                nuevoNodo.enlace = siguiente
                return

            nodoActual = nodoActual.enlace


    def addFirst(self, nuevoNodo):
        if self.first == None:
            self.first = nuevoNodo
            self.last = nuevoNodo
            return

        nuevoNodo.enlace = self.first
        self.first = nuevoNodo
        pass

    def recorrer(self):
        nodoActual = self.first
        while nodoActual != None:
            print(nodoActual.nombre)
            nodoActual = nodoActual.enlace


