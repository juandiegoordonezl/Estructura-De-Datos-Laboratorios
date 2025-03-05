from binaryTree import *
class BSTEntry:
    def __init__(self, data, key):
        self.data = data
        self.key = key
    
    def get_data(self):
        #Retorna el dato almacenado.
        return self.data
    
    def get_key(self):
        #Retorna la clave asociada al dato.
        return self.key
    
    def set_data(self, data):
        #Asigna un nuevo valor al dato.
        self.data = data
    
    def set_key(self, key):
        #Asigna un nuevo valor a la clave.
        self.key = key
        
    def __str__(self):  # Agregar este método
        return f"{self.data} (Key: {self.key})"
        
class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()
    
    def find(self, key):
        return self._search_tree(key, self.root)
    
    def _search_tree(self, key, node):
        if node is None:
            return None
        
        entry = node.get_data()
        if key == entry.get_key():
            return node
        elif key < entry.get_key():
            return self._search_tree(key, node.get_left())
        else:
            return self._search_tree(key, node.get_right())
    
    def insert(self, data, key):
        new_entry = BSTEntry(data, key)
        if self.is_empty():
            self.add_root(new_entry)
        else:
            self._add_entry(self.root, new_entry)
    
    def _add_entry(self, node, entry):
        node_entry = node.get_data()
        new_node = Node(entry)
        
        if entry.get_key() < node_entry.get_key():
            if self.has_left(node):
                self._add_entry(node.get_left(), entry)
            else:
                node.set_left(new_node)
                self.size += 1
        else:
            if self.has_right(node):
                self._add_entry(node.get_right(), entry)
            else:
                node.set_right(new_node)
                self.size += 1
    
    def remove(self, key):
        node = self.find(key)
        if node is None:
            return None
        
        entry = node.get_data()
        if self.has_left(node) and self.has_right(node):
            predecessor = self._predecessor(node)
            node.set_data(predecessor.get_data())
            super().remove(predecessor)
        else:
            super().remove(node)
        
        return entry
    
    def _predecessor(self, node):
        temp = node.get_left()
        return self._max_node(temp)
    
    def _max_node(self, node):
        if self.has_right(node):
            return self._max_node(node.get_right())
        return node
    
    def max_value(self):
        if self.is_empty():
            return None
        return self._max_node(self.root).get_data()
    
    def min_value(self):
        if self.is_empty():
            return None
        return self._min_node(self.root).get_data()
    
    def _min_node(self, node):
        if self.has_left(node):
            return self._min_node(node.get_left())
        return node
    
    def inorder_traversal(self):
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node, result):
        if node is not None:
            if self.has_left(node):
                self._inorder(node.get_left(), result)
            result.append(node.get_data().get_key())
            if self.has_right(node):
                self._inorder(node.get_right(), result)
    
    def display(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root
        
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.get_data().get_key()))
            if self.has_left(node):
                self.display(node.get_left(), level + 1, "L-- ")
            if self.has_right(node):
                self.display(node.get_right(), level + 1, "R-- ")
