def dividir_seguro(a, b):
    try:
        return a // b
    except ZeroDivisionError:
        print("Aviso: No se puede dividir entre cero.")
        return None


# Pruebas requeridas
print("Resultado 10 / 2:", dividir_seguro(10, 2))
print("Resultado 5 / 0:", dividir_seguro(5, 0))
