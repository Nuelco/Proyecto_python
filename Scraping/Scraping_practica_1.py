import requests
from bs4 import BeautifulSoup

url = "https://es.wikipedia.org/wiki/Mat%C3%ADas_Corvino"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Verificar si encontramos el título
titulo = soup.find("h1")
print("Título encontrado:", titulo.text)


parrafos=soup.find_all("p")
for p in parrafos:
    print(p.text)