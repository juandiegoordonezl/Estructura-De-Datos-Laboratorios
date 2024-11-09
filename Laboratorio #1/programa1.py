"""Variables, expresiones y estructuras de control: 
Diseñe un programa que le pida al usuario ingresar n números enteros, donde n también es ingresado por el usuario. 
El programa debe calcular: 
(i) el valor máximo, (ii) el valor mínimo, (iii) la suma de los enteros ingresados y (iv) el valor promedio."""

#Declaración de variables y lista
max=0
min=0
promedio=0
numeros=[]

#Se pide el número de números enteros a ingresar y se castea a entero
n=int(input("Ingrese cuantos números enteros quiere comparar: "))

#Se inicia unn ciclo para recolectar los números solicitados y agregarlos a la lista "numeros"
for x in range(0,n,1):
    N=int(input(f"Ingrese el numero #{x+1}: "))
    numeros.append(N)
    
max=numeros[0]
min=numeros[0]

for y in numeros:
    
    if y>max:
        max=y
    elif min>y:
        min=y
    
    promedio=promedio+y

print(f"El valor maximo es {max}, el valor minimo es {min} y el promedio de los valores es {promedio/len(numeros)}")
        
    

    