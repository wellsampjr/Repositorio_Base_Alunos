# Escrever texto automaticamente

#importamos o pyautogui
import pyautogui
import time


#Press é um comando para pressionar uma tecla desejada
pyautogui.press("Win") #pressiona a tecla Windows


# 'Sleep' é um comando para esperar um tempo determinado
pyautogui.sleep(1) #espera 1 segundo

# 'Write' é um comando para escrever o que for desejado
pyautogui.write("Bloco de notas") #escreve "Bloco de notas"

pyautogui.press("Enter") #pressiona a tecla Enter


#Obs: abra um bloco de notas numa pagina em branco 
#Aguardar 5 segundos para voce abrir o bloco de notas

time.sleep(5)

#Escrever um texto 
pyautogui.write("Automatizando com PyAutoGUI", interval=0.1)