from listas import *
from pilasycolas import *
class Node:
    def __init__(self, data=None):

       #param data: Valor del nodo (puede ser cualquier objeto).
   
        self.data = data
        self.left = None
        self.right = None
    
    def get_left(self):
        #Retorna el nodo izquierdo.
        return self.left
    
    def get_right(self):
        #Retorna el nodo derecho.
        return self.right
    
    def get_data(self):
        #Retorna el dato almacenado en el nodo.
        return self.data
    
    def set_left(self, node):
        #Asigna un nodo al hijo izquierdo.
        self.left = node
    
    def set_right(self, node):
        #Asigna un nodo al hijo derecho.
        self.right = node
    
    def set_data(self, data):
        #Asigna un nuevo valor al nodo.
        self.data = data
        
        
class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def is_root(self, node):
        return node == self.root
    
    def is_internal(self, node):
        return self.has_left(node) or self.has_right(node)
    
    def has_left(self, node):
        return node.get_left() is not None
    
    def has_right(self, node):
        return node.get_right() is not None
    
    def get_root(self):
        return self.root
    
    def get_left(self, node):
        return node.get_left()
    
    def get_right(self, node):
        return node.get_right()
    
    def add_root(self, data):
        if self.root is None:
            self.root = Node(data)
            self.size = 1
        else:
            raise Exception("El árbol ya tiene una raíz")
    
    def insert_left(self, node, data):
        if node.get_left() is None:
            node.set_left(Node(data))
            self.size += 1
        else:
            raise Exception("El nodo ya tiene un hijo izquierdo")
    
    def insert_right(self, node, data):
        if node.get_right() is None:
            node.set_right(Node(data))
            self.size += 1
        else:
            raise Exception("El nodo ya tiene un hijo derecho")
    
    def parent(self, node):
        if self.is_root(node):
            return None
        
        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            if temp.get_left() == node or temp.get_right() == node:
                return temp
            if self.has_left(temp):
                queue.append(temp.get_left())
            if self.has_right(temp):
                queue.append(temp.get_right())
        return None
    
    def depth(self, node):
        if self.is_root(node):
            return 0
        return 1 + self.depth(self.parent(node))
    
    def height(self, node):
        if not self.is_internal(node):
            return 0
        return 1 + max(self.height(self.get_left(node)), self.height(self.get_right(node)))
    
    def remove(self, node):
        parent_node = self.parent(node)
        if self.has_left(node) or self.has_right(node):
            child = node.get_left() if self.has_left(node) else node.get_right()
            if parent_node:
                if parent_node.get_left() == node:
                    parent_node.set_left(child)
                else:
                    parent_node.set_right(child)
        else:
            if parent_node:
                if parent_node.get_left() == node:
                    parent_node.set_left(None)
                else:
                    parent_node.set_right(None)
        self.size -= 1
