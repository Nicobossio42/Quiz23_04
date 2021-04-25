Vec1 = int(input("Ingresa el tamaño de los arreglos: "))
Almacenaje1 = []
Almacenaje2 = []
for i in range (0,Vec1):
 Almacenaje1.append(input("Ingresa el nombre de las personas: "))
print(Almacenaje1)
for j in range (0,Vec1):
 Almacenaje2.append(len(Almacenaje1[j]))
print(Almacenaje2)
