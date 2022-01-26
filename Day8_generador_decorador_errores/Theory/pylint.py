"""
--- DETECTAR ERRORES ---
"""


# Pylint es una herramienta que analiza el código y muestra posibles errores de estilo (PEP-8)
# Debemos instalar Pylint
def una_funcion():
    """
    Función que imprime algo
    """
    numero = 10
    print(numero)


una_funcion()

# Para testear esta función deberemos:
'''
1. Ir al terminal a la ubicación del módulo. Si está dentro de algún folder, deberemos entrar.
2. Ejecutar el módulo con 'pylint' al inicio [primero pylint deberá estar instalado con "pip install pylint"
3. "pylint pylint.py -r y" -r --> reporte // y --> yes
'''