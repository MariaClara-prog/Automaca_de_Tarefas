#Passo 1: Abrir o navegador
import pyautogui
import time

#PAUSE significa uma pausa entre os comandos
pyautogui.PAUSE = 1.0

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "n")


#Passo 2: Acessar o site do sistema com login e senha
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
time.sleep(2)
pyautogui.press("enter")    



time.sleep(1)
pyautogui.click(x=851, y=459)
pyautogui.write("claramarialy@gmail.com")
pyautogui.press("tab")
pyautogui.write("suasenha")
pyautogui.press("tab")
pyautogui.press("enter")


#Passo 3: Importar a base de dados
import pandas 
tabela = pandas.read_csv ("produtos.csv")
linha = 0   

#Passo 4: Inserir as informações de 1 produto
for linha in tabela.index:
    pyautogui.click(x=923, y=326)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
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

    if not pandas.isna (obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)

    
    
    
    
    

