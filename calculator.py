
print("================================")
print("        CALCULADORA")
print("================================")

while True:
    print("\nSeleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Descuento")
    print("7. Salir")

    opcion = input("\nOpción: ")

    if opcion == "7":
        print("Calculadora finalizada.")
        break

    if opcion not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Opción no válida.")
        continue

    try:
        if opcion == "6":
            precio = float(input("Ingrese el precio original: "))
            porcentaje = float(input("Ingrese el porcentaje de descuento: "))

            if precio < 0:
                print("Error: el precio no puede ser negativo.")
                continue

            if porcentaje < 0 or porcentaje > 100:
                print("Error: el descuento debe estar entre 0 y 100.")
                continue

            resultado = precio - (precio * porcentaje / 100)

            print("Descuento aplicado:", porcentaje, "%")
            print("Precio original:",precio)
            print("Precio final:",round(resultado, 2))
            continue

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == "1":
            resultado = num1 + num2
        elif opcion == "2":
            resultado = num1 - num2
        elif opcion == "3":
            resultado = num1 * num2
        elif opcion == "4":
            if num2 == 0:
                print("Error: no se puede dividir entre cero.")
                continue
            resultado = num1 / num2
        elif opcion == "5":
            resultado = num1 ** num2

        print("Resultado:", resultado)

    except ValueError:
        print("Error: ingrese un número válido.")
