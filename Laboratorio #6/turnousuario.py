from usuario import Usuario
from pilasycolas import Stack, Queue

class TurnoUsuario:
    def __init__(self):
        self.registro = Queue()
        self.usuarioAtendidos = Stack()

    def registrar(self, usuario: Usuario):
        self.registro.enqueue(usuario)

    def atenderSiguiente(self):
        if self.registro.isEmpty():
            print("No hay usuarios en la cola.")
            return None
        usuario = self.registro.dequeue()
        self.usuarioAtendidos.push(usuario)
        return usuario

    def toFile(self):
        with open("usuariospendientes.txt", "w") as pendientes:
            temp_queue = Queue()
            while not self.registro.isEmpty():
                usuario = self.registro.dequeue()
                pendientes.write(f"{usuario.getNombre()} {usuario.getId()}\n")
                temp_queue.enqueue(usuario)
            self.registro = temp_queue
        
        with open("usuariosatendidos.txt", "w") as atendidos:
            temp_stack = Stack()
            while not self.usuarioAtendidos.isEmpty():
                usuario = self.usuarioAtendidos.pop()
                atendidos.write(f"{usuario.getNombre()} {usuario.getId()}\n")
                temp_stack.push(usuario)
            self.usuarioAtendidos = temp_stack
