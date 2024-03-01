import requests

def obtener_datos_evaluacion(param:dict):
    url= 'http://localhost:8000/webhook'
    # Hacer una solicitud GET a la URL especificada con los parámetros dados
    response = requests.get(url, params=param)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Obtener los datos de la respuesta
        data = response
        return  data
    else:
        return "Error al realizar la obtencion"

# Ejemplo de uso de la función



