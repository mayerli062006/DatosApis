import json
import requests

URL = "https://api.open-meteo.com/v1/forecast"


# Funcion para consultar el clima con manejo de errores y timeout
def consultar_clima(lat, lon):
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m",
    }
    try:
        r = requests.get(URL, params=params, timeout=10)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException:
        return None


# Diccionario de ciudades con sus coordenadas
ciudades = {
    "Popayan": (2.4419, -76.6063),
    "Bogota": (4.7110, -74.0721),
    "Cali": (3.4516, -76.5320),
    "Medellin": (6.2442, -75.5812),
}

climas_exitosos = {}

# 1. Recorrer el diccionario y consultar la temperatura actual de cada ciudad
for ciudad, (lat, lon) in ciudades.items():
    resultado = consultar_clima(lat, lon)
    # 2. Si falla, muestra un aviso y continua con las demas sin detener el programa
    if resultado and "current" in resultado:
        temp = resultado["current"]["temperature_2m"]
        climas_exitosos[ciudad] = temp
        print(f"Consulta exitosa para {ciudad}: {temp} C")
    else:
        print(f"Aviso: No se pudo consultar el clima de {ciudad}.")

# 3. Guardar en clima_ciudades.json el diccionario con las temperaturas exitosas
with open("clima_ciudades.json", "w", encoding="utf-8") as f:
    json.dump(climas_exitosos, f, indent=4, ensure_ascii=False)

print("\nArchivo clima_ciudades.json guardado correctamente.\n")

# 4. Leer el archivo y mostrar cual es la ciudad mas calurosa
with open("clima_ciudades.json", "r", encoding="utf-8") as f:
    datos_guardados = json.load(f)

if datos_guardados:
    ciudad_calurosa = max(datos_guardados, key=datos_guardados.get)
    temp_maxima = datos_guardados[ciudad_calurosa]
    print(f"La ciudad mas calurosa es {ciudad_calurosa} con {temp_maxima} C.")
else:
    print("No hay datos suficientes para calcular la ciudad mas calurosa.")
