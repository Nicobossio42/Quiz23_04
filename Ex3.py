subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"] #se genera una lista con las materias
Resultado = [] #Se genera la lista
for subject in subjects:
    score = input("¿Qué nota has sacado en " + subject + "?")
    Resultado.append(score)
for num in range(len(subjects)):
    print("En " + subjects[num] + " has sacado " + Resultado[num])