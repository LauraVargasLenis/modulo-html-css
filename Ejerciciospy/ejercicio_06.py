n1= float(input("Ingrese un número: "))
n2= float(input("Ingrese un número: "))

operacion = input("Teniendo en cuenta que:"
"\nsuma = +" \
"\nresta = -" \
"\nmultiplicación = *" \
"\ndivisión = /" \
"\n \nIngrese que operación desea realizar: ")

if operacion == "/":
    if n2 == 0:
        print("No se puede dividir entre cero")
    else:
        print("n1/n2")

elif operacion == "*":
    print (n1*n2)

elif operacion == "+":
    print(n1+n2) 

elif operacion == "-":
    print(n1-n2)

else:
    print("Digite un símbolo de operación válido")