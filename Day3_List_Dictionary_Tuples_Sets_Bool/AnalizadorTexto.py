"""
ANALIZADOR DE TEXTO:\n\n
Pide texto a usuario por consola\n
Pide tres letras a la eleccion del usuario\n
------------------------------------------------------------------------
Devolver la cantidad de veces que aparece cada letra, NOT CASE SENSITIVE [OK]\n
Cantidad de palabras a lo largo del texto [ok]\n
Informar la primera y última letra del texto\n
Texto con las palabras invertidas [OK]\n
Confirmar si la palabra Python se encuentra en el texto [OK]
"""

texto = input("Gracias por usar nuestro analizador de texto.\n Indique el texto a analizar: ")
palabras = (input("¿Qué 3 letras desee que contabilicemos? Separe cada letra por un intro\n")).lower()
palabras = palabras.split()
texto = texto.lower()
encontrar_python = ("python" in texto)
primera_letra = texto[0]
ultima_letra = texto[-1]
primera_letra_recuento = texto.count(palabras[0])
segunda_letra_recuento = texto.count(palabras[1])
tercera_letra_recuento = texto.count(palabras[2])
texto = texto.split()
cantidad_palabras = len(texto)
texto.reverse()
texto_inverso = " ".join(texto)

print(f"La letra \"{palabras[0]}\" aparece en el texto \"{primera_letra_recuento}\". "
      f"La letra \"{palabras[1]}\" aparece en el texto \"{segunda_letra_recuento}\". "
      f"La letra \"{palabras[2]}\" aparece en el texto \"{tercera_letra_recuento}\".")
print(f"\nEn total hay {cantidad_palabras} palabras en el texto introducido.")
print(f"\nLa primera letra y la última son \"{primera_letra}\" y \"{ultima_letra}\" respectivamente.")
print(f"\nEl texto indicado con las palabras invertidas correspondería al siguiente texto:\n\"{texto_inverso}\"\n")
print(f"\nPor último, tras confirmar si la palabra \"Python\" se encuentra en el texto, "
      f"el resultado es \"{encontrar_python}\".")
