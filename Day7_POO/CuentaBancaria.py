"""
Crea una aplicación que estará basada en la POO
1. Clase Persona con nombre y apellido
2. Clase Cliente que hereda de persona y con numero de cuenta y balance.
2. Métodos de cliente: __str__, depositar, retirar
3. Crear cliente con datos dados por usuario
4. Código de ejecución de loop hasta que usuario desee salir del programa
"""
from os import system


class Persona:
    def __init__(self, nombre, apellido1, apellido2):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2


class Cliente(Persona):
    def __init__(self, nombre, apellido1, apellido2, cuenta, balance):
        super().__init__(nombre, apellido1, apellido2)
        self.cuenta = cuenta
        self.balance = balance

    def __str__(self):
        return f"[Nombre: {self.nombre}, Apellidos: {self.apellido1} {self.apellido2}, Cuenta: {self.cuenta}, " \
               f"Balance: {self.balance}]"

    def retirar(self):
        # Limpiamos consola
        system('cls')

        # Solicitamos importe
        cantidad_retirar = float(input("Indique la cantidad de dinero a retirar: "))

        # Retiramos dinero si balance igual o superior a cantidad a retirar
        if cantidad_retirar <= self.balance:
            self.balance -= cantidad_retirar
            print(f"Se han retirado los {cantidad_retirar}€ correctamente.")
            print(f"Su balance actual es de {self.balance}€.")
        else:
            print(f"No dispone de dinero suficiente en su cuenta para retirar el importe de {cantidad_retirar}€.")

        # Esperamos input de usuario
        input("Pulse cualquier tecla para continuar")

    def depositar(self):
        # Limpiamos consola
        system('cls')

        # Solicitamos cantidad a depositar
        cantidad_depositar = float(input("Indique la cantidad de dinero a depositar: "))
        self.balance += cantidad_depositar
        print(f"Se ha depositado correctamente en su cuenta el importe de {cantidad_depositar}€.")
        print(f"Su balance actual es de {self.balance}€.")

        # Esperamos input de usuario
        input("Pulse cualquier tecla para continuar: ")


def crearCliente():
    print("BIENVENIDO AL GESTOR DE SU CUENTA BANCARIA.")
    print("Actualmente no disponemos de ningún dato de su cuenta. Vamos a crearle una cuenta a continuación.")
    nombre = input("Por favor, indíquenos su nombre: ").upper()
    apellido1 = input("Por favor, indíquenos su primer apellido: ").upper()
    apellido2 = input("Por favor, indíquenos su segundo apellido. En caso de no tener, simplemente presione "
                      "\"INTRO\": ").upper()
    cuenta = input("Finalmente, indique el número de su cuenta bancaria: ").upper()

    # Instanciamos objeto de la clase cliente
    cliente = Cliente(nombre, apellido1, apellido2, cuenta, 0)
    print("Se ha creado su cuenta en nuestra base de datos.")

    # Esperamos input de usuario
    input("Pulse cualquier tecla para continuar: ")

    # Retornamos objeto
    return cliente


def menu_inicio():
    opcion = 10
    print("Gracias por usar nuestro gestor de cuenta bancaria.")
    while opcion not in [1, 2, 3]:
        print("A continuación le mostraremos las opciones disponibles para su cuenta: ")
        print("[1]. Ingresar dinero a su cuenta.")
        print("[2]. Retirar dinero de su cuenta.")
        print("[3]. Mostrar la información de su cuenta.")
        print("[0]. Salir del programa.")
        opcion = int(input("\nIndique la opción que desea ejecutar "
                       "indicando el número que aparece delante de cada opción: "))
        if opcion not in [1, 2, 3, 0]:
            print("\nEl número indicado no es válido.")
    return opcion


def seleccionar_opcion(cliente, opcion):
    match opcion:
        case 1:
            cliente.depositar()
        case 2:
            cliente.retirar()
        case 3:
            print(cliente)
            input("Pulse cualquier tecla para continuar: ")
        case 0:
            print("Gracias por usar el gestor de cuenta bancaria.\n\n")


cliente = crearCliente()
opcion = 10
while opcion != 0:
    opcion = menu_inicio()
    seleccionar_opcion(cliente, opcion)
