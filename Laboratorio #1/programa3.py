usuarios = {
    "Juan1223": "J12an*.",
    "Maria2345": "M23a*.",
    "Pablo1459": "P14o*.",
    "Ana3456": "A34a*."
}

intentos = 0  # Variable para contar los intentos fallidos
max_intentos = 3  # Límite de intentos

while intentos < max_intentos:
    print("Programa de control de acceso (╹ڡ╹ )")
    usuario = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")

    if usuario in usuarios and usuarios[usuario] == password:
        print("Acceso permitido")
        break  # Sale del ciclo si el acceso es correcto
    else:
        print("Datos incorrectos")
        intentos += 1  # Aumenta el contador de intentos fallidos
    
    if intentos == max_intentos:
        print("Lo siento, su acceso no es permitido")
