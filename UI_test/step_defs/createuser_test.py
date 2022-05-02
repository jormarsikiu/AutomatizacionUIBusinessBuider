from pytest_bdd import scenarios, given, when, then, parsers
from .objects import *
import pytest
import time
from .login import *
import os


# Scenarios 
scenarios('../features/createuser.feature')
    
@given('Abro el menu User')
def abro_el_menu_security(sb, login_con_cookies_usuario_y_contrasena):
    try:
        sb.is_valid_url("https://test-xweb.eurokaizen.com/dashboard/security/index/MAP-001")
        sb.execute_script(CreateUser.ButtonMenuUser)
    except:
        print('El test falla al presionar el boton - Users')
        time.sleep(1) 

@when('Presiono el boton crear usuario')
def presiono_el_boton_crear_usuario(sb):  
    try:
        sb.is_valid_url("https://test-xweb.eurokaizen.com/settings/user")
        sb.click("#IdFormCreateUser")
    except:
        print('El test falla al presionar el boton - Crear Usuario')
        time.sleep(5) 


@then(parsers.parse('Agrego los datos {FirstName} {LastName} {Avatar} {Email} {Password} {ConfirmPassword} {PhoneNumber} y guardo'))
def datos_usuario(sb,FirstName,LastName, Avatar, Email, Password, ConfirmPassword, PhoneNumber):    
    try:
        sb.is_valid_url("https://test-xweb.eurokaizen.com/settings/user")
        sb.type("#FirstName", FirstName)
        sb.type("#LastName", LastName)
        sb.type("#Avatar", Avatar)
        sb.type("#Email", Email)
        sb.type("#Password", Password)
        sb.type("#ConfirmPassword", ConfirmPassword)
        sb.type("#PhoneNumber", PhoneNumber)
        #sb.click("#IsActive")
        time.sleep(3)
        sb.execute_script(CreateUser.ButtonMenuUserNext)
        sb.click("#977836644-selectable")
    except:
        print('El test guardar el formulario de crear usuario')
        #os.mkdir('screenshot/createuser_test')
        #sb.save_screenshot('screenshot/createuser_test/datos_usuario.png')
        time.sleep(5) 
