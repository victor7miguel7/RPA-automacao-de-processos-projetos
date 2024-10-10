# Quais passos seguir?
# Passo1 - entrar no navegador
# Passo2 - entrar no link 
# Passo3 - preencher login
# Passo4 - preencher senha
# Passo5 - confirmar no batão
# Passo6 - preencher produtos
# Passo7 - apertar botão de enviar

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
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

# entrar no site
pyautogui.press('enter')
time.sleep(3)

# muda para campo do email
pyautogui.click(x=474, y=411)

# preenche email
pyautogui.write("victor77miguel@gmail.com")

# altera para campo de senha
pyautogui.press('tab')

# escreve senha
pyautogui.write('senha_ficticia')

# alterna para botao de confirma
pyautogui.press('tab')

# confirma
pyautogui.press('enter')

# alterna para campo de codigo
#pyautogui.press('tab')

# importar tabela para ver produtos à serem cadastrados

import pandas as pd

df = pd.read_csv('produtos.csv')
print(df)

for linha in df.index:
    time.sleep(1.5)
    # alterna para campo de codigo
    pyautogui.click(x=586, y=300)
    # captura célula desejada 
    codigo_valor = str(df.loc[linha,'codigo'])
    # escreve valor da celula no campo de codigo
    pyautogui.write(codigo_valor)

    # pula para proxima celula
    pyautogui.press('tab')

    # captura célula desejada
    marca_valor = str(df.loc[linha, 'marca'])
    # escreve valor da celula
    pyautogui.write(marca_valor)

    # pula para proxima celula
    pyautogui.press('tab')

    # captura célula desejada
    tipo_valor = str(df.loc[linha, 'tipo'])
    # escreve valor da celula
    pyautogui.write(tipo_valor)

    # pula para proxima celula
    pyautogui.press('tab')

    # captura célula desejada
    categoria_valor = str(df.loc[linha, 'categoria'])
    # escreve valor da celula
    pyautogui.write(categoria_valor)

    # pula para proxima celula
    pyautogui.press('tab')

    # captura célula desejada
    preco_unitario_valor = str(df.loc[linha, 'preco_unitario'])
    # escreve valor da celula
    pyautogui.write(preco_unitario_valor)

    # pula para proxima celula
    pyautogui.press('tab')

    # captura célula desejada
    custo_valor = str(df.loc[linha, 'custo'])
    # escreve valor da celula
    pyautogui.write(custo_valor)

    # pula para proxima celula
    pyautogui.press('tab')

    # captura célula desejada
    obs_valor = df.loc[linha, 'obs']
    if not pd.isna(obs_valor):
        # escreve valor da celula
        pyautogui.write(obs_valor)

    # pula para proxima celula
    pyautogui.press('tab')

    # envia
    pyautogui.press('enter')

    # rola para o topo 
    pyautogui.scroll(5000)