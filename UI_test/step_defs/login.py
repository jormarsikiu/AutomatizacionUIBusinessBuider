from objects.paths import *
from objects.global_variables import Page, User, Pass
import pytest
import time
import os
import shutil
from objects.allure_screenshot import *

#Carpeta para fotos
dir = 'screenshot/login'
if os.path.exists(dir):
    shutil.rmtree(dir)

PAGE = Page

@pytest.fixture
def login_con_cookies_usuario_y_contrasena(sb):
    try:    
        #Abre la pagina
        sb.get(PAGE)
        
        #Acepta cookies
        sb.execute_script(Login.ButtonCookie)
        time.sleep(1)
        
        #Ingresa los datos
        sb.type("#UserName", User)
        sb.type("#Password", Pass)
        
        #Acepta el boton
        sb.execute_script(Login.ButtonLogin)
        time.sleep(8) 
        
        #Cambia el idioma
        sb.execute_script(Login.ButtonFlag)
        sb.execute_script(Login.ButtonSpanishFlag)

    except:
        imageFile = 'screenshot/login/login con cookies usuario y contrasena.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_only_fail(imageFile)
        raise Exception("Error: login con cookies usuario y contrasena") 