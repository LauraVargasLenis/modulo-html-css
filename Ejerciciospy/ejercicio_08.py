nota = int(input("Ingrese una nota de 0 a 100: "))

if nota >= 70:
    if nota>100:
        print("Ingrese una nota válida")
    else:    
        print("El estudiante está aprobado")
else:
    if nota<0:
        print("Ingrese una nota válida")
    else:
        print("El estudiante está reprobado")