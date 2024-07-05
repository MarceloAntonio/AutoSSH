
#
#instalar python em https://www.python.org/downloads/
#
#instalar o pip: python get-pip.py (cmd)
#
#caso não funcione, siga o tutorial
#
#Passo 1 no cmd digite: curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py (para baixar o instalador do pip) 
#
#Passo 2 no cmd digite: python get-pip.py (para executar a instalação)
#
#passo 3 no cmd digite: pip --version (para verificar se baixou)
#


import pyautogui as pa
import time

pa.PAUSE = 1.2

pa.hotkey("win","r") #abrir executar

pa.write("cmd") #digitar cmd

pa.press("enter")

pa.write("ssh user@ip") #altere para seu user e ip | exemplo: ssh marcelo@127.0.0.1

pa.press("enter")

time.sleep(0.5)

pa.write("senha") #altere para sua senha

pa.press("enter")

#se não quiser ir para root delete ou comente o código abaixo

pa.write ("sudo -s") # entrar no root

pa.press("enter")

time.sleep(0.5)

pa.write("senha") # sua senha novamente

pa.press("enter")