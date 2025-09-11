import pyautogui
import time 

pyautogui.press("Win") #pressiona a tecla Windows

pyautogui.sleep(1) #espera 1 segundo    

pyautogui.write("Calculadora") #pesquisa por "Calculadora"
pyautogui.press("Enter") #pressiona a tecla Enter

time.sleep(3) 

pyautogui.press("8")    #pressiona o número 8
pyautogui.press("+")    #pressiona o símbolo de adição
pyautogui.press("5")    #pressiona o número 5   
pyautogui.press("=")    #pressiona o símbolo de igual    