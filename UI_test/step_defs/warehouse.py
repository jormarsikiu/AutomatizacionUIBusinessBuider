from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.keys import Keys
from objects.paths import *
from objects.global_variables import Page
from objects.allure_screenshot import *
import random
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
Name = 'Pytest-'+str(random.randint(0,1000))+random.choice('abcdefghijklmnopqrstuvwxyz')
WarehouseCode = random.randint(0,1000)

# Scenarios
scenarios('../features/warehouse.feature')
feature = "features/warehouse.feature"

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
        imageFile = 'screenshot/Warehouse/Abro el modulo business.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: Abro el modulo business") 
        

@given('presiono el boton WareHouse')
def presiono_el_boton_warehouse(sb):  
    try: 
        sb.execute_script(CreateWareHouse.ButtonWarehouse)
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "Management/WareHouse" in getURL)
        time.sleep(3)
    except:
        imageFile = 'screenshot/Warehouse/presiono el boton WareHouse.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_only_fail(imageFile)
        raise Exception("Error: presiono el boton WareHouse")

@when('presiono el boton de crear un WareHouse')
def presiono_el_boton_crear_warehouse(sb):  
    try:
        sb.execute_script(CreateWareHouse.ButtonCreateWarehouse)
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "Management/Warehouse/Form" in getURL)
        time.sleep(3)
    except:
        imageFile = 'screenshot/Warehouse/presiono el boton de crear un WareHouse.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_only_fail(imageFile)
        raise Exception("Error: presiono el boton de crear un WareHouse")

@when(parsers.parse('completo los datos del formulario del Almacen {ShortName}'))
def completo_los_datos_de_formulario(sb,ShortName):
    try:
        sb.type("#WareHouseCode", WarehouseCode )
        sb.type("#WareHouseName", Name)
        sb.execute_script(CreateWareHouse.SelectClientTypeEntityOpen)
        sb.execute_script(CreateWareHouse.SelectClientTypeEntity)
        sb.type("#ShortName", ShortName)
        time.sleep(5)
    except:
        imageFile = 'screenshot/Warehouse/completo los datos del formulario del Almacen.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_only_fail(imageFile)
        raise Exception("Error: completo los datos del formulario del Almacen")

@then('anado la Direccion Grupos Condicion comercial Atributo de entidad')
def anado_direccion_contabilidad_grupo_direccioncomercial(sb):  
    try:    
        #Address
        sb.execute_script(CreateWareHouse.ButtonAddAddress)
        time.sleep(5)
        sb.execute_script(CreateWareHouse.ButtonOpenTypeAddress)
        time.sleep(5)
        sb.execute_script(CreateWareHouse.ButtonTypeAddress)
        time.sleep(5)
        sb.execute_script(CreateWareHouse.ButtonIsDelivery)
        sb.type("#pac-input", "Caracas")
        time.sleep(2)
        element = sb.wait_for_element_visible("#pac-input")
        time.sleep(2)
        element.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        element.send_keys(Keys.TAB)
        time.sleep(5)
        sb.execute_script(Global.Accept)
        time.sleep(5)
    except:
        imageFile = 'screenshot/Warehouse/anado la Direccion .png'
        sb.save_screenshot(imageFile)
        allure_screenshot_only_fail(imageFile)
        raise Exception("Error: anado la Direccion")
    
    try:
        #Groups
        sb.execute_script(CreateWareHouse.ButtonTapGroup)
        time.sleep(4)
        sb.execute_script(CreateWareHouse.ButtonAddBPGroup)
        time.sleep(4)
        sb.execute_script(CreateWareHouse.SelectOpenGroup)
        time.sleep(4)
        sb.execute_script(CreateWareHouse.SelectParentGroup)
        time.sleep(4)
        sb.execute_script(CreateWareHouse.SelectOpenChildGroup)
        time.sleep(4)
        sb.execute_script(CreateWareHouse.SelectChildGroup)
        time.sleep(4)
        sb.execute_script(Global.Accept)
        time.sleep(4)
    except:
        imageFile = 'screenshot/Warehouse/anado Grupos .png'
        sb.save_screenshot(imageFile)
        allure_screenshot_only_fail(imageFile)
        raise Exception("Error:  anado Grupos")

    try:
        #Business Condition
        sb.execute_script(CreateWareHouse.ButtonBussCond)
        time.sleep(2)
        sb.execute_script(CreateWareHouse.SelectOpenBussCond)
        time.sleep(4)
        sb.execute_script(CreateWareHouse.SelectBussCond)
        time.sleep(2)
    except:
        imageFile = 'screenshot/Warehouse/Business Condition.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_only_fail(imageFile)
        raise Exception("Error:  Business Condition")

    try:
        #Attributes
        sb.execute_script(CreateWareHouse.ButtonAttributes)
        time.sleep(2)
        sb.execute_script(CreateWareHouse.SelectOpenAttributes)
        time.sleep(4)
        sb.execute_script(CreateWareHouse.SelectAttributes)
        time.sleep(10)
    except:
        imageFile = 'screenshot/Warehouse/Attributes.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_only_fail(imageFile)
        raise Exception("Error:   Attributes")

