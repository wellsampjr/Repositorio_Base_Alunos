import requests
from bs4 import BeautifulSoup
import json
import time
import pyautogui

# 1. URL da página
url = "https://ge.globo.com/futebol/libertadores/"

# 2. Requisição HTTP
response = requests.get(url)
response.encoding = response.apparent_encoding  # Detecta automaticamente


# 3. Parse HTML
soup = BeautifulSoup(response.content, 'html.parser')


# 4. Extrair dados
titulo = soup.title.string if soup.title else "Sem título"
paragrafo = soup.find('p')
primeiro_paragrafo = paragrafo.text if paragrafo else "Nenhum parágrafo encontrado"

# 5. Montar e salvar JSON
dados = {"titulo": titulo, "primeiro_paragrafo": primeiro_paragrafo}
dados_json = json.dumps(dados, indent=4, ensure_ascii=False)

with open("python_geglobo.json", "w", encoding="utf-8") as f:
    f.write(dados_json)

# 6. Usar pyautogui para digitar no terminal
print("Abra o terminal, posicione o cursor e aguarde...")
time.sleep(5)
pyautogui.write(dados_json, interval=0.01)

print("\n\nConteúdo digitado no terminal com sucesso!")
