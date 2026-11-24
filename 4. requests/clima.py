import requests

# URL de la API pública de Open-Meteo
URL = "https://api.open-meteo.com/v1/forecast"

# Parámetros para Popayán y los datos actuales que queremos consultar
params_popayan = {
    "latitude": 2.4419,
    "longitude": -76.6063,
    "current": "temperature_2m,wind_speed_10m"
}

# Realizamos la petición GET a la API
r = requests.get(URL, params=params_popayan)
data = r.json()

# Imprimimos la temperatura y la velocidad del viento con sus unidades
print("Clima de Popayán")
print(f"Temperatura actual: {data['current']['temperature_2m']} °C")
print(f"Velocidad del viento: {data['current']['wind_speed_10m']} km/h")