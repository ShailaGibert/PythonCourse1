"""
---- SHUTIL ---
"""

# Creamos un archivo de texto
import os
import shutil
from pathlib import Path

import send2trash

archivo = open("texto_de_prueba.txt", "w")

archivo.close()

# Con shutil podemos moverlo
shutil.move("texto_de_prueba.txt", Path.home())

# Eliminar archivos con shutil
# con OS podemos eliminar archivos con unlink
# con OS podemos eliminar repositorios vacíos con rmdir

# Con shutil podemos eliminar lo que se encuentra con un repositorio con rmtree
# ¡OJO! con rmtree perdemos todos los archivos sin posibilidad de recuperarlos

# Para evitarlo y que los archivos vayan a la papelera, instalaremos el módulo send2trash
send2trash.send2trash(f"{Path.home()}\\texto_de_prueba.txt")

# Con os.walk recorre un directorio y muestra los elementos dentro de él
ruta = Path.home()

# Walk mostrará en tuplas la siguiente información: ruta, subcarpetas y archivos
for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"La carpeta padre es {Path(carpeta).stem}")
    print("Las subcarpetas son:")
    # Iteramos para que nos muestra todas las subcarpetas que encuentre dentro de cada carpeta
    for sub in subcarpeta:
        print(f"\t{sub}")
    print("Los archivos son:")

    # Iteramos para que nos muestre los archivos que encuentre dentro de cada carpeta
    for arch in archivo:
        print(f"\t{arch}")
