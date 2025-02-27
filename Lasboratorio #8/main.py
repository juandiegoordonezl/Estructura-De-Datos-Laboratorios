from binarySearchTree import *

class User:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
        self.key = self.calculate_key()
    
    def calculate_key(self):
        return sum(int(digit) for digit in str(self.id_number))
    
    def __str__(self):
        return f"{self.name} (ID: {self.id_number}, Key: {self.key})"

# Crear el árbol binario de búsqueda
bst = BinarySearchTree()

# Lista de usuarios
users = [
    User("Juan", 10101013),
    User("Pablo", 10001011),
    User("Maria", 10101015),
    User("Ana", 1010000),
    User("Diana", 10111105),
    User("Mateo", 10110005)
]

# Insertar usuarios en el ABB
for user in users:
    bst.insert(user, user.key)

# Mostrar el árbol
print("\nÁrbol Binario de Búsqueda:")
bst.display()

# Prueba de búsqueda
print("\nBuscando clave 7 (Juan):", str(bst.find(7).get_data()) if bst.find(7) else "No encontrado")
print("Buscando clave 4 (Pablo):", str(bst.find(4).get_data()) if bst.find(4) else "No encontrado")

# Prueba de eliminación
print("\nEliminando clave 7 (Juan)")
bst.remove(7)
bst.display()

# Prueba de valores mínimos y máximos
print("\nValor mínimo:", bst.min_value().get_data() if bst.min_value() else "Árbol vacío")
print("Valor máximo:", bst.max_value().get_data() if bst.max_value() else "Árbol vacío")

# Prueba de recorrido inorder
print("\nRecorrido Inorder:", [str(node) for node in bst.inorder_traversal()])
