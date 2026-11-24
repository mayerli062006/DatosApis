import json


# Definición de la clase CarritoCompras con los métodos requeridos
class CarritoCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, precio, cantidad):
        self.productos.append(
            {"producto": producto, "precio": precio, "cantidad": cantidad}
        )

    def guardar(self, archivo):
        # Guarda los productos en un archivo JSON en la misma carpeta
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(self.productos, f, indent=4, ensure_ascii=False)

    def cargar(self, archivo):
        # Lee los productos de vuelta desde el archivo JSON
        with open(archivo, "r", encoding="utf-8") as f:
            self.productos = json.load(f)


# Creamos el primer carrito, le agregamos productos y lo guardamos
carrito1 = CarritoCompras()
carrito1.agregar_producto("Mochila", 75000, 1)
carrito1.agregar_producto("Cuaderno", 12000, 3)
carrito1.guardar("carrito.json")

# Creamos un segundo carrito vacío y cargamos la información del archivo
carrito2 = CarritoCompras()
carrito2.cargar("carrito.json")

print("Productos cargados en el segundo carrito:")
print(carrito2.productos)
