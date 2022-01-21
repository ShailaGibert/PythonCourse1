"""
CREAR UN ADMINISTRADOR DE RECETAS
- Crear directorio de carpetas en carpeta base (home)
________________________________________
1. Recetas
    1.1. Carnes
        - Entrecot al Mallbec.txt
        - Matambre a la pizza.txt
    1.2. Ensaladas
        - Ensalada Griega.txt
        - Ensalada Mediterranea.txt
    1.3. Pastas
        - Canelones de espinaca.txt
        - Raviolis de Ricotta.txt
    1.4. Postres
        - Compota de Manzana.txt
        - Tarta de Frambuesa.txt
________________________________________
- Saludará al usuario
- Indicará la ruta en la que se encuentra la carpeta Recetas
- Informará la cantidad de recetas
- Le pedirá elegir una opción
    __________________________
    1. Leer receta
        - Pedir categoría
        - Receta a leer
    2. Crear receta
        - Elegir categoría
        - Pedir nombre de receta
        - Pedir contenido de receta
    3. Crear categoría
        - Pedir nombre de categoría
        - Crear categoría
    4. Eliminar receta
        - Pedir categoría
        - Receta a eliminar
    5. Eliminar categoría
        - Pedir categoría a eliminar
    6. Finalizar programa
    __________________________

* Que el usuario pueda volver al menú principal cada vez que termine un proceso
* Limpiar consola cuando vuelva al menú principal
"""
import os
import shutil
from os import system
from pathlib import Path, PureWindowsPath


def saludar_usuario():
    """
    Primera función de inicio de aplicación
    """
    print("BIENVENIDO A LA GESTIÓN DE RECETARIO DE TU EQUIPO")
    print("*" * 10)


def indicar_ruta_Recetas():
    """
    Sacamos la ruta absoluta en la que se encuentra la carpeta Recetas
    return: ruta_recetario = ruta de la carpeta Recetas
    """
    ruta_recetario = Path(Path.home(), "Recetas")
    return Path(ruta_recetario)


def mostrar_menu_principal(ruta_recetario):
    """
    Mostramos las opciones a ejecutar desde el administrador por pantalla, damos al usuario la opción de elegir.
    Mientras no indique un numero válido, se mostrará el menú principal
    :return: nombre_usuario
    """
    ruta_recetario = Path(ruta_recetario)
    nombre_usuario = ruta_recetario.parent.stem
    numero_dado = 0
    print(f"Gracias {nombre_usuario} por usar el administrador de recetas. A continuación se le mostrarán las opciones"
          f" del programa.\n")
    while numero_dado not in [1, 2, 3, 4, 5, 6]:
        print("[1]: Leer receta existente")
        print("[2]: Crear receta nueva")
        print("[3]: Crear categoría")
        print("[4]: Eliminar receta existente")
        print("[5]: Eliminar categoría existente")
        print("[6]: Salir del programa")
        print("*" * 5)
        numero_dado = int(input("Por favor, indique el número de la opción que desee ejecutar: "))
        if numero_dado not in [1, 2, 3, 4, 5, 6]:
            input("El número indicado no es válido.\n"
                  "Se le mostrará el menú principal de nuevo. Pulse cualquier tecla para continuar: ")
            # Limpiamos consola
            system('cls')
        elif numero_dado in [1, 2, 3, 4, 5, 6]:
            # Limpiamos consola
            system('cls')
            return numero_dado


def final_orden():
    print("La orden se ha ejecutado correctamente y finalizado con éxito.")
    print("*" * 10)
    input("Pulse qualquier tecla para volver al menú principal: ")
    system('cls')


def listar_glob(categoria, categoria_o_texto, carpeta_a_leer):
    """
    Listará con glob los archivos o repositorios dentro de la ruta madre
    :param categoria: ruta en la que esté la carpeta recetarios
    :return:
    """
    print(f"A continuación le mostramos {categoria_o_texto} que existen en su carpeta \"{carpeta_a_leer}\":")
    ruta = indicar_ruta_Recetas()
    for elemento in Path(ruta).glob(categoria):
        print(elemento.name)


