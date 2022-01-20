"""
********* ARCHIVOS **********
"""

"""
Abrir y leer
"""
print("ABRIR Y LEER")
print("*" * 10)

# Abrir un archivo que sabemos que existe
archivo = open("prueba.txt")  # Al estar en el mismo path que este archivo, es la ruta por defecto
print(archivo.read())  # Nos lee el archivo entero
print(archivo.readline())  # Lee por líneas cada vez que se llama el método
print(archivo.readline())  # Lee por líneas cada vez que se llama el método
print(archivo.readline())  # Lee por líneas cada vez que se llama el método

# SIEMPRE VAMOS A CERRAR EL ARCHIVO para vaciar buffer y ahorrar almacenamiento
archivo.close()

# O bien realizar iteración
archivo = open("prueba.txt")  # Al estar en el mismo path que este archivo, es la ruta por defecto

for linea in archivo:
    print(linea)  # Al haber un salto de línea al final de cada frase, se imprimirán las líneas separadas por \n

archivo.close()

archivo = open("prueba.txt")
for linea in archivo:
    print(linea.lstrip())  # Al añadir lstrip, elimina el salto de línea

# SIEMPRE VAMOS A CERRAR EL ARCHIVO para vaciar buffer y ahorrar almacenamiento
archivo.close()

# se pueden leer todas las líneas y se almacenarán en una lista
archivo = open("prueba.txt")  # Al estar en el mismo path que este archivo, es la ruta por defecto
print(archivo.readlines())
archivo.close()

"""
crear y modificar
"""
print("CREAR Y MODIFICAR")
print("*" * 10)
# Con open podemos indicar el tipo de apertura
# 'r' [tipo por defecto] = solo lee
# 'w' = el archivo se abre para solo escritura (vacía el archivo si ya existe)
# 'a' = el archivo se abre para escritura y si existe contenido, se posiciona al final del contenido ya existente

archivo = open("prueba.txt", 'w')
archivo.write("Soy un nuevo texto.\nSoy un nuevo texto x2")
# No nos dejará leerlo, debemos cerrarlo
archivo.close()
archivo = open("prueba.txt", 'r')
print(archivo.read())
archivo.close()

archivo = open("prueba.txt", 'a')

# Con writelines, nos escribirá los strings de la lista que le pasemos a la función
# ¡OJO! que los concatena
archivo.writelines(["Hola ", "soy ", "la ", "tercera línea"])
archivo.close()

"""
Directorios
"""

print("DIRECTORIOS")
print("*" * 10)

# Para evitar problemas con las rutas, deberemos importar path y usaremos "os"

import os

##get current working directory
ruta = os.getcwd()
print(ruta)

# change directory
os.chdir("C:\\Users\\Shaila Gibert\\IdeaProjects\\PythonCourse1\\Day6_ruta_alternativa_textos")

# al cambiar el directorio de trabajo, podemos abrir archivos que estén en ese directorio
archivo = open("texto.txt")
print(archivo.read())
archivo.close()

# crea una carpeta no existente dentro de la ruta que tú indicas
os.makedirs("C:\\Users\\Shaila Gibert\\IdeaProjects\\PythonCourse1\\Day6_ruta_alternativa_textos\\carpeta_nueva")

ruta = "C:\\Users\\Shaila Gibert\\IdeaProjects\\PythonCourse1\\Day6_ruta_alternativa_textos\\texto.txt"

# si indicamos el archivo con su ruta, con os.basename nos saca el nombre de base del elemento
print(os.path.basename(ruta))
# Con dirname nos da la ruta SIN el nombre del elemento de la ruta
print(os.path.dirname(ruta))
# con split, nos separará la ruta en el nombre base del elemento y en la ruta donde se encuentre
print(os.path.split(ruta))

##ELIMINAR CARPETAS
os.rmdir(
    "carpeta_nueva")  # No hace falta poner la ruta entera dado que con chdir ya hemos cambiado el directorio de trabajo

# ***************************************************************************************************************
"""
PATHLIB
"""

print("PATHLIB")
print("*" * 10)

# Nos permite manipular rutas de sistemas de archivos

from pathlib import Path, PureWindowsPath  # ES UN OBJETO

ruta = Path("C:/Users/Shaila Gibert/IdeaProjects/PythonCourse1/Day6")

ruta_con_archivo = ruta / 'prueba.txt'
archivo = open(ruta_con_archivo)
print(archivo.read())
archivo.close()

# Al usar Path, podemos usar:
ruta = Path("C:/Users/Shaila Gibert/IdeaProjects/PythonCourse1/Day6/prueba.txt")
print(ruta.read_text())  # No es necesario abrir el texto ni cerrarlo
print(ruta.name)  # Nombre del archivo
print(ruta.suffix)  # tipo de elemento, en este caso .txt
print(ruta.stem)  # nombre del archivo SIN el sufijo

if ruta.exists():  # Nos permite ver si el archivo existe
    print("El archivo existe")
else:
    print("El archivo no existe")

##PureWindowsPath transforma la ruta que se pasa por Path a un tipo de ruta de Windows

ruta_en_windows = PureWindowsPath(ruta)
print(ruta_en_windows)
ruta_resolved = ruta.resolve()
print(ruta_resolved)

# *******************************************************************************

# PATH
# es capaz de crear un directorio dados uns string
base = Path.home()  # Ruta absoluta del usuario actual
ruta_prueba = Path(base, "Shaila", "Gibert", "Marco")
print(ruta_prueba)

# podemos crear una ruta de una ruta ya existente
ruta2 = ruta_prueba.with_name("SeCambiaLaRuta")
print(ruta2)
# Parent nos trae el antecesor de la ruta
print(ruta.parent)
print(ruta_prueba.parent.parent.parent)

# Con Glob indicados los archivos existentes en un directorio
ruta = Path(Path(os.getcwd()))
print(ruta)
for txt in Path(ruta).glob("**/*.txt"):  # Con ** indicamos que busque también dentro
    # de los directorios dentro de la ruta
    print(txt)

# Con relative podemos partir de una parte de una ruta
ruta_relativa = ruta.relative_to(Path(base, "IdeaProjects", "PythonCourse1"))  # #Al ser la otra ruta absoluta, esta
# también debe serlo
print(ruta_relativa)

ruta_relativa = ruta.relative_to(Path(base, "IdeaProjects"))
print(ruta_relativa)

"""
LIMPIAR CONSOLA
"""
print("LIMPIAR CONSOLA")
print("*" * 10)

# Sólo funciona en el IDE PyCharm
from os import system

print("Primera linea antes de limpiar")
print("Segunda linea antes de limpiar")
input("Aprieta intro para limpiar: ")
system('cls')  # cls para Windows
print("Hemos limpiado la consola")
# para que funcione tendremos que cambiar la configuración del proyecto en PyCharm
