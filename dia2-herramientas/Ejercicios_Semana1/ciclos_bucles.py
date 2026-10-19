#EJERCICIO 1
#Cuenta regresiva

#num = int(input("Ingresa un número: "))

#while num >0:
#    print(num)
#    num -= 1

#print("¡Despegue!")


##EJERCICIO 2
#Suma del 1 al n

#n = int(input("Ingrese un número: "))
#suma = 0

#for i in range(1,n+1):
#    suma = suma + i

#print(suma)

##EJERCICIO 3
#Tabla de multiplicar

#n = int(input("Ingrese un número: "))
#c= 1

#while c <=10:
#    print(n, " x ", c, " = ", (n*c))
#    c += 1


##EJERCICIO 4
#Contador de vocales

vocales = ["a","e","i","o","u"]
c = 0

text = (input("Ingrese un texto: ")).lower()

for letra in (text):
    if letra in vocales:
        c += 1
    else: 
        continue

print(c)