def elegir_para_leer(texto_de_input, categoria_escogida):
    """

    :param categoria_para_glob: texto que se pasará a la función listar_glob para listar archivos o carpetas
    :param categoria_o_texto: "las categorías" // "los archivos"
    :param carpeta_a_leer:  "Recetas" // cualquier categoría dentro
    :return: ruta_categoria
    """
    ruta_categoria = "xxxxxxxxxxxxxxx"
    while not Path(ruta_categoria).exists():
        categoria_o_archivo = input(texto_de_input)
        if categoria_escogida == "":
            ruta_categoria = Path(indicar_ruta_Recetas(), categoria_o_archivo)
        else:
            ruta_categoria = Path(indicar_ruta_Recetas(), categoria_escogida, categoria_o_archivo + ".txt")

        if not Path(ruta_categoria).exists():
            print("\n\nEl nombre de la categoría o archivo indicado no es válido.\n"
                  "Si está indicando un archivo de texto, no indique la extensión \".txt\"\n")
    return ruta_categoria


def abrir_y_leer(ruta_archivo_a_leer, texto_de_print):
    ruta = Path(ruta_archivo_a_leer)
    print(texto_de_print)
    print("*" * 5 + "\n")
    print(ruta.read_text())
    print("*" * 5 + "\n")


def leer_receta():
    """
    función que le pedirá al usuario que indique la categoría en la que se encuentra la receta
    le pedirá también el nombre del archivo
    Buscará el archivo.stem, abrirá el archivo en modo lectura y leerá la receta.
    Esperará tecla para limpiar la consola
    :return: void
    """

    # Limpiamos consola
    system('cls')

    print("Ha elegido la opción \"[1]: leer receta.\"\n")
    print("*" * 5)

    # Listamos primero las categorías existentes para mostrar en pantalla
    categoria_para_glob = "*/"
    listar_glob(categoria_para_glob, "las categorías", "Recetas")

    # Llamamos a elegir_para_leer que nos devolverá la categoría seleccionada para después seleccionar el texto
    texto_de_input = "Por favor, indique el nombre de la categoría en la que se encuentra la receta: "
    categoria = Path(elegir_para_leer(texto_de_input, "")).stem

    # Limpiamos consola
    system('cls')

    # Listamos primero las recetas que existen dentro de la categoría elegida
    categoria_para_glob = categoria + "/*.txt"
    listar_glob(categoria_para_glob, "los archivos", categoria)

    # Llamamos elegir_para_leer para que nos devuelva el nombre del texto a leer
    texto_de_input = "Por favor, indique el nombre del arhivo de texto que desea leer: "
    ruta_archivo_a_leer = elegir_para_leer(texto_de_input, categoria)

    # Limpiamos consola
    system('cls')

    texto_de_input = f"A continuación se muestra las instrucciones dentro de la receta {Path(ruta_archivo_a_leer).stem}."
    abrir_y_leer(ruta_archivo_a_leer, texto_de_input)


def preparando_ruta(categoria_para_texto_nuevo):
    """
    :param categoria_para_texto_nuevo: se pasa el nombre de la categoría en la que se creará el archivo .txt
    Si se pasa "" en categoría_para_texto_nuevo, se entenderá que lo que se debe crear es una ruta para crear un
    directorio
    :return: devuelve la ruta para crear el archivo o directorio según lo que proceda
    """
    ruta_elemento_a_crear = ""
    while Path(ruta_elemento_a_crear).exists():
        elemento_a_crear = input("Por favor, indique el nombre del elemento con el que desea realizar la acción: ")

        # Si se ha pasado categoria_para_texto_nuevo vacío, significa que debemos crear un directorio
        if categoria_para_texto_nuevo == "":
            # Creamos la ruta conjunta para crear el directorio nuevo
            ruta_elemento_a_crear = Path(indicar_ruta_Recetas(), elemento_a_crear).resolve()

        # Si se ha pasado categoria_para_texto_nuevo lleno, significa que debemos crear una receta
        else:
            # Creamos ruta conjunta para la receta
            ruta_elemento_a_crear = Path(indicar_ruta_Recetas(), categoria_para_texto_nuevo, elemento_a_crear + ".txt")
        if Path(ruta_elemento_a_crear).exists():
            print("El nombre para el nuevo elemento ya existe.")
    return ruta_elemento_a_crear


