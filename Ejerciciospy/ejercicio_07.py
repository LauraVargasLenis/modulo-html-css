edad= int(input("Ingresa tu edad: "))

if edad >=18:
    print("Puede ingresar")
elif edad <18 and edad>=0:
    print("No puede ingresar")
else:
    print("Ingrese un número positivo")
    