# Creamos la lista para ventas
ventas = [45000, 120000, 8000, 300000]

# Cuardamos ventas en un archivo
with open("ventas.txt", "w", encoding="utf-8") as f:
    for venta in ventas:
        f.write(str(venta) + "\n")

# Leemos las ventas
ventas_leidas = []

with open("ventas.txt", "r", encoding="utf-8") as f:
    for linea in f:
        valor = int(linea.strip())
        ventas_leidas.append(valor)

# Calculamos el total
total = sum(ventas_leidas)

print("Total de ventas:", total)
