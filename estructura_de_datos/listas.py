Estudiantes = ["Elizabeth", "Jose", "Alejandro", "Pacho", "Camila","Jose"]
print (Estudiantes)
# print(f"El primrer elemento de la lista es {Estudiantes[0]}")
# print(f"El ultimo elemento de la lista es {Estudiantes[4]}")
# print(f"Cantidad de elemento de la lista es ", len(Estudiantes))
# print(f"El ultimo elemento de la lista es {Estudiantes[len(Estudiantes)-1]}")

# Estudiantes.append("David")
# print(Estudiantes)

# print("Lista ordenada alfabeticamente ")
# Estudiantes.sort()
# print(Estudiantes)
# Estudiantes.append("Julian") ubicacion final
# print(Estudiantes)

# Estudiantes.insert(2, "Alexander")  se ubica donde se le de la orden
# print(Estudiantes)

# Estudiantes.remove("Jose") remueve
# print(Estudiantes)

# print("Números de veces que se encuentra Jose en la lista ", Estudiantes.count("Jose"))

# for indice in Estudiantes: imprimir en lista
#     print(indice)
i=1
for indice in Estudiantes:
    print(f"{i}{indice}")
    i = i + 1