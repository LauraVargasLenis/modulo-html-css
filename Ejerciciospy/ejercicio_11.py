temp = float(input ("Ingrese la temperatura en °C: "))

if temp<10:
    print("frío")
elif 10<=temp<25:
    print("templado")
elif 25<=temp<30:
    print("caluroso")
else:
    print("muy caluroso")