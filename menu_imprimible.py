while True:
# Imprimir el men
    print("Menú:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")

    # Solicitar al usuario que ingrese una opción
    opcion = input("Ingrese el número de opción que desea: ")

    # Procesar la opción seleccionada
    if opcion == "1":
        print("Ha seleccionado sitio deportivo.")
        print("Seleccione una de las siguientes opciones:")
        print("Deportes de equipo")
        print("Deportes en solitario")
        print("Deportes extremos")
        break
    elif opcion == "2":
        print("Ha seleccionado sitio fitness de recetas.")
    elif opcion == "3":
        print("Ha seleccionado sitio de mascotas")
    elif opcion == "4":
        print("Saliendo del programa ... ")
        break # Salir del ciclo while

    else:
        print("Opción inválida. Por favor, ingrese un número válido.")