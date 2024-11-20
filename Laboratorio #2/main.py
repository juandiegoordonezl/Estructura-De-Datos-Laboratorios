from direccion import *
from fecha import *
class Main:
  
    if __name__ == "__main__":
        fecha1 = Fecha(20,11,2024)
        print(f"{fecha1.get_Dia} / {fecha1.get_Mes} / {fecha1.get_A}")
        
        direccion1 = Direccion("Calle 54A", "30-01", "Boston", "Medellín", "Edificio Central", "101")
        print(direccion1)