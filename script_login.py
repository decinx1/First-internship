#Este script permite interactuar con el teclado para poner el usuario y la contraseña en sap 
#Este codigo es una prueba el cual interactua con el blog de notas 
#Funcion del codigo: abirir un blog de notas y lo maximise en dado caso de no estar abierto, de lo controrio solo lo maximisara,
#Agregara el usuario, interactuara con la tecla tab y agregara la contraseña, dara enter fin del script 



import pyautogui #Documentacion de librerias(biblotecas) utilizadas ---> https://pyautogui.readthedocs.io/en/latest/keyboard.html#the-press-keydown-and-keyup-functions
import time  #Documentacion de librerias(biblotecas) utilizadas ---> https://docs.python.org/3/library/time.html
import os #Documentacion de librerias(biblotecas) utilizadas --->  https://www.w3schools.com/python/module_os.asp


"""def app_abierta():
    windows = pyautogui.getWindowsWithTitle("Excel")
    return len(windows) > 0
"""


def blog_notas(): #Funcion  para abrir  el blog de notas
    os.system("start excel")
    time.sleep(5) #Timepo designado para realizar operacion 
    pyautogui.press('enter')#Preciona enter contrasea
    time.sleep(0.5)


def max_window(): #Funcion para abrir  la ventana
    pyautogui.hotkey('alt','space') #Preciona Alt + Espacio
    time.sleep(0.5)
    pyautogui.press('x') #Selecciona Maximisar 
    time.sleep(0.5)



def user_password(usuario, contraseña): #Funcion que designa usuario y contraseña 
    pyautogui.write(usuario)#Escribir el usuario 
    time.sleep(1) 
    pyautogui.press('enter')#Preciona enter 
    time.sleep(0.5)
    pyautogui.press('tab')#Precionar Tab
    time.sleep(2)
    pyautogui.write(contraseña)#Escribe la contraseña
    time.sleep(0.5)
    pyautogui.press('enter')#Preciona enter 
    time.sleep(2)
    #Tiempo designado 0.5 segundos para todas las operacciones 


# Script principal

blog_notas()



""" if not app_abierta():
    blog_notas()


elif blog_notas():
    app_abierta
"""


# Agrega usuario y contraseña
usuario = "usuario"
contraseña = "contraseña"
user_password(usuario, contraseña)

# Maximiza la ventana del Bloc de notas
max_window()
