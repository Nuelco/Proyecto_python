import requests
from bs4 import BeautifulSoup
import time

url = "https://es.wikipedia.org/wiki/Mat%C3%ADas_Corvino"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

# Añadir un pequeño retraso antes de hacer la solicitud
time.sleep(1)

try:
    response = requests.get(url, headers=headers)
    print(f"Status code: {response.status_code}")
    
    # Verificar si la solicitud fue exitosa
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Verificar si encontramos el título
    titulo = soup.find("h1", {"id": "firstHeading"})
    if titulo is None:
        print("No se pudo encontrar el título (h1)")
    else:
        print("Título encontrado:", titulo.text.strip())
    
    # Buscar y mostrar los párrafos
    parrafos = soup.find_all("p")
    if not parrafos:
        print("No se encontraron párrafos")
    else:
        print(f"Se encontraron {len(parrafos)} párrafos:")
        for p in parrafos:
            if p.text.strip():  # Solo imprimir párrafos que no estén vacíos
                print("---")
                print(p.text.strip())

except requests.exceptions.RequestException as e:
    print(f"Error al hacer la solicitud: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")