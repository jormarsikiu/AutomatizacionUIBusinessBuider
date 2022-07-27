from pytest_bdd import scenarios, given, when, then, parsers
from .objects import *
import time
from .login import *
import random

# Scenarios 
scenarios('../features/creategroup.feature')
GroupCode = str(random.randint(0,100000))

@given('Abro el modulo business')
def abro_el_modulo_de_security(sb, login_con_cookies_usuario_y_contrasena):
    sb.is_valid_url("https://test-xweb.eurokaizen.com/dashboard/security/index/MAP-001")
    sb.execute_script(Global.ButtonBusiness)
    time.sleep(1)

@given('presiono el boton Entity Group')
def presiono_el_boton_entity_group(sb):  
    sb.execute_script(CreateGroup.ButtonEntityGroup)
    sb.is_valid_url("https://test-xweb.eurokaizen.com/settings/entitygroup")
    time.sleep(3)

@when('presiono el boton Crear Grupo de entidades')
def presiono_el_boton_crear_grupo_entidades(sb):  
    sb.execute_script(CreateGroup.ButtonCreateEntityGroup)
    
    time.sleep(3)

@when(parsers.parse('agrego Codigo Nombre NombreCorto TipoEntidad CodigoPadre'))
def completo_los_datos_de_formulario(sb):
    sb.is_valid_url("https://test-xweb.eurokaizen.com/Management/BusinessPartner/Form")
    sb.type("#EntityGroupCode", GroupCode)
    sb.type("#EntityGroupName", "Grupo-UI"+GroupCode)
    sb.type("#ShortName", "Grupo-UI"+GroupCode)
    sb.execute_script(CreateGroup.SelectOpenEntityType)
    sb.execute_script(CreateGroup.SelectEntityType)
    sb.execute_script(CreateGroup.SelectOpenFatherCode)
    sb.execute_script(CreateGroup.SelectFatherCode)
    time.sleep(5)
    
@then('selecciono cargo una imagen')
def agrego_la_imagen(sb):  
    sb.execute_script(Global.AcceptModal)
    time.sleep(8)
    
    
@then('guardo el grupo')
def edito_y_guardo(sb): 
    string1 = '''document.querySelectorAll("[href*='''
    string2 = "'/Settings"+"/EntityGroup/EditGroupFormAsync?entityCode="+GroupCode+"'"
    string3 = ''']")[0].click()'''
    string4 = string1+string2+string3
    sb.execute_script(string4)
    sb.type("#EntityGroupName", "Grupo-UI"+GroupCode+"T")
    sb.type("#ShortName", "Grupo-UI2"+GroupCode+"T")
    sb.execute_script(Global.AcceptModal)
    time.sleep(8)