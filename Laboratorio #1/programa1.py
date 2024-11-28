# Declaración de variables y lista
max_val = 0
min_val = 0
suma = 0
numeros = []

# Intentamos solicitar el número de números enteros a ingresar
while True:
    try:
        n = int(input("Ingrese cuantos números enteros quiere comparar: "))
        break  # Si se ingresó un valor válido, salimos del ciclo
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

# Se inicia un ciclo para recolectar los números solicitados y agregarlos a la lista "numeros"
for x in range(n):
    while True:
        try:
            num = int(input(f"Ingrese el numero #{x + 1}: "))
            numeros.append(num)
            break  # Si el número es válido, salimos del ciclo
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

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
print(f"El valor máximo es {max_val}, el valor mínimo es {min_val}, la suma es {suma} y el promedio de los valores es {promedio}")
