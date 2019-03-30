n = int(input("Ingrese la cantidad de datos "))
suma = 0
for i in range(n):
    x = float(input("Ingrese Nota: "))
    suma = suma + x
    prom = suma / n 
print ("El promedio es: ",prom)