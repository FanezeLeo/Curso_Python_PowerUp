import pyautogui
import time
import pandas


#pyautogui.press: pressiona um botão
#pyautogui.write: escreve um texto
#pyautogui.click: click do mouse
#pyautogui.hotkey: atalho (combinação de tecla)
#pyautogui.PAUSE: delay entre cada comando
#pyautogui.sleep: somente um delay nesse ponto

pyautogui.PAUSE = 0.2

pyautogui.press("win") 
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(2)

pyautogui.click(x=598, y=593)

pyautogui.write("email@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.press("tab")
pyautogui.press("enter")

tabela = pandas.read_csv("produtos.csv")
time.sleep(2)

for linha in tabela.index:
    pyautogui.click(x=561, y=421)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
