from pytest_bdd import scenarios, given, when, then, parsers
from objects.paths import *
from objects.global_variables import Page
import time
from .login import *
import os
import shutil

#Carpeta para fotos
dir = 'screenshot/Warehouse'
if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)

PAGE = Page

# Scenarios
scenarios('../features/warehouse.feature')

@pytest.fixture
@given('Abro el modulo business')
def abro_el_modulo_de_business(sb, login_con_cookies_usuario_y_contrasena):
    try:
        sb.get(PAGE)
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "dashboard/security/index" in getURL)
        sb.execute_script(Global.ButtonBusiness)
        time.sleep(4)
    except:
        sb.save_screenshot('screenshot/Warehouse/Abro el modulo business.png')
        raise Exception("Error: Abro el modulo business")

@given('presiono el boton WareHouse')
def presiono_el_boton_warehouse(sb):  
    try: 
        sb.execute_script(CreateWareHouse.ButtonWarehouse)
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "Management/WareHouse" in getURL)
        time.sleep(3)
    except:
        sb.save_screenshot('screenshot/Warehouse/presiono el boton WareHouse.png')
        raise Exception("Error: presiono el boton WareHouse")

@when('presiono el boton de crear un WareHouse')
def presiono_el_boton_crear_warehouse(sb):  
    try:
        sb.execute_script(CreateWareHouse.ButtonCreateWarehouse)
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "Management/Warehouse/Form" in getURL)
        time.sleep(3)
    except:
        sb.save_screenshot('screenshot/Warehouse/presiono el boton de crear un WareHouse.png')
        raise Exception("Error: presiono el boton de crear un WareHouse")

@when(parsers.parse('completo los datos del formulario del Almacen {Code} {Name} {ShortName}'))
def completo_los_datos_de_formulario(sb,Code,Name,ShortName):
    try:
        sb.type("#WareHouseCode", Code)
        sb.type("#WareHouseName", Name)
        sb.execute_script(CreateWareHouse.SelectClientTypeEntityOpen)
        sb.execute_script(CreateWareHouse.SelectClientTypeEntity)
        sb.type("#ShortName", ShortName)
        time.sleep(5)
    except:
        sb.save_screenshot('screenshot/Warehouse/completo los datos del formulario del Almacen.png')
        raise Exception("Error: completo los datos del formulario del Almacen")

@then('añado la Direccion Contabilidad Grupo Condicion comercial')
def anado_direccion_contabilidad_grupo_direccioncomercial(sb):  
    try:    
        #Address
        sb.execute_script()
        time.sleep(5)
        #Address
        sb.execute_script()
        time.sleep(5)
    except:
        sb.save_screenshot('screenshot/Warehouse/añado la Direccion Contabilidad Grupo Condicion comercial.png')
        raise Exception("Error: añado la Direccion Contabilidad Grupo Condicion comercial")