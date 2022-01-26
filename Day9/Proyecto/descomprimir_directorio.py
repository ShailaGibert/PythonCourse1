"""
Módulo que usaremos para descomprimir el archivo Proyecto+Día+9.zip
"""
import shutil
from pathlib import PureWindowsPath

archivo_a_descomprimir = "C:\\Users\Shaila Gibert\IdeaProjects\PythonCourse1\Day9\Proyecto\Proyecto+Día+9.zip"
archivo_a_descomprimir = PureWindowsPath(archivo_a_descomprimir)
shutil.unpack_archive(archivo_a_descomprimir, "instrucciones_proyecto", "zip")