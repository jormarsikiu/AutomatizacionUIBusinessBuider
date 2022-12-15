from pytest_bdd import scenarios, given, when, then, parsers
from objects.paths import *
from objects.allure_screenshot import *
from objects.global_variables import Page
import time
from .login import *
import os
import shutil

#Carpeta para fotos
dir = 'screenshot/Survey'
if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)

PAGE = Page

# Scenarios 
scenarios('../features/survey.feature')
feature = "features/survey.feature"
    
@given('Abro el menu Panel de Consumo')
def abro_el_menu_oanel_consumo(sb, login_con_cookies_usuario_y_contrasena):
    try:
        sb.get(PAGE)
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "dashboard/security/index/" in getURL)
        sb.execute_script(CreateSurvey.ButtonMenuSurvey)
        time.sleep(5)
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "dashboard/HumanTalent/Index/MAP-015" in getURL)
        time.sleep(5) 
    except:
        imageFile = 'screenshot/Survey/Abro el menu Panel de Consumo.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error : Abro el menu Panel de Consumo")

@given('Presiono el boton Survey Administrador y el boton crear encuesta')
def presiono_el_boton_crear_survey_y_crear(sb):
    try:
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "HumanTalent/Survey/SurveyAdmin" in getURL)
        time.sleep(3) 
        sb.execute_script(CreateSurvey.ButtonMenuCrearSurvey)
        time.sleep(5) 
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "HumanTalent/Survey/CreateSurvey" in getURL)
        time.sleep(3) 
    except:
        imageFile = 'screenshot/BusinessPartner/Presiono el boton Survey Administrador y el boton crear encuesta.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error : Presiono el boton Survey Administrador y el boton crear encuesta")

@when(parsers.parse('Selecciono el {Tipo} de encuesta y el {Estatus}'))
def selecciono_tipo_y_estatus(sb,Tipo,Estatus):
    try:
        sb.execute_script(CreateSurvey.SelectOpenType)
        time.sleep(8)
        if Tipo == '360-Survey' and Estatus == 'Open' :
            sb.execute_script(CreateSurvey.Select360Survey)
            sb.execute_script(CreateSurvey.SelectStatus)
            sb.execute_script(CreateSurvey.SelectOpenStatus)
            time.sleep(5) 
        elif Tipo == 'Form-Survey' and Estatus == 'Open':
            sb.execute_script(CreateSurvey.SelectFormSurvey)
            sb.execute_script(CreateSurvey.SelectStatus)
            sb.execute_script(CreateSurvey.SelectOpenStatus)
            time.sleep(5) 
        elif Tipo == 'Personal-Reference' and Estatus == 'Open': 
            sb.execute_script(CreateSurvey.SelectReferenceSurvey)
            sb.execute_script(CreateSurvey.SelectStatus)
            sb.execute_script(CreateSurvey.SelectOpenStatus)    
            time.sleep(5) 
    except:
        imageFile = 'screenshot/Survey/Selecciono el Tipo de encuesta y el Estatus.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error : Selecciono el Tipo de encuesta y el Estatus")

@when(parsers.parse('Agrego los datos de la encuesta {Titulo} {Descripcion}'))
def agrego_titulo_y_descripcion(sb,Titulo, Descripcion):
    try:        
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "HumanTalent/Survey/CreateSurvey" in getURL)
        time.sleep(5)
        sb.type("#Title", Titulo)
        time.sleep(3)
        sb.type("#Description", Descripcion)
        time.sleep(3)
    except:
        imageFile = 'screenshot/Survey/Agrego los datos de la encuesta Titulo Descripcion.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error : Agrego los datos de la encuesta Titulo Descripcion")

@then('Agrego una pregunta')
def agrego_pregunta(sb):
    try:
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "HumanTalent/Survey/CreateSurvey" in getURL)
        time.sleep(3)
        sb.execute_script(CreateSurvey.ButtonAddQuestion)
        time.sleep(5) 
        sb.execute_script(CreateSurvey.SelectOpenQuestion)
        time.sleep(3)
        sb.execute_script(CreateSurvey.SelectQuestion)
        time.sleep(5) 
    except:
        imageFile = 'screenshot/Survey/Agrego una pregunta.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error : Agrego una pregunta") 

@then('Agrego una respuesta y guardo')
def agrego_respuesta_y_guardo(sb):
    try:
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "HumanTalent/Survey/CreateSurvey" in getURL)
        time.sleep(3)        
        sb.execute_script(CreateSurvey.SelectOpenAnswer)
        time.sleep(1)
        sb.execute_script(CreateSurvey.SelectAnswer)
        time.sleep(3)
        sb.execute_script(CreateSurvey.ButtonSaveAnswer)
        time.sleep(3)
        sb.execute_script(CreateSurvey.ButtonSaveSurvey)
        time.sleep(5)
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "HumanTalent/Survey/SurveyAdmin" in getURL)
        time.sleep(3)
        allure_screenshot_success(feature)
    except:
        imageFile = 'screenshot/Survey/Agrego una respuesta y guardo.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error : Agrego una respuesta y guardo")