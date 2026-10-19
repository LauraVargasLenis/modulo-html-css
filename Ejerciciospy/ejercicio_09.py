precio = float(input("Ingrese el precio de la compra: "))

if precio>=200000:
    print("El monto a pagar es: "+ str(precio*0.8))
elif 100000<=precio<200000:
    print("El monto a pagar es: "+ str(precio*0.9))
else:
    print("El monto a pagar es: "+ str(precio))