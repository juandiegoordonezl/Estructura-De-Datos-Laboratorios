import string

# Ruta completa del archivo
archivo = r'C:\Users\junid\Documents\GitHub\Estructura-De-Datos-Laboratorios\Laboratorio #1\test_pr2.txt'

# Abrir y leer el contenido del archivo
with open(archivo, 'r', encoding='utf-8') as f:
    contenido = f.read()

# Convertir el contenido a minúsculas para contar sin distinguir mayúsculas
contenido = contenido.lower()

# Eliminar signos de puntuación del texto
for signo in string.punctuation:
    contenido = contenido.replace(signo, "")

# Dividir el texto en palabras
palabras = contenido.split()

# Contar las apariciones de la palabra "en"
conteo_en = palabras.count("no")

# Mostrar el resultado
print(f"La palabra 'en' se repite {conteo_en} veces en el archivo.")
