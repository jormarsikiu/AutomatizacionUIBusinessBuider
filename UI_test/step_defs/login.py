from objects.paths import *
from objects.global_variables import Page
import pytest
import time

PAGE = Page

@pytest.fixture
def login_con_cookies_usuario_y_contrasena(sb):
    
    #Abre la pagina
    sb.get(PAGE)
    
    #Acepta cookies
    sb.execute_script(Login.ButtonCookie)
    time.sleep(1)
    
    #Ingresa los datos
    sb.type("#UserName", "QA@corpalcione.com")
    sb.type("#Password", "Pa$$w0rd")
    
    #Acepta el boton
    sb.execute_script(Login.ButtonLogin)
    time.sleep(8) 
    
    #Cambia el idioma
    sb.execute_script(Login.ButtonFlag)
    sb.execute_script(Login.ButtonSpanishFlag)
   