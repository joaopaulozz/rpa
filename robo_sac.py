import webbrowser
import pyautogui
import time
import os

#Abrindo a url no seu navegador
webbrowser.open('https://colchoescastor.com.br/sac/')

#espero um tempo pre determinado para o site carregar
time.sleep(10)

#movendo o mouse para rolar a pagina
pyautogui.moveTo(1350, 500, duration=0.25)
time.sleep(2)
pyautogui.click(1350, 500, button='left', duration=0.25)

time.sleep(2)

# Onde identifico a posicao dos checkbox, atraves de imagem
#primeiro_checkbox = pyautogui.locateOnScreen('declaro.png')
#if primeiro_checkbox:
#    print(primeiro_checkbox)
#    time.sleep(10)

#segundo_checkbox = pyautogui.locateOnScreen('aceito.png')
#if segundo_checkbox:
#    print(segundo_checkbox)
#    time.sleep(10)

pyautogui.click(273, 270, button='left', duration=0.25)
time.sleep(2)
pyautogui.click(271, 408, button='left', duration=0.25)

#proximo
pyautogui.hotkey('enter')

#preenchendo o nome
time.sleep(1)
pyautogui.typewrite('Joao Paulo de Oliveira')
pyautogui.hotkey('tab')

#preenchendo o email
time.sleep(1)
pyautogui.typewrite('joaopaulooliveiira@hotmail.com')
pyautogui.hotkey('tab')

#preenchendo o cpf
time.sleep(1)
pyautogui.typewrite('44444488899')
pyautogui.hotkey('tab')

#preenchendo o telefone
time.sleep(1)
pyautogui.typewrite('1433245728')
pyautogui.hotkey('tab')

#preenchendo o celular
time.sleep(1)
pyautogui.typewrite('14996889678')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

#preenchendo o logradouro - como pode ser nulo, ignoro
time.sleep(1)
pyautogui.hotkey('down')
pyautogui.press('enter')
pyautogui.hotkey('tab')

#preenchendo o celular
time.sleep(1)
pyautogui.typewrite('Joaozinho da Silva')
pyautogui.hotkey('tab')

#preenchendo o bairro
time.sleep(1)
pyautogui.typewrite('Jardins')
pyautogui.hotkey('tab')

#preenchendo o numero da casa
time.sleep(1)
pyautogui.typewrite('44')
pyautogui.hotkey('tab')

#preenchendo o complemento
time.sleep(1)
pyautogui.typewrite('casa')
pyautogui.hotkey('tab')

#preenchendo o logradouro
time.sleep(1)
pyautogui.hotkey('down')
pyautogui.press('enter')
pyautogui.hotkey('tab')
pyautogui.hotkey('down')
pyautogui.press('enter')
pyautogui.hotkey('tab')

#preenchendo o cep
time.sleep(1)
pyautogui.typewrite('19906000')
pyautogui.hotkey('tab')

#preenchendo o modelo do colchao
time.sleep(1)
pyautogui.typewrite('Pocket')
pyautogui.hotkey('tab')

#preenchendo o cod de barras
time.sleep(1)
pyautogui.hotkey('del')
pyautogui.hotkey('del')
pyautogui.hotkey('del')
pyautogui.hotkey('del')
pyautogui.hotkey('del')
pyautogui.hotkey('del')
pyautogui.hotkey('del')
pyautogui.typewrite('7895606986048')
pyautogui.hotkey('tab')

#preenchendo o lote
time.sleep(1)
pyautogui.typewrite('66887')
pyautogui.hotkey('tab')

#preenchendo a data
time.sleep(1)
pyautogui.press('enter')
pyautogui.hotkey('tab')

#preenchendo a medida
time.sleep(1)
pyautogui.typewrite('198cm')
pyautogui.hotkey('tab')

#preenchendo a nf
time.sleep(1)
pyautogui.typewrite('17054')
pyautogui.hotkey('tab')

#preenchendo a data
time.sleep(1)
pyautogui.press('enter')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

#preenchendo a reclamacao
time.sleep(1)
pyautogui.typewrite('Cholchao apresentando afundamento')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

#enviando formulario
time.sleep(2)
pyautogui.press('enter')
