from pytest_bdd import scenarios, given, when, then, parsers
from .objects import *
import time
from .login import *

# Scenarios 
scenarios('../features/createsurvey.feature')
    
@given('Abro el menu Panel de Consumo')
def abro_el_menu_oanel_consumo(sb, login_con_cookies_usuario_y_contrasena):
    
    sb.is_valid_url("https://test-xweb.eurokaizen.com/dashboard/security/index/MAP-001")
    sb.execute_script(CreateSurvey.ButtonMenuSurvey)
    sb.is_valid_url("https://test-xweb.eurokaizen.com/dashboard/HumanTalent/Index/MAP-015")
    time.sleep(1) 

@given('Presiono el boton Survey Administrador y el boton crear encuesta')
def presiono_el_boton_crear_survey_y_crear(sb):  
    sb.execute_script(CreateSurvey.ButtonMenuSurveyAdministrator)
    sb.is_valid_url("https://test-xweb.eurokaizen.com/HumanTalent/Survey/SurveyAdmin/")
    sb.execute_script(CreateSurvey.ButtonMenuCrearSurvey)
    sb.is_valid_url("https://test-xweb.eurokaizen.com/HumanTalent/Survey/CreateSurvey")
    time.sleep(1)

@when(parsers.parse('Selecciono el {Tipo} de encuesta y el {Estatus}'))
def selecciono_tipo_y_estatus(sb,Tipo,Estatus):
    sb.is_valid_url("https://test-xweb.eurokaizen.com/HumanTalent/Survey/CreateSurvey")
    time.sleep(5)
    sb.execute_script(CreateSurvey.SelectOpenType)
    if Tipo == '360-Survey' and Estatus == 'Open' :
        sb.execute_script(CreateSurvey.Select360Survey)
        sb.execute_script(CreateSurvey.SelectStatus)
        sb.execute_script(CreateSurvey.SelectOpenStatus)
    elif Tipo == 'Form-Survey' and Estatus == 'Open':
        sb.execute_script(CreateSurvey.SelectFormSurvey)
        sb.execute_script(CreateSurvey.SelectStatus)
        sb.execute_script(CreateSurvey.SelectOpenStatus)
    elif Tipo == 'Personal-Reference' and Estatus == 'Open':
        sb.execute_script(CreateSurvey.SelectReferenceSurvey)
        sb.execute_script(CreateSurvey.SelectStatus)
        sb.execute_script(CreateSurvey.SelectOpenStatus)    
        time.sleep(1)         
    

@when(parsers.parse('Agrego los datos de la encuesta {Titulo} {Descripcion}'))
def agrego_titulo_y_descripcion(sb,Titulo, Descripcion):
    sb.is_valid_url("https://test-xweb.eurokaizen.com/HumanTalent/Survey/CreateSurvey")
    sb.type("#Title", Titulo) 
    sb.type("#Description", Descripcion)
    time.sleep(5) 

@then('Agrego una pregunta')
def agrego_pregunta(sb):    
    sb.is_valid_url("https://test-xweb.eurokaizen.com/HumanTalent/Survey/CreateSurvey")
    sb.execute_script(CreateSurvey.ButtonAddQuestion)
    time.sleep(5) 
    sb.execute_script(CreateSurvey.SelectOpenQuestion)
    sb.execute_script(CreateSurvey.SelectQuestion)
    time.sleep(5) 

@then('Agrego una respuesta y guardo')
def agrego_respuesta_y_guardo(sb): 
    sb.is_valid_url("https://test-xweb.eurokaizen.com/HumanTalent/Survey/CreateSurvey")
    sb.execute_script(CreateSurvey.SelectOpenAnswer)
    time.sleep(1)
    sb.execute_script(CreateSurvey.SelectAnswer)
    sb.execute_script(CreateSurvey.ButtonSaveAnswer)
    sb.execute_script(CreateSurvey.ButtonSaveSurvey)
    time.sleep(5)
    sb.is_valid_url("https://test-xweb.eurokaizen.com/HumanTalent/Survey/SurveyAdmin/")
    time.sleep(3) 
