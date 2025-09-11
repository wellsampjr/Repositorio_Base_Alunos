# importamos a biblioteca pyautogui
import pyautogui

#Criamos um loop de 10  repetições para mover o mouse na forma de quadrado que se move 

for i in range(10):
    pyautogui.moveTo(300 + 10 * i, 300 + 10 * i, duration=0.25)
    pyautogui.moveTo(600 + 10 * i, 300 + 10 * i, duration=0.25)
    pyautogui.moveTo(600 + 10 * i, 600 + 10 * i, duration=0.25)
    pyautogui.moveTo(300 + 10 * i, 600 + 10 * i, duration=0.25)
