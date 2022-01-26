"""
--- MÉTODOS ESPECIALES -----
"""


# Son aquellos que se usan para crear funcionalidades especiales
# Los que hemos conocido: __init__, __bases__, __subclasses__, __mro__

class CD:
    def __init__(self, autor, titulo, cantidad_canciones):
        self.autor = autor
        self.titulo = titulo
        self.cantidad_canciones = cantidad_canciones

    # Equivalente al toString. Cuando se llame a print se llamará a este método especial
    def __str__(self):
        return f"Autor: {self.autor}, Titulo: {self.autor}, Canciones: {self.cantidad_canciones}"

    # Cuando se llame a len, se llamará a este método especial
    def __len__(self):
        return self.cantidad_canciones

    def __del__(self):
        disco_eliminado = self.__str__()
        print(f"Se ha eliminado el CD [{disco_eliminado}]")


disco1 = CD("Shaila Gibert", "Mi primer disco", 12)

# Con [del] eliminamos una instancia eliminada, al modificarla con __del__, no solo eliminará, sino que
# realizará la acción que le indicamos al crear el método especial
print(disco1)
print(len(disco1))
del disco1
