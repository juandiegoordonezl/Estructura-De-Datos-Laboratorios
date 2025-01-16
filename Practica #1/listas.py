
class DoubleNode:
    def __init__(self, data = None):
        self.data = data
        self._next = None
        self._prev = None
        
    # Getters and setters
    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data
    
    def getNext(self):
        return self._next
    
    def getPrev(self):
        return self._prev
        
    def setNext(self, nextNode):
        self._next = nextNode
        
    def setPrev(self, prev):
        self._prev = prev

class DoubleList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    def size(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    def first(self):
        return self._head
    def last(self):
        return self._tail
    
    def addFirst(self, data):
        node = DoubleNode(data)
        node.setNext(self._head)        
        if self.isEmpty():
            self._tail = node
        else:
            self._head.setPrev(node)
        self._head = node
        self._size += 1
        pass
    
    def addLast(self, data):
        node = DoubleNode(data)
        if self.isEmpty():
            self._head = node
        else:
            node.setPrev(self._tail)
            self._tail.setNext(node)
        self._tail = node
        self._size += 1
        pass
        
    def removeFirst(self):
        data = self._head.getData()
        self._head = self._head.getNext()
        self._head.setPrev(None)
        self._size -= 1
        return data
    
    def removeLast(self):
        data = self._tail.getData()
        self._tail = self._tail.getPrev()
        self._tail.setNext(None)
        self._size -= 1
        return data

    def remove(self, node):
        data = node.getData()

        prev = node.getPrev()
        nextNode = node.getNext()
        prev.setNext(nextNode)
        nextNode.setPrev(prev)

        self._size -= 1
        return data
        
    def addAfter(self, node, data):
        newNode = DoubleNode(data)
        newNode.setPrev(node)
        newNode.setNext(node.getNext())

        node.getNext().setPrev(newNode)
        node.setNext(newNode)
        self._size += 1
        pass

    def addBefore(self, node, data):
        newNode = DoubleNode(data)

        newNode.setNext(node)
        newNode.setPrev(node.getPrev())

        node.getPrev().setNext(newNode)
        node.setPrev(newNode)
        self._size += 1
        pass

    def printData(self):
        node = self._head
        while node != None:
            print(node.getData())
            node = node.getNext()
        pass
    
    def _split(self, head):
        """
        Divide la lista a partir del nodo `head` en dos mitades.
        Retorna el inicio de la segunda mitad.
        """
        slow = head
        fast = head.getNext()

        while fast and fast.getNext():
            slow = slow.getNext()
            fast = fast.getNext().getNext()

        mid = slow.getNext()
        slow.setNext(None)  # Divide la lista
        if mid:
            mid.setPrev(None)
        return mid

    def _merge(self, left, right, key):
        """
        Fusiona dos sublistas ordenadas según la función `key`.
        Retorna el nuevo inicio de la lista fusionada.
        """
        dummy = DoubleNode()  # Nodo temporal para facilitar la fusión
        tail = dummy

        while left and right:
            if key(left.getData()) <= key(right.getData()):  # Comparar según la función clave
                tail.setNext(left)
                left.setPrev(tail)
                left = left.getNext()
            else:
                tail.setNext(right)
                right.setPrev(tail)
                right = right.getNext()
            tail = tail.getNext()

        # Conectar cualquier nodo restante
        if left:
            tail.setNext(left)
            left.setPrev(tail)
        if right:
            tail.setNext(right)
            right.setPrev(tail)

        return dummy.getNext()

    def _mergeSort(self, head, key):
        """
        Ordena la lista usando el algoritmo de Merge Sort y la función `key`.
        Retorna el nuevo inicio de la lista ordenada.
        """
        if not head or not head.getNext():  # Caso base
            return head

        mid = self._split(head)

        # Dividir y conquistar
        left = self._mergeSort(head, key)
        right = self._mergeSort(mid, key)

        return self._merge(left, right, key)

    def sort(self, key=lambda x: x):
        """
        Método público para ordenar la lista usando Merge Sort con una función `key`.
        Actualiza `_head` y `_tail` después de ordenar.
        """
        if not self._head or not self._head.getNext():
            return  # Lista vacía o con un solo elemento no necesita ordenarse

        self._head = self._mergeSort(self._head, key)

        # Actualizar el tail después de ordenar
        current = self._head
        while current.getNext():
            current = current.getNext()
        self._tail = current