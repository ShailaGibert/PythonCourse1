"""
---- ACOPLAMIENTO ----
"""
'''
- Acoplamiento débil, que implica que no hay dependencia entre un módulo y otros. Esta es la situación ideal.

- Acoplamiento fuerte, que es la situación contraria, e indica que el módulo tiene dependencias internas con otros

Una situación de acoplamiento fuerte puede originar errores que son difíciles de depurar.
'''


class Mascota:
    tiene_patas = True
    pass


class Perro:
    def __init__(self):
        self.velocidad = None

    def correr(self, velocidad):
        # Aquí se está creando una dependencia con el atributo de clase Mascota [tiene_patas]
        if Mascota.tiene_patas:
            self.velocidad = velocidad


mi_mascota = Perro()
mi_mascota.correr("rápido")
print(mi_mascota.velocidad)

''' Si tu programa debe contener dependencias externas, deberás asegurarte que las mismas son esenciales y están 
debidamente justificadas para minimizar los efectos adversos mencionados. '''