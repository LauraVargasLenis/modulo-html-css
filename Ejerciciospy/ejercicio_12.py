l1 = float(input("Ingrese el valor del lado 1: "))
l2 = float(input("Ingrese el valor del lado 2: "))
l3 = float(input("Ingrese el valor del lado 3: "))

if l1==l2==l3:
  print("Triángulo equilátero")

elif (l1==l2 and l2!=l3) or (l1==l3 and l3!=l2) or (l3==l2 and l1!=l3):
  print("Triángulo isóceles")

else:
  print("Tríangulo escaleno")