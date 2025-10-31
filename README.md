## Script Asíncrono para Llamar APIs con Python
Este script asíncrono en Python realiza peticiones concurrentes a dos APIs diferentes utilizando las bibliotecas asyncio y httpx.
## APIs Utilizadas
### CoinDesk API: Proporciona el precio actual de Bitcoin en diferentes monedas.
- URL: https://api.coindesk.com/v1/bpi/currentprice.json
### Dog CEO API: Devuelve una imagen aleatoria de un perro.

- URL: https://dog.ceo/api/breeds/image/random
## Características del Código
- Implementa concurrencia usando async/await y asyncio.gather

- Utiliza httpx.AsyncClient para realizar peticiones HTTP asíncronas

- Formatea los resultados en diccionarios con la URL como clave

- Maneja errores de forma implícita a través del contexto del cliente HTTP

## Requisitos
- Python 3.7 o superior
- Biblioteca httpx
## Instalación de Dependencias
```bash
pip install httpx
```
## Ejecución
```
python3 gcp_task.py
```
## Salida Esperada
El script imprimirá los resultados de ambas APIs en formato de diccionario:
```
{
    'https://api.coindesk.com/v1/bpi/currentprice.json': {
        'time': {...},
        'disclaimer': '...',
        'bpi': {...}
    }
}
{
    'https://dog.ceo/api/breeds/image/random': {
        'message': 'https://images.dog.ceo/breeds/...',
        'status': 'success'
    }
}
```
