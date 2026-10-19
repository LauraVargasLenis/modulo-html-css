name = input("Ingrese el nombre dle cliente: ")
producto = input("Ingrese el producto: ")
price = float(input("Valor del producto: "))
cant = int(input("Ingrese la cantidad: "))

total = price * cant
descuento = 0

if total >= 500000:
  descuento = total * 0.15

elif 200000 <= total < 500000:
  descuento = total * 0.1

else:
  descuento = 0


print("FACTURA\n\nCliente: " + name + "\n\n" + "\nPRODUCTO    CANTIDAD    PRECIO\n" + producto + "         " + str(cant) + "           " + str(price) + "\n\nSubtotal: " + str(total) + "\nDescuento: " + str(descuento) + "\nTOTAL A PAGAR: " + str(total))
