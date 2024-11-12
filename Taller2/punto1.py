'''     
Plantea una estructura en Python para almacenar información de los empleados de una empresa, incluyendo las horas laborales y las horas extras nocturnas trabajadas.
Crea una estructura (lista, diccionario) que contenga la siguiente información para cada empleado:
Nombre: nombre del empleado.
Horas laborales: número de horas trabajadas durante el horario normal.
Horas extras nocturnas: número de horas extra trabajadas durante el horario nocturno.
'''
# Se declara e inicializa la lista de empleados
empleados = [
    ["Juan", 40, 5],
    ["María", 35, 3],
    ["Pedro", 42, 6],
    ["Laura", 38, 4]
]

# Imprimir encabezado de la tabla
print(f"{'Nombre':<20} {'Horas Laborales':<25} {'Horas Extras Nocturnas':<30}")

#Se recorre la lista empleados
for empleado in empleados:
    nombre, horas_laborales, horas_extras_nocturnas = empleado
    #Imprimir lista de empleados formateada
    print(f"{nombre:<20} {horas_laborales:<25} {horas_extras_nocturnas:<30}")


