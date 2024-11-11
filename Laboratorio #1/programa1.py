# Declaración de variables y lista
max_val = 0
min_val = 0
suma = 0
numeros = []

# Se pide el número de números enteros a ingresar y se castea a entero
n = int(input("Ingrese cuantos números enteros quiere comparar: "))

# Se inicia un ciclo para recolectar los números solicitados y agregarlos a la lista "numeros"
for x in range(n):
    num = int(input(f"Ingrese el numero #{x + 1}: "))
    numeros.append(num)

# Inicializa max y min al primer valor de la lista
max_val = numeros[0]
min_val = numeros[0]

# Calcula el valor máximo, mínimo y la suma
for y in numeros:
    if y > max_val:
        max_val = y
    if y < min_val:
        min_val = y
    suma += y

# Calcula el promedio
promedio = suma / len(numeros)

# Imprime los resultados
print(f"El valor máximo es {max_val}, el valor mínimo es {min_val}, la suma es {suma} y el promedio de los valores es {promedio:.2f}")
