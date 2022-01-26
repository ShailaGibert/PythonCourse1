"""
--- COMPRIMIR Y DESCOMPRIMIR ARCHIVOS ---
"""

# Usaremos zipfile y shutil
import shutil
import zipfile

# Pasamos primero el archivo en el que se guardarán los archivos comprimidos
from pathlib import PureWindowsPath

mi_zip = zipfile.ZipFile("mi_archivo_comprimido.zip", "w")
# Indicamos el archivo que queremos comprimir y añadir en el archivo comprimido
mi_zip.write("archivo_a_comprimir.txt")
mi_zip.close()

#Para descomprimir
zip_abierto = zipfile.ZipFile("mi_archivo_comprimido.zip", 'r')
# Extraemos todos los archivos dentro del archivo comprimido
zip_abierto.extractall()
zip_abierto.close()


'''
HACIÉNDOLO CON SHUTIL
'''
# Indicaremos la ruta del archivo que queremos comprimir
carpeta_origen = 'C:\\Users\Shaila Gibert\IdeaProjects\PythonCourse1\Day9\Theory\Carpeta_a_comprimir'
carpeta_origen = PureWindowsPath(carpeta_origen)
carpeta_destino = "Todo_comprimido"

# Shutil crea un archivo con la extensión que le pasamos, en este caso .zip
shutil.make_archive(carpeta_destino, "zip", carpeta_origen)

# Para descomprimir
shutil.unpack_archive(carpeta_destino+".zip", "Carpeta_descomprimida_shutil", "zip")



