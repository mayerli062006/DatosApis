# Lista de estudiantes
estudiantes = ["Carlos", "Ana", "Luis"]

# Guardar los nombres
with open("estudiantes.txt", "w", encoding="utf-8") as f:
    for nombre in estudiantes:
        f.write(nombre + "\n")

# Leer el archivo e imprimir cada nombre con su número
print(" Lista inicial de estudiantes")
with open("estudiantes.txt", "r", encoding="utf-8") as f:
    for i, linea in enumerate(f, start=1):

        print(i, linea.strip())


#  Agregar sin borrar
with open("estudiantes.txt", "a", encoding="utf-8") as f:
    f.write("Marta\n")

# Comprobar la lista actualizada leyendo de nuevo
print("\n Despues de agregar a Marta ")
with open("estudiantes.txt", "r", encoding="utf-8") as f:
    for i, linea in enumerate(f, start=1):
        print(i, linea.strip())
# Leemos el archivo
with open("estudiantes.txt", "r", encoding="utf-8") as f:
    estudiantes = f.readlines()

    # Contamos los estudiantes
    cantidad = len(estudiantes)

    print("\n Cantidad de estudiantes:", cantidad)