def crear_elemento(ruta):
    """
    Crea el archivo o directorio
    :param ruta: la ruta creada con la funcion seleccionar_texto_antes_creacion
    """
    ruta_windows = Path(ruta).resolve()
    # Si contiene la extension .txt, significa que deberemos crear un archivo de texto
    if ruta.suffix == ".txt":
        archivo = open(ruta_windows, 'w')
    else:
        os.makedirs(ruta_windows)
        print(f"El elemento con nombre {Path(ruta).stem} ha sido creado correctamente en {Path(ruta).parent.stem}")


def aniadir_texto_receta(ruta_archivo):
    """
    Una vez creado el archivo, abrirá el archivo de texto en modo 'w' para sobreescribir dentro
    :param ruta_archivo: ruta del archivo de texto que se debe abrir
    """
    print("Indique a continuación el texto que desea añadir a la receta. Escriba \"STOP\" cuando desee salir "
          "del modo de escritura\n" + "*" * 15 + "\n")

    texto = input("> ")
    while texto != "STOP":
        archivo = open(ruta_archivo, 'a')
        archivo.write(texto + "\n")
        archivo.close()
        texto = input("> ")

    print("Se ha añadido el texto correctamente.\n")


def crear_receta():
    """
    función que hace uso de:
    - listar_gob para listar el contenido del directorio en el que nos encontramos
    - elegir_para_leer para saber la categoria en la que crear la receta
    - preparando_ruta para devolver una ruta con el archivo de texto
    - crear_elemento para crear la receta
    - aniadir_texto_receta para sobreescribir el archivo de texto
    """
    # Limpiamos consola
    system('cls')
    print("Ha elegido la opción \"[2]: crear receta.\"\n")
    print("*" * 5)

    # Limpiamos consola
    system('cls')
    # Listamos primero las categorías existentes para mostrar en pantalla
    categoria_para_glob = "*/"
    listar_glob(categoria_para_glob, "las categorías", "Recetas")

    # Llamamos a elegir_para_leer que nos devolverá la categoría seleccionada para después crear el texto dentro
    texto_de_input = "Por favor, indique el nombre de la categoría en la que desee crear la receta: "
    # Categoría elegida en blanco dado que es lo que queremos seleccionar
    categoria = Path(elegir_para_leer(texto_de_input, "")).stem

    # Limpiamos consola
    system('cls')
    # Listamos ahora las recetas existentes en la categoría seleccionada
    categoria_para_glob = categoria + "/*.txt"
    listar_glob(categoria_para_glob, "las recetas", categoria)

    # Llamamos a seleccionar_ruta_antes_creacion para que seleccione la ruta antes de crear
    ruta_elemento_a_crear = preparando_ruta(categoria)

    # Llamamos a crear para crear la receta en la categoría indicada
    crear_elemento(ruta_elemento_a_crear)

    # Añadimos texto a la receta
    aniadir_texto_receta(ruta_elemento_a_crear)


def crear_categoria():
    """
    Función que hace uso de:
    - listar_gob para listar el contenido del directorio en el que nos encontramos
    - preparando_ruta para devolver una ruta con el directorio
    - crear_elemento para crear el directorio
    """
    # Limpiamos consola
    system('cls')

    print("Ha elegido la opción \"[3]: crear categoría.\"\n")
    print("*" * 5)

    # Limpiamos consola
    system('cls')

    # Listamos primero las categorías existentes para mostrar en pantalla
    categoria_para_glob = "*/"
    listar_glob(categoria_para_glob, "las categorías", "Recetas")

    # Llamamos a seleccionar_ruta_antes_creacion para que seleccione la ruta antes de crear
    ruta_elemento_a_crear = preparando_ruta("")

    # Llamamos a crear para crear la categoría en la carpeta de Recetas
    crear_elemento(ruta_elemento_a_crear)
    print("\n\n")


def eliminar_elemento(ruta):
    """
    Función que elimina el archivo de texto o el directorio segun el tipo de ruta que se pasa como argumento
    """
    if Path(ruta).suffix == ".txt":
        ruta = PureWindowsPath(ruta)
        Path(ruta).rmdir()
        print(f"Se ha eliminado el archivo {Path(ruta).stem}")
    else:
        confirmacion = ""
        while confirmacion not in ["S", "N"]:
            confirmacion = input("Si elimina el directorio y existen archivos o carpetas en él, éstos también se "
                                 "eliminarán. ¿Desea continuar? [S/N]: ").upper()
            if confirmacion == "S":
                ruta = PureWindowsPath(ruta)
                shutil.rmtree(ruta)
                print(f"Se ha eliminado correctamente el directorio {Path(ruta).stem}")
            elif confirmacion == "N":
                print("Se cancela la eliminación del directorio.\n\n")
                pass
            if confirmacion not in ["S", "N"]:
                print("Por favor, seleccione una de las opciones válidas. [S/N]")


