import json
import requests

URL = "https://api.open-meteo.com/v1/forecast"


def consultar_clima(lat, lon):
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,wind_speed_10m",
    }
    try:
        response = requests.get(URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Aviso: Error en la conexion. Detalle: {e}")
        return None


# Consultamos usando la función
datos_completos = consultar_clima(2.4419, -76.6063)

if datos_completos:
    # Opcional: imprime r.json() una vez para ver su estructura completa

    #  Guardamos la respuesta completa en clima.json
    with open("clima.json", "w", encoding="utf-8") as f:
        json.dump(datos_completos, f, indent=4, ensure_ascii=False)

    # Leemos el archivo y mostramos solo la temperatura
    with open("clima.json", "r", encoding="utf-8") as f:
        archivo_leido = json.load(f)
        temperatura = archivo_leido["current"]["temperature_2m"]
        print(f"Temperatura: {temperatura} °C")
