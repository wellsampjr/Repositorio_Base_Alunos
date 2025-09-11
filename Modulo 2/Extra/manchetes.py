import requests
from bs4 import BeautifulSoup

# URL do site de notícias
url = "https://g1.globo.com/"

# Fazer requisição HTTP
resposta = requests.get(url)
resposta.raise_for_status()  # Garante que não houve erro

# Criar objeto BeautifulSoup
soup = BeautifulSoup(resposta.text, "html.parser")

# Coletar as manchetes (G1 usa a classe 'feed-post-link')
manchetes = soup.find_all("a", class_="feed-post-link")

print(f"Manchetes do {url}\n")
for i, manchete in enumerate(manchetes, start=1):
    print(f"{i}. {manchete.get_text(strip=True)}")
