import requests

URL = "https://api.open-meteo.com/v1/forecast"

def consultar_clima(lat, lon):
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,wind_speed_10m"
    }
    try:
        # timeout=10 detiene la espera si la red falla; raise_for_status detecta errores HTTP
        response = requests.get(URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Aviso: Error en la conexion. Detalle: {e}")
        return None

# Prueba de la función
print("Funcion consultar_clima")
resultado = consultar_clima(2.4419, -76.6063)
if resultado:
    print("Consulta exitosa") 
    
    
    
    