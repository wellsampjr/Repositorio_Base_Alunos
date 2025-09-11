import pyautogui        
import time

print("Voce tem 10 segundos para posicionar o mouse sobre o botao escrever ")

time.sleep(10)  

print("Posição do mouse: ", pyautogui.position())