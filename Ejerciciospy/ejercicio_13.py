print("CALCULADORA")
print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir")

opcion = int(input("Seleccione una opción: "))

if 1 <= opcion <= 4:
    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))

    if opcion == 1:
        resultado = num1 + num2
    elif opcion == 2:
        resultado = num1 - num2
    elif opcion == 3:
        resultado = num1 * num2
    elif num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "No se puede dividir entre cero"

    print("Resultado:", resultado)
else:
    print("Opción no válida")