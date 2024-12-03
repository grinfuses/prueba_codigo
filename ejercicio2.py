#Importamos las librerías necesarias
import requests
import json

# Url del endpoint para la solicitud
direccion_endpoint = "https://jsonplaceholder.typicode.com/posts"

try:
    # Realizamos la petición
    respuesta = requests.get(direccion_endpoint)
    
    # Vemos si es correcta
    if respuesta.status_code == 200:
        # Convertimos la respuesta a JSON
        total_posts = respuesta.json()
        
        # Mostrar el JSON completo
        print("Resultados completos en formato JSON:")
        print(json.dumps(total_posts, indent=4))  # Se formatea la respuesta para que sea legible
        
        # Se muestra el título del primer post en el caso que existan
        if total_posts:
            print("Título del post:")
            print(total_posts[0]["title"])
        else:
            print("No hay posts en la dirección.")
    else:
        print(f"Error de solicitud con código de estado {respuesta.status_code}")
except requests.RequestException as e:
    print(f"Error al realizar la solicitud: {e}")