#Save
@then('guardo formulario')
def guardo_formulario (sb):
    try:
        sb.execute_script(Global.SaveAll)
        time.sleep(8)
    except:
        imageFile = 'screenshot/Warehouse/guardo formulario.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_only_fail(imageFile)
        raise Exception("Error: guardo formulario")

@when('busco y presiono el boton de editar un Almacen')
def busco_el_partner_code_y_edito (sb): 
    try:
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "Management/WareHouse" in getURL)
        sb.execute_script(Global.Search)
        time.sleep(2)
        sb.execute_script(Global.FieldOpen)
        time.sleep(2)
        sb.execute_script(Global.FieldCode)
        time.sleep(2)
        sb.execute_script(Global.FieldOpenCondition)
        time.sleep(2)
        sb.execute_script(Global.FieldCondition)
        time.sleep(2)
        sb.type('[name*="Value"]', Name )
        time.sleep(2)
        sb.execute_script(Global.AcceptSearch)
        time.sleep(5)
        sb.click('#btnSearchPanel')
        time.sleep(5)
        sb.execute_script(CreateWareHouse.EditWarehouse)
        time.sleep(8)
    except:
        imageFile = 'screenshot/Warehouse/busco y presiono el boton de editar un business partner.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_only_fail(imageFile)
        raise Exception("Error: busco y presiono el boton de editar un business partner")


@when(parsers.parse('cambio los datos del formulario del Almacen {ShortName}'))
def cambio_los_datos_de_formulario(sb,ShortName):
    try:
        sb.type("#ShortName", ShortName)
        time.sleep(5)
    except:
        imageFile = 'screenshot/Warehouse/cambio los datos del formulario del Almacen.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_only_fail(imageFile)
        raise Exception("Error: cambio los datos del formulario del Almacen")

@when('busco y presiono el boton de Eliminar un Almacen')
def busco_el_partner_code_y_edito (sb): 
    try:
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "Management/WareHouse" in getURL)
        sb.execute_script(Global.Search)
        time.sleep(2)
        sb.execute_script(Global.FieldOpen)
        time.sleep(2)
        sb.execute_script(Global.FieldCode)
        time.sleep(2)
        sb.execute_script(Global.FieldOpenCondition)
        time.sleep(2)
        sb.execute_script(Global.FieldCondition)
        time.sleep(2)
        sb.type('[name*="Value"]', Name )
        time.sleep(2)
        sb.execute_script(Global.AcceptSearch)
        time.sleep(5)
        sb.click('#btnSearchPanel')
        time.sleep(5)
        sb.execute_script(CreateWareHouse.DeleteWarehouse)
        time.sleep(4)
        sb.execute_script(CreateWareHouse.ModalDeleteWarehouse)
        time.sleep(8)
        allure_screenshot_success(feature)
    except:
        imageFile = 'screenshot/Warehouse/busco y presiono el boton de Eliminar un Almacen.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_only_fail(imageFile)
        raise Exception("Error: busco y presiono el boton de Eliminar un Almacen") 