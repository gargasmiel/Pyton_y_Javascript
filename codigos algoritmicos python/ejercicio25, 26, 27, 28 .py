print("MENU")
print("1. Saludar")
print("2. Mostrar fecha")
print("3. Salir")

numero = int(input("Ingrese un numero: "))

if numero >= 1:

    if numero == 1:
        nombre = input("Ingrese su nombre: ")
        print("Hola", nombre)

    else:

        if numero == 2:
            print("La fecha de hoy es 25/06/2024")

        else:

            if numero == 3:
                salir = input("¿Desea salir? (s/n): ")

                if salir.lower() == "s":
                    print("¡Hasta luego!")
                else:
                    print("Continuando con el programa...")

            else:
                print("Opción no válida")