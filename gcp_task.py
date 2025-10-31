import asyncio
import httpx

# Lista de APIs a consultar
APIS = [
    "https://api.coindesk.com/v1/bpi/currentprice.json",  # API de precio de Bitcoin
    "https://dog.ceo/api/breeds/image/random"  # API de imágenes aleatorias de perros
]

# Función asíncrona para hacer peticiones HTTP
async def fetch(url):
    try:
        # Crea un cliente HTTP asíncrono con timeout
        async with httpx.AsyncClient(timeout=10.0) as client:
            # Realiza la petición GET y espera la respuesta
            r = await client.get(url)
            r.raise_for_status()  # Lanza excepción si el código de estado es 4xx o 5xx
            # Retorna un diccionario con la URL y los datos JSON de la respuesta
            return {url: r.json()}
    except httpx.TimeoutException:
        return {url: {"error": "La petición excedió el tiempo de espera"}}
    except httpx.HTTPStatusError as e:
        return {url: {"error": f"Error HTTP: {e.response.status_code}"}}
    except httpx.RequestError as e:
        return {url: {"error": f"Error de conexión: {str(e)}"}}
    except Exception as e:
        return {url: {"error": f"Error inesperado: {str(e)}"}}

# Función principal que coordina las tareas asíncronas
async def main():
    # Ejecuta todas las peticiones de forma concurrente usando asyncio.gather
    # return_exceptions=True permite que continúe aunque una tarea falle
    results = await asyncio.gather(*(fetch(url) for url in APIS), return_exceptions=True)
    
    # Imprime los resultados de cada petición
    for result in results:
        print(result)

# Punto de entrada del script
if __name__ == "__main__":
    # Ejecuta la función principal usando el event loop de asyncio
    asyncio.run(main())
