saldo = 500000
opcion = 0

while opcion != 4:
    print("1. Consultar saldo\n2. Retirar dinero\n3. Depositar dinero\n4. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("Su saldo es: ", saldo)

    elif opcion == 2:
        retiro = float(input("Valor a retirar: "))
        if retiro <= 0:
            print("El valor debe ser mayor que cero")
        elif retiro > saldo:
            print("Saldo insuficiente")
        else:
            saldo = saldo - retiro
            print("Retiro exitoso. Saldo actual: ", saldo)

    elif opcion == 3:
        deposito = float(input("Valor a depositar: "))
        if deposito > 0:
            saldo = saldo + deposito
            print("Depósito exitoso. Saldo actual: ", saldo)
        else:
            print("El valor debe ser mayor que cero")

    elif opcion == 4:
        print("Gracias por usar el cajero")

    else:
        print("Opción no válida")