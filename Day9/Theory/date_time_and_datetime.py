"""
--- TIME ---
"""


# Deberemos importar el módulo

import datetime

from datetime import datetime, date, time

mi_hora = time(17, 35, 30)

# Horas, minutos, segundos, microsegundos, zona horaria.. son los argumentos que pasamos

# Podemos seccionar la hora
print(mi_hora.hour)
print(mi_hora.minute)

"""
--- DATE ---
"""

mi_dia = date(2022, 1, 27)  # Año, mes y dia
print(mi_dia)
# Si llamamos today desde cualquier objeto del tipo date / datetime, nos indicará el dia de hoy
print(mi_dia.today())
print(mi_dia.ctime())

"""
--- DATETIME ---
"""

mi_fecha = datetime(2021, 1, 26, 15, 30)  # Fecha y después hora

# Podemos cambiar los datos de una variable
mi_fecha = mi_fecha.replace(month=2)

# Podemos realizar cálculos mediante las fechas
nacimiento = date(2000, 12, 11)
hoy = date.today()
print(f"A día de hoy, {hoy}, tengo {int((hoy-nacimiento).days/365)} años")

hoy = datetime.today()
print(hoy.minute)