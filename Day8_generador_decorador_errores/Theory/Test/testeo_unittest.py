"""
---- PRUEBAS CON UNITTEST ----
"""

# Importamos el módulo que deseamos testear
from Day8_generador_decorador_errores.Theory.Paquete1.SumaYresta import suma


# Importamos el paquete de unittest
import unittest


class ProbarCambiarMayuscula(unittest.TestCase):

    # Todas las funciones deberán empezar con test
    def test_suma(self):
        # Indicamos el resultado que esperamos
        total_esperado = 5
        # Llamamos a la función
        resultado = suma(2,3)
        # Realizamos el test, indicando siempre primero el resultado real y después el resultado esperado
        self.assertEqual(resultado, total_esperado)


if __name__ == '__main__':
    unittest.main()