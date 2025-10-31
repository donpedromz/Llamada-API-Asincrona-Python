import asyncio
import httpx

# Lista de APIs a consultar
APIS = [
    "https://api.coindesk.com/v1/bpi/currentprice.json",  # API de precio de Bitcoin
    "https://dog.ceo/api/breeds/image/random"  # API de imágenes aleatorias de perros
]

# Función asíncrona para hacer peticiones HTTP
async def fetch(url):
    # Crea un cliente HTTP asíncrono
    async with httpx.AsyncClient() as client:
        # Realiza la petición GET y espera la respuesta
        r = await client.get(url)
        # Retorna un diccionario con la URL y los datos JSON de la respuesta
        return {url: r.json()}

# Función principal que coordina las tareas asíncronas
async def main():
    # Ejecuta todas las peticiones de forma concurrente usando asyncio.gather
    results = await asyncio.gather(*(fetch(url) for url in APIS))
    
    # Imprime los resultados de cada petición
    for result in results:
        print(result)

# Punto de entrada del script
if __name__ == "__main__":
    # Ejecuta la función principal usando el event loop de asyncio
    asyncio.run(main())
