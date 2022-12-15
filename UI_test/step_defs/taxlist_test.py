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
dir = 'screenshot/Taxlist'
if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)

PAGE = Page

# Scenarios 
scenarios('../features/taxlist.feature')
feature = "features/taxlist.feature"
TaxCode = str(random.randint(0,100000))

@pytest.fixture
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
        imageFile = 'screenshot/Taxlist/Abro el modulo business.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error : Abro el modulo business")


@given('presiono el boton Impuesto')
def presiono_el_boton_taxlist(sb):  
    try:    
        sb.execute_script(CreateTaxlist.ButtonTaxlist)
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "Management/Tax" in getURL)
        time.sleep(4)
    except:
        imageFile = 'screenshot/Taxlist/presiono el boton Impuesto.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: presiono el boton Impuesto")    

@when('presiono el boton de crear un Impuesto')
def presiono_el_boton_crear_taxlist(sb):  
    try:    
        sb.execute_script(CreateTaxlist.ButtonCreateTaxlist)
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "Management/Tax" in getURL)
        time.sleep(3)
    except:
        imageFile = 'screenshot/Taxlist/presiono el boton de crear un Impuesto.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: presiono el boton de crear un Impuesto")  

@when(parsers.parse('completo los datos del primer formulario {Name} {ShortName} {LowerLimit} {UpperLimit}'))
def completo_los_datos_de_formulario(sb,Name, ShortName,LowerLimit, UpperLimit ):
    try:
        sb.type("#TaxName", Name)
        sb.type("#ShortName", ShortName)
        time.sleep(3)
        sb.type("#BaseEntityCode", TaxCode)
        time.sleep(3)
        sb.type("#LowerLimit", LowerLimit)
        time.sleep(3)
        sb.type("#UpperLimit", UpperLimit)
        time.sleep(3)
        sb.execute_script(CreateTaxlist.SelectClientTypeEntityOpen)
        time.sleep(3)
        sb.execute_script(CreateTaxlist.SelectClientTypeEntity)
        time.sleep(5)
        sb.execute_script(CreateTaxlist.SelectParentCodeOpen)
        time.sleep(5)
        sb.execute_script(CreateTaxlist.SelectParentCode)
        time.sleep(10)
    except:
        imageFile = 'screenshot/Taxlist/completo los datos del primer formulario.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: completo los datos del primer formulario")

@then('añado el valor del impuesto')
def anado_del_impuesto(sb):  
    try:
        #Address
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "Management/Tax" in getURL)
        time.sleep(5)
        sb.execute_script(CreateTaxlist.ButtonMenuNext)
        time.sleep(5)
        sb.type("#Val", "5")
        time.sleep(5)
        sb.execute_script(CreateTaxlist.AcceptValue)
        time.sleep(5)
    except:
        imageFile = 'screenshot/Taxlist/añado el valor del impuesto.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: añado el valor del impuesto")

#Save
@then('guardo formulario')
def guardo_formulario (sb):
    try:
        sb.execute_script(CreateTaxlist.ButtonFinishform)
        time.sleep(10)
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "Management/Tax" in getURL)
        allure_screenshot_success(feature)
    except:
        imageFile = 'screenshot/Taxlist/guardo formulario.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: guardo formulario")  

@when('busco y presiono el boton de editar Impuesto')
def busco_el_tax_code_y_edito (sb): 
    try:
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "Management/Tax" in getURL)
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
        sb.type('[name*="Value"]', TaxCode )
        time.sleep(2)
        sb.execute_script(Global.AcceptSearch)
        time.sleep(5)
        sb.click('#btnSearchPanel')
        time.sleep(5)
        sb.execute_script(CreateTaxlist.EditTax)
        time.sleep(8)
    except:
        imageFile = 'screenshot/Taxlist/busco y presiono el boton de editar Impuesto.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: busco y presiono el boton de editar Impuesto")

@when(parsers.parse('cambio los datos del primer formulario {Name} {ShortName}'))
def cambio_los_datos_de_formulario(sb,Name, ShortName):
    try:
        sb.type("#TaxName", Name)
        time.sleep(3)
        sb.type("#ShortName", ShortName)
        time.sleep(6)
    except:
        imageFile = 'screenshot/Taxlist/cambio los datos del primer formulario.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: cambio los datos del primer formulario")
        
@then('añado otro el valor del impuesto')
def anado_del_impuesto(sb):  
    try:
        #Address
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "Management/Tax" in getURL)
        time.sleep(5)
        sb.execute_script(CreateTaxlist.ButtonMenuNext)
        time.sleep(5)
        sb.type("#Val", "8")
        time.sleep(5)
        sb.execute_script(CreateTaxlist.AcceptValue)
        time.sleep(5)
    except:
        imageFile = 'screenshot/Taxlist/añado otro el valor del impuesto.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: añado otro el valor del impuesto")

@when('busco y presiono el boton de Eliminar Impuesto')
def busco_el_tax_code_y_edito (sb): 
    try:
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "Management/Tax" in getURL)
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
        sb.type('[name*="Value"]', TaxCode )
        time.sleep(2)
        sb.execute_script(Global.AcceptSearch)
        time.sleep(5)
        sb.click('#btnSearchPanel')
        time.sleep(5)
        sb.execute_script(CreateTaxlist.DeleteTax)
        time.sleep(5)
        sb.execute_script(CreateTaxlist.ModalDeleteTax)
        time.sleep(8)
        allure_screenshot_success(feature)
        time.sleep(3)
    except:
        imageFile = 'screenshot/Taxlist/busco y presiono el boton de eliminar Impuesto.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: busco y presiono el boton de eliminar Impuesto")