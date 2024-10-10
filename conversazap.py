# Quais passos seguir?
# Passo1 - entrar no navegador
# Passo2 - entrar no link do whatsapp
# Passo3 - encontrar conversa desejada
# Passo4 - escrever mensagem
# Passo5 - enviar

import time
import pyautogui

# pyautogui.click -> clica com o mouse
# pyautogui.write -> escreve
# pyautogui.scroll -> rola a tela
# pyautogui.press -> pressiona uma tecla
pyautogui.PAUSE = 0.5

# abrir windows
pyautogui.press('win')

# escrever chrome
pyautogui.write('chrome')

# clicar no navegador
pyautogui.press('enter')

# escrever no navegador o endereço
pyautogui.write("https://web.whatsapp.com/")

# entrar no site
pyautogui.press('enter')
time.sleep(10)
# clicar na barra de pesquisas
pyautogui.click(x=299, y=207)

# escrever o nome do contato
pyautogui.write('Pedro')

# tab p mudar de posicao 1
pyautogui.press('tab')

# tab p mudar de posicao 2
pyautogui.press('tab')

# tab p mudar de posicao 3
pyautogui.press('tab')

# tab p mudar de posicao 4
pyautogui.press('tab')

# tab p mudar de posicao 5
pyautogui.press('tab')

# clica no campo de enviar mensagem
pyautogui.click(x=629, y=691)

# escreve a mensagem
pyautogui.write("Oi, boa noite!")

# envia mensagem
pyautogui.press("enter")