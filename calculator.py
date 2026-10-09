
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
    print("6. Salir")

    opcion = input("\nOpción: ")

    if opcion == "6":
        print("Calculadora finalizada.")
        break

    if opcion not in ["1", "2", "3", "4", "5"]:
        print("Opción no válida.")
        continue

    try:
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