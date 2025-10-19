import aiohttp
import asyncio
import os
import time
from dotenv import load_dotenv
async def async_api_call(url, params, total_timeout=60):
	try:
		timeout = aiohttp.ClientTimeout(total=total_timeout)
		async with aiohttp.ClientSession(timeout=timeout) as session, session.get(url, params=params) as response:
			response.raise_for_status()
			data = await response.json()
			return data
	except Exception as e:
		print(f"Error al llamar la api: {e}")
async def movies_api_call(movie_name:str, limit:int):
	movie_api_recomendation_url = "https://tastedive.com/api/similar"
	if limit > 20 or limit < 0:
		raise ValueError("Limite incorrecto")
	movie_params = {
		"q": movie_name,
		"type": "movie",
		"info":0,
		"limit":limit,
		"k":movies_api_key
	}
	data = await async_api_call(movie_api_recomendation_url, params=movie_params)
	if not data:
		print("Error al llamar a la API de peliculas")
		return
	print("---- Resultados de la llamada a la API de peliculas -----")
	print(f"Recomendaciones para: {movie_name}")
	index = 0
	for recomendation in data["similar"]["results"]:
		name = recomendation["name"]
		print(f"Recomendacion[{index}]: {name}")
		index += 1
async def number_validation_api_call(phone_number:str, country_code:str):
	number_validation_url = "http://apilayer.net/api/validate"
	number_validation_params={
		"access_key":number_validation_key,
		"number":phone_number,
		"country_code":country_code,
		"format":1
	}
	data = await async_api_call(number_validation_url, number_validation_params)
	if not data:
		print("Error al llamara a la API de validacion de teléfonos")
		return
	print("---- Resultados llamada a la API de validacion de telefonos ----")
	if not data["valid"]:
		print(f"El numero de teléfono: {phone_number} no es válido según la API")
	else:
		prefix = data["country_prefix"] or "Sin info del Prefijo"
		country_name = data["country_name"] or "Sin info del País"
		carrier = data["carrier"] or "Sin info del Operador"
		line_type = data["line_type"] or "Sin info del tipo de linea"
		print(f"El número de teléfono: {phone_number} es válido según la API, y posee la siguiente información:")
		print(f"Prefijo del pais: {prefix}")
		print(f"Nombre del pais: {country_name}")
		print(f"Operador: {carrier}")
		print(f"Tipo de linea: {line_type}")
async def main():
	results = await asyncio.gather(
		movies_api_call("Pride and Prejudice", 5),
		movies_api_call("The Shining",5),
		number_validation_api_call("3043945372","CO"),
		number_validation_api_call("3164909496", "CO")
	)
# --- Cargar Variables de entorno
load_dotenv()
movies_api_key = os.getenv("MOVIES_API_KEY")
number_validation_key = os.getenv("NUMBER_VALIDATION_API_KEY")
# --- Ejecutar el programa
start = time.time()
asyncio.run(main())
end = time.time()
print("-"*10)
print(f"Tiempo total de ejecución: {end-start:.2f}s")
