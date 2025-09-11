import pyautogui
from datetime import datetime
import time     
import webbrowser

# Gerar nome do arquivo com data e hora
agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
nome_arquivo = f"screenshot_{agora}.png"

# abrir o navegador na link desejado
url = "https://www.uol.com.br/"
webbrowser.open(url)

# Aguardar o carregamento da página
time.sleep(5)

# Tirar o print da tela
screenshot = pyautogui.screenshot()

# Salvar o print
screenshot.save(nome_arquivo)

print(f"Screenshot salva como {nome_arquivo}")
