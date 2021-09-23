#abrir o g drive no meu pc
#entrar na area de trabalho
#2 - pegar o arquivo e arrastar
import pyautogui
import time
pyautogui.alert('nao use o mouse e teclado enquanto o codigo e executado')
pyautogui.PAUSE = 0.5#faz o programa esperar 0.5 segundos
#entrar no navegdor
pyautogui.press('winleft')
pyautogui.write('firefox')
pyautogui.press('enter')
time.sleep(1)
#realizar a pésquisa necessaria
pyautogui.write('noticias de hoje')
pyautogui.press('enter')