def eliminar_receta():
    """
    Función que hace uso de:
    - listar_gob para listar el contenido del directorio en el que nos encontramos
    - elegir_para_leer para saber la categoria en la que eliminar la receta
    - preparando_ruta para devolver una ruta con el archivo de texto
    - eliminar_elemento para eliminar la receta
    """
    # Limpiamos consola
    system('cls')

    print("Ha elegido la opción \"[4]: eliminar receta.\"\n")
    print("*" * 5)

    # Listamos primero las categorías existentes para mostrar en pantalla
    categoria_para_glob = "*/"
    listar_glob(categoria_para_glob, "las categorías", "Recetas")

    # Llamamos a elegir_para_leer que nos devolverá la categoría seleccionada para después crear el texto dentro
    texto_de_input = "Por favor, indique el nombre de la categoría en la que desee eliminar la receta: "
    # Categoría elegida en blanco dado que es lo que queremos seleccionar
    categoria = Path(elegir_para_leer(texto_de_input, "")).stem

    # Limpiamos consola
    system('cls')
    # Listamos ahora las recetas existentes en la categoría seleccionada
    categoria_para_glob = categoria + "/*.txt"
    listar_glob(categoria_para_glob, "las recetas", categoria)

    # Llamamos a preparando_ruta para que seleccione la ruta antes de eliminar la receta
    texto_de_input = "Por favor, indique el nombre de la receta a eliminar: "
    ruta_elemento_a_eliminar = elegir_para_leer(texto_de_input, categoria)

    # Llamamos a eliminar_elemento para que elimine el archivo
    eliminar_elemento(ruta_elemento_a_eliminar)


def eliminar_categoria():
    """
    Función que hace uso de:
    - listar_gob para listar el contenido del directorio en el que nos encontramos
    - preparando_ruta para devolver una ruta con el directorio
    - eliminar_elemento para eliminar la receta
    """
    # Limpiamos consola
    system('cls')

    print("Ha elegido la opción \"[5]: eliminar categoría.\"\n")
    print("*" * 5)

    # Listamos primero las categorías existentes para mostrar en pantalla
    categoria_para_glob = "*/"
    listar_glob(categoria_para_glob, "las categorías", "Recetas")

    # Llamamos a preparando_ruta para que seleccione la ruta antes de eliminar la receta
    texto_de_input = "Por favor, indique el nombre de la categoría que desea eliminar: "
    ruta_elemento_a_eliminar = elegir_para_leer(texto_de_input, "")

    # Llamamos a eliminar_elemento para que elimine el archivo
    eliminar_elemento(ruta_elemento_a_eliminar)


def parar_programa():
    """
    Para el código
    """
    # Limpiamos consola
    system('cls')

    print("Gracias por usar nuestro administrador de recetarios.\n\n\n")
    print("*" * 20)


def elegir_opcion(opcion):
    """
    Función que al recibir un número de opción válido, ejecutará las funciones necesarias para cada opción del menú
    :param opcion: int from 1 to 6
    """
    match opcion:
        case 1:
            leer_receta()
            final_orden()
        case 2:
            crear_receta()
            final_orden()
        case 3:
            crear_categoria()
            final_orden()
        case 4:
            eliminar_receta()
            final_orden()
        case 5:
            eliminar_categoria()
            final_orden()
        case 6:
            parar_programa()


saludar_usuario()
ruta_recetario = indicar_ruta_Recetas()
print("Tu carpeta de Recetas se encuentra en la siguiente ruta:\n"
      f"{ruta_recetario}\n\n")
# Limpiamos consola
input("Presione cualquier tecla para entrar en el menú principal: ")
system('cls')
numero_dado = 0
while numero_dado != 6:
    numero_dado = mostrar_menu_principal(ruta_recetario)
    elegir_opcion(numero_dado)
