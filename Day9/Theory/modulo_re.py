"""
--- RE ---
"""

# Con RE [regular expression] nos sirve para abstraer más información de un string
# Para indicar a Python que se trata de una expresión regular, deberemos crear un patrón con:
import re
from os import system

"""
r"" --> r para indicar que es un patrón
\d dentro de r"" --> cualquier valor numérico
\w dentro de r"" --> cualquier valor alfabético
\s dentro de r"" --> un espacio
Cuando indicas \D, \W, \S [en mayúscula] estás negando dicho carácter
Cuantificadores --> cantidad de veces que queremos indicar dicha expresión 
    - \d{3} == \d\d\d
    - \d+ == ese valor debe aparecer una vez o más
    - \d{2, 3} --> debe aparecer entre 2 a 3 veces
    - \d{2, } --> debe aparecer como mínimo 2 veces, sin máximo
    - \d* --> opcional y/o la cantidad de veces que se desee
    - ? casas? --> permite a la letra "s" a que aparezca o no. Sirve sobretodo para buscar plurales y singulares
    - | un valor u otro --> lunes|martes
    - . --> valor anterior a lo que se busca ".demos" in "atendemos" = "ndemos"
    - ^ --> al principio del texto en el que se busca ej.: r"^\D" --> confirmar que el primer carácter no es un digito
    - $ --> al final del texto en el que se busca ej.: r"\D$" --> confirmar que el último carácter no es un digito
    - [^\s] --> excluye de la búsqueda aquello que indiquemos dentro de las llaves
"""

texto = "Si necesitas ayuda, escribe ayuda"
patron = 'nada'
busqueda = re.search(patron, texto)
print(busqueda)  # Indica que no existe dicha palabra

patron = 'ayuda'
busqueda = re.search(patron, texto)
print(busqueda.span())  # Indica el inicio y final de dicha palabra encontrada
print(busqueda.start())  # Indica el inicio de dicha palabra
print(busqueda.end())  # Indica el final de dicha palabra

# Si queremos encontrar todas las coincidencias
busqueda = re.findall(patron, texto)
print(busqueda)

# Si queremos tratar con cada elemento encontrado:
for encontrado in re.finditer(patron, texto):  # finditer --> buscar para cada iteración
    print(encontrado.span())

texto = "llama al 618 985 046"
patron = r"\d{3}\s\d{3}\s\d{3}" # Buscamos cualquier texto que cumpla con este patrón
resultado = re.search(patron, texto)
print(resultado)

# Si solo queremos el valor:
print(resultado.group())

# Podemos compilar los patrones
patron = re.compile(r"(\d{3})\s(\d{3})\s(\d{3})")
resultado = re.search(patron, texto)
# ¡OJO! Los indices empiezan por 1, no por 0
print(resultado.group(1))
print(resultado.group(2))
print(resultado.group(3))

system('cls')

# Queremos confirmar que el input de un usuario cumpla con un patrón
contrasenia = input("Inidque su contraseña. La primera letra debe ser una letra y debe tener una longitud mínima de 7 "
                    "carácteres: ")

patron = r"\D{1}\w{6,}"

chequear_patron = re.search(patron, contrasenia)

print(chequear_patron)

# Usemos el [^\s]
texto = "Si necesitas ayuda, escribe ayuda"
busqueda = re.findall(r"[^\s]", texto) # Nos indicará todos aquellos resultados que no tengan el espacio

# Si queremos agrupar los resultados en palabras (que separe el resultado cada vez que encuentre 1 espacio o más)
busqueda = re.findall(r"[^\s]+", texto) # Con el "+" estamos indicando que solo separe cuando encuentre 1 espacio o más
print(busqueda)
