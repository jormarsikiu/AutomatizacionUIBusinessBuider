from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pytest_bdd import scenarios, given, when, then, parsers
from objects.paths import *
from objects.allure_screenshot import *
from objects.global_variables import Page
import time
from .login import *
import random
import os
import shutil

#Carpeta para fotos
dir = 'screenshot/Group'
if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)

PAGE = Page

# Scenarios 
scenarios('../features/group.feature')
feature = "features/group.feature"
GroupCode = str(random.randint(0,100000))

@given('Abro el modulo business')
def abro_el_modulo_de_security(sb, login_con_cookies_usuario_y_contrasena):
    try:
        sb.get(PAGE)
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "dashboard/security/index/MAP-001" in getURL)
        time.sleep(5)
        sb.execute_script(Global.ButtonBusiness)
        time.sleep(5)
    except:
        imageFile = 'screenshot/Group/Abro el modulo business.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error : Abro el modulo business")


@given('presiono el boton Entity Group')
def presiono_el_boton_entity_group(sb): 
    try: 
        sb.execute_script(CreateGroup.ButtonEntityGroup)
        time.sleep(5)
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "settings/entitygroup" in getURL)
        time.sleep(5)
    except:
        imageFile = 'screenshot/Group/presiono el boton Entity Group.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error : presiono el boton Entity Group")


@when('presiono el boton Crear Grupo de entidades')
def presiono_el_boton_crear_grupo_entidades(sb):
    try:
        sb.execute_script(CreateGroup.ButtonCreateEntityGroup)
        time.sleep(3)
    except:
        imageFile = 'screenshot/Group/presiono el boton Crear Grupo de entidades.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error : presiono el boton Crear Grupo de entidades")


@when(parsers.parse('agrego Codigo Nombre NombreCorto TipoEntidad CodigoPadre, selecciono cargo una imagen'))
def completo_los_datos_de_formulario(sb):
    try:
        sb.type("#EntityGroupCode", GroupCode)
        sb.type("#EntityGroupName", "Grupo-UI"+GroupCode)
        sb.type("#ShortName", "Grupo-UI"+GroupCode)
        sb.execute_script(CreateGroup.SelectOpenEntityType)
        sb.execute_script(CreateGroup.SelectEntityType)
        sb.execute_script(CreateGroup.SelectOpenFatherCode)
        sb.execute_script(CreateGroup.SelectFatherCode)
        time.sleep(5)
    except:
        imageFile = 'screenshot/Group/agrego Codigo Nombre NombreCorto TipoEntidad CodigoPadre, selecciono cargo una imagen.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error : agrego Codigo Nombre NombreCorto TipoEntidad CodigoPadre, selecciono cargo una imagen")


@then('guardo el grupo')
def guardo_el_grupo(sb):
    try:
        sb.execute_script(Global.AcceptModal)
        time.sleep(8)
    except:
        imageFile = 'screenshot/Group/guardo el grupo.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error : guardo el grupo")
