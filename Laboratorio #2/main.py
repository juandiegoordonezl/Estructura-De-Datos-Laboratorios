from direccion import Direccion
class Main:
    @staticmethod
    def run():
        # Crear una instancia de la clase Direccion
        direccion1 = Direccion("Calle 54A", "30-01", "Boston", "Medellín", "Edificio Central", "101")
        
        # Mostrar los atributos del objeto direccion1
        print(direccion1)

# Código principal que llama a la clase Main
if __name__ == "__main__":
    Main.run()