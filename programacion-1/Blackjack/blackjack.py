#Tarea programacion, Genio y figura...
#Leonardo Mariscal Villalobos, Leonardo Zepeda Aboytes

def proceso():
    print("1. Reloj de arena\n2. Rombo\n3. Moño\n4. Copa\n")
    respuesta = int(input("Selecciona el numero < "))
    match respuesta:
        case 1:
            print("\n\n\n")
            while True:
                opcion = input("Relleno [si/no] < ")
                if opcion.lower() == "no":
                    while True:
                        asignacion_forma = input("Que simbolo desea utilizar < ")
                        if len(asignacion_forma) == 1:
                            break
                        elif len(asignacion_forma) == 2:
                            print("ERROR 001")
                    while True:
                        dimension = int(input("\nAsigna el tamaño [impar] < "))
                        print("\n")
                        if dimension % 2 == 1:
                            if dimension > 29:
                                print("Numero demasiado grande")
                                break
                            for i in range(dimension, 0, -1):
                                borrador = " " * (dimension - i)
                                if i == dimension:
                                    print(borrador + asignacion_forma * (2 * i - 1))
                                elif i == 1:
                                    print(borrador + asignacion_forma * (2 * i - 1))
                                else:
                                    forma = " " * (2 * i - 3)
                                    print(borrador + asignacion_forma + forma + asignacion_forma)
                            for i in range(2, dimension + 1):
                                borrador2 = " " * (dimension - i)
                                if i == dimension:
                                    print(borrador2 + asignacion_forma * (2 * i - 1))
                                else:
                                    forma2 = " " * (2 * i - 3)
                                    print(borrador2 + asignacion_forma + forma2 + asignacion_forma)
                        elif dimension % 2 == 0:
                            print("ERROR 002")
                elif opcion.lower() == "si":
                    while True:
                        asignacion_forma = input("Que simbolo desea utilizar < ")
                        if len(asignacion_forma) == 1:
                            break
                        elif len(asignacion_forma) == 2:
                            print("ERROR 001")
                    while True:
                        dimension = int(input("\nAsigna el tamaño [impar] < "))
                        print("\n")
                        if dimension % 2 == 1:
                            if dimension > 29:
                                print("Numero demasiado grande")
                                break
                            for i in range(dimension, 0, -1):
                                borrador = " " * (dimension - i)
                                forma = asignacion_forma * (2 * i - 1)
                                print(borrador + forma)
                            for i in range(2, dimension + 1):
                                borrador2 = " " * (dimension - i)
                                forma2 = asignacion_forma * (2 * i - 1)
                                print(borrador2 + forma2)
                        elif dimension % 2 == 0:
                            print("ERROR 002")
                        break
                else:
                    print("ERROR 003")
                break
        case 2:
            print("\n\n\n")
            while True:
                opcion = input("Relleno [si/no] < ")
                if opcion.lower() == "no":
                    while True:
                        asignacion_forma = input("Que simbolo desea utilizar < ")
                        if len(asignacion_forma) == 1:
                            break
                        elif len(asignacion_forma) == 2:
                            print("ERROR 001")
                    while True:
                        dimension = int(input("\nAsigna el tamaño [impar] < "))
                        print("\n")
                        if dimension % 2 == 1:
                            if dimension > 29:
                                print("Numero demasiado grande")
                                break
                            for i in range(1, dimension + 1):
                                borrador = " " * (dimension - i)
                                if i == 1:
                                    print(borrador + "*")
                                elif i == dimension:
                                    print(borrador + "*" * (2 * i - 1))
                                else:
                                    forma2 = " " * (2 * i - 3)
                                    print(borrador + "*" + forma2 + "*")
                            for i in range(dimension -1, 0, -1):
                                borrador = " " *(dimension - i)
                                if i == 1:
                                    print(borrador + "*")
                                else:
                                    forma2 = " " * (2 * i - 3)
                                    print(borrador + "*" + forma2 + "*")
                        elif dimension % 2 == 0:
                            print("ERROR 002")
                        break
                elif opcion.lower() == "si":
                    while True:
                        asignacion_forma = input("Que simbolo desea utilizar < ")
                        if len(asignacion_forma) == 1:
                            break
                        elif len(asignacion_forma) == 2:
                            print("ERROR 001")
                    while True:
                        dimension = int(input("\nAsigna el tamaño [impar] < "))
                        print("\n")
                        if dimension % 2 == 1:
                            if dimension > 29:
                                print("Numero demasiado grande")
                                break
                            for i in range(1, dimension, 1):
                                borrador2 = " " * (dimension - i)
                                forma2 = asignacion_forma * (2 * i - 1)
                                print(borrador2 + forma2)
                            for i in range(dimension, 0, -1):
                                borrador2 = " " * (dimension - i)
                                forma2 = asignacion_forma * (2 * i - 1)
                                print(borrador2 + forma2)
                        if dimension % 2 == 0:
                            print("ERROR 002")
                        break
                else:
                    print("ERROR 003")
                break
        case 3:
            print("\n\n\n")
            while True:
                opcion = input("Relleno [si/no] < ")
                if opcion.lower() == "no":
                    while True:
                        asignacion_forma = input("Que signo desea utilizar < ")
                        if len(asignacion_forma) == 1:
                            break
                        elif len(asignacion_forma) == 2:
                            print("ERROR 001")
                    dimension = int(input("\nAsigna el tamaño [impar] < "))
                    if dimension % 2 == 1:
                        if dimension > 29:
                                print("Numero demasiado grande")
                                break
                        for i in range(0, dimension):
                            izquierda = " " * i
                            centro = " " * (dimension - i)
                            derecha = " " * (dimension - i)
                            final = " " * i
                            print("*" + izquierda, "*" + centro, derecha + "*", final + "*")
                        for i in range(dimension, -1, -1):
                            izquierda = " " * i
                            centro = " " * (dimension - i)
                            derecha = " " * (dimension - i)
                            final = " " * i
                            print("*" + izquierda, "*" + centro, derecha + "*", final + "*")
                    elif dimension % 2 == 0:
                        print("Inserta un numero real")
                elif opcion.lower() == "si":
                    while True:
                        asignacion_forma = input("Que signo desea utilizar < ")
                        if len(asignacion_forma) == 1:
                            break
                        elif len(asignacion_forma) == 2:
                            print("ERROR 002")
                    dimension = int(input("\nAsigna el tamaño [impar] < "))
                    if dimension % 2 == 1:
                        if dimension > 29:
                                print("Numero demasiado grande")
                                break
                        for i in range(1, dimension):
                            izquierda = "*" * i
                            centro = "  " * (dimension - i)
                            derecha = "*" * i
                            print(izquierda, centro, derecha)
                        for i in range(dimension, 0, -1):
                            izquierda = "*" * i
                            centro = "  " * (dimension - i)
                            derecha = "*" * i
                            print(izquierda, centro, derecha)
                    elif dimension % 2 == 0:
                        print("ERROR 002")
                else:
                    print("ERROR 003")
                break
        case 4:
            print("\n\n\n")
            while True:
                opcion = input("Relleno [si/no] < ")
                if opcion.lower() == "no":
                    while True:
                        asignacion_forma = input("Que signo desea utilizar < ")
                        if len(asignacion_forma) == 1:
                            break
                        elif len(asignacion_forma) == 2:
                            print("ERROR 002")
                    dimension = int(input("\nAsigna el tamaño [impar] < "))
                    if dimension % 2 == 1:
                        if dimension > 29:
                                print("Numero demasiado grande")
                                break
                        for i in range(dimension):
                            forma = "* " * (dimension + 2)
                        print(forma)
                        for i in range(dimension, 0, -1):
                            espacio = " " * (dimension - i + 1)
                            forma = " " * (2 * i - 1)
                            print(espacio + "*" + forma + "*")
                        for i in range(dimension):
                            print(" " * (dimension - i + i), "*")
                        for i in range(dimension):
                            espacio = "  " * (dimension - i)
                            forma = "*" * (2 * i - 1)
                        print(espacio, forma)
                    elif dimension % 2 == 0:
                        print("ERROR 002")
                elif opcion.lower() == "si":
                    while True:
                        asignacion_forma = input("Que signo desea utilizar < ")
                        if len(asignacion_forma) == 1:
                            break
                        elif len(asignacion_forma) == 2:
                            print("ERROR 002")
                    dimension = int(input("\nAsigna el tamaño [impar] < "))
                    if dimension % 2 == 1:
                        if dimension > 29:
                                print("Numero demasiado grande")
                                break
                        for i in range(dimension, 0, -1):
                            espacio = " " * (dimension - i)
                            forma = "*" * (2 * i - 1)
                            print(espacio, forma)
                        for i in range(dimension):
                            print(" " * (dimension - 1), "*")
                        for i in range(dimension):
                            espacio = " " * (dimension - i)
                            forma = "*" * (2 * i - 1)
                        print(espacio, forma)
                    elif dimension % 2 == 0:
                        print("ERROR 002")
                else:
                    print("ERROR 003")
                break


                                
                                    
                            
                            
    

print("----------------------\n* GENIO Y FIGURA *\n----------------------\n")

input("Presiona Enter para continuar ")
print("\n")

while True:
    proceso()

    reinicio = input("Reiniciar [si/no] < ")
    if reinicio != "si":
        print("Programa finalizado...")
        exit()