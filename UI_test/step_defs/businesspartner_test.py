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
dir = 'screenshot/BusinessPartner'
if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)

PAGE = Page

# Scenarios 
scenarios('../features/businesspartner.feature')
feature = "features/businesspartner.feature"
PartnerCode = random.randint(0,1000)

@pytest.fixture
@given('Abro el modulo business')
def abro_el_modulo_de_security(sb, login_con_cookies_usuario_y_contrasena):
    try:
        sb.get(PAGE)
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "dashboard/security/index/" in getURL)
        sb.execute_script(Global.ButtonBusiness)
        time.sleep(1)
    except:
        imageFile = 'screenshot/BusinessPartner/Abro el modulo business.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Abro el modulo business")

    
#checar el flujo actual de business partner
@given('presiono el boton business partner')
def presiono_el_boton_business_partenr(sb):  
    try:    
        sb.execute_script(Global.ButtonBusiness)
        sb.execute_script(CreateBusinessPartner.ButtonBusinessPartner)
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "Management/BusinessPartner" in getURL)
        time.sleep(4)
    except:
        imageFile = 'screenshot/BusinessPartner/presiono el boton business partner.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: presiono el boton business partner")    
    


@when('presiono el boton de crear un business partner')
def presiono_el_boton_crear_business_partenr(sb):  
    try:
        sb.execute_script(CreateBusinessPartner.ButtonBusinessPartnerCreate)
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "Management/BusinessPartner/Form" in getURL)
        time.sleep(3)
    except:
        imageFile = 'screenshot/BusinessPartner/presiono el boton de crear un business partner.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: presiono el boton de crear un business partner")


@when(parsers.parse('completo los datos del formulario de cliente {Name} {ShortName} {ComercialActivity} {TaxCode}'))
@when(parsers.parse('cambio los datos del formulario de cliente {Name} {ShortName} {ComercialActivity} {TaxCode}'))
def completo_los_datos_de_formulario(sb,Name, ShortName,ComercialActivity, TaxCode):
    try:
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "Management/BusinessPartner/" in getURL)
        sb.execute_script(CreateBusinessPartner.SelectClientTypeOpen)
        sb.execute_script(CreateBusinessPartner.SelectClientType)
        sb.type("#PartnerCode", PartnerCode)
        sb.type("#PartnerName", Name)
        sb.type("#ShortName", ShortName)
        sb.type("#ComercialActivity", ComercialActivity)
        sb.type("#TaxCode", TaxCode)
        time.sleep(5)
    except:
        imageFile = 'screenshot/BusinessPartner/completo los datos del formulario de cliente.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: completo los datos del formulario de cliente")
    
    
@then('añado la Direccion Contabilidad Grupo Condicion comercial')
def anado_direccion_contabilidad_grupo_direccioncomercial(sb):  
    try:
        #Address
        sb.execute_script(CreateBusinessPartner.ButtonAddAddress)
        time.sleep(5)
        sb.execute_script(CreateBusinessPartner.ButtonOpenTypeAddress)
        time.sleep(5)
        sb.execute_script(CreateBusinessPartner.ButtonTypeAddress)
        time.sleep(5)
        sb.execute_script(CreateBusinessPartner.ButtonIsDelivery)
        time.sleep(5)
        sb.type("#pac-input", "Caracas")
        time.sleep(5)
        element = sb.wait_for_element_visible("#pac-input")
        time.sleep(5)
        element.send_keys(Keys.ARROW_DOWN)
        time.sleep(5)
        element.send_keys(Keys.TAB)
        time.sleep(5)
        sb.execute_script(Global.Accept)
        time.sleep(5)
    except:
        imageFile = 'screenshot/BusinessPartner/añado la Direccion Contabilidad Grupo Condicion comercial.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: añado la Direccion Contabilidad Grupo Condicion comercial")
    
    try:    
        #Accounting
        sb.execute_script(CreateBusinessPartner.ButtonAccounting)
        time.sleep(2)
        sb.execute_script(CreateBusinessPartner.ButtonAddAccounting)
        time.sleep(2)
        sb.execute_script(CreateBusinessPartner.SelectOpenAccounting)
        time.sleep(4)
        sb.execute_script(CreateBusinessPartner.SelectParentAccounting)
        time.sleep(2)
        sb.execute_script(CreateBusinessPartner.SelectOpenChildAccounting)
        time.sleep(2)
        sb.execute_script(CreateBusinessPartner.SelectChildAccounting)
        time.sleep(2)
        sb.execute_script(Global.Accept)
        time.sleep(2)
    except:
        imageFile = 'screenshot/BusinessPartner/Accounting.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: Accounting")

    try:
        #Groups
        sb.execute_script(CreateBusinessPartner.ButtonTapGroup)
        time.sleep(2)
        sb.execute_script(CreateBusinessPartner.ButtonAddBPGroup)
        time.sleep(2)
        sb.execute_script(CreateItem.SelectOpenGroup)
        time.sleep(4)
        sb.execute_script(CreateItem.SelectParentGroup)
        time.sleep(2)
        sb.execute_script(CreateItem.SelectOpenChildGroup)
        time.sleep(2)
        sb.execute_script(CreateItem.SelectChildGroup)
        time.sleep(2)
        sb.execute_script(Global.Accept)
        time.sleep(2)
    except:
        imageFile = 'screenshot/BusinessPartner/Groups.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: Groups")

    try:
        #Business Condition
        sb.execute_script(CreateBusinessPartner.ButtonBussCond)
        time.sleep(2)
        sb.execute_script(CreateBusinessPartner.SelectOpenBussCond)
        time.sleep(4)
        sb.execute_script(CreateBusinessPartner.SelectBussCond)
        time.sleep(2)
    except:
        imageFile = 'screenshot/BusinessPartner/Business Condition.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: Business Condition")
    
    
@then('añado el Impuesto Atributos Equipos Contacto Imagen')
def anado_impuesto_atributos_equipos_contacto_imagen(sb): 
    try:
        #Tax
        sb.execute_script(CreateBusinessPartner.ButtonTax)
        time.sleep(2)
        sb.execute_script(CreateBusinessPartner.SelectOpenTax)
        time.sleep(7)
        sb.execute_script(CreateBusinessPartner.SelectTax)
        time.sleep(2)
    except:
        imageFile = 'screenshot/BusinessPartner/añado el Impuesto Atributos Equipos Contacto Imagen.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: añado el Impuesto Atributos Equipos Contacto Imagen")    

    try:
        #Attributes
        sb.execute_script(CreateBusinessPartner.ButtonAttributes)
        time.sleep(2)
        sb.execute_script(CreateBusinessPartner.SelectOpenAttributes)
        time.sleep(4)
        sb.execute_script(CreateBusinessPartner.SelectAttributes)
        time.sleep(2)
    except:
        imageFile = 'screenshot/BusinessPartner/Attributes.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: Attributes")  

    try:      
        #Equipments
        sb.execute_script(CreateBusinessPartner.ButtonEquip)
        time.sleep(2)
        sb.execute_script(CreateBusinessPartner.ButtonAddEquip)
        time.sleep(2)
        sb.execute_script(CreateBusinessPartner.SelectOpenEquip)
        time.sleep(4)
        sb.execute_script(CreateBusinessPartner.SelectEquip)
        time.sleep(2)
        sb.execute_script(CreateBusinessPartner.InputEquip)
        time.sleep(2)
        sb.execute_script(Global.Accept)
        time.sleep(2)
    except:
        imageFile = 'screenshot/BusinessPartner/Equipments.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: Equipments")  
    
    try:
        #Contact 
        sb.execute_script(CreateBusinessPartner.ButtonContact)
        time.sleep(2)
        sb.execute_script(CreateBusinessPartner.ButtonAddContact)
        time.sleep(2)
        sb.execute_script(CreateBusinessPartner.SelectOpenContact)
        time.sleep(4)
        sb.execute_script(CreateBusinessPartner.SelectContact)
        time.sleep(2)
        sb.execute_script(CreateBusinessPartner.InputContact)
        time.sleep(2)
        sb.execute_script(Global.Accept)
        time.sleep(2)
    except:
        imageFile = 'screenshot/BusinessPartner/Contact.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: Contact")  

    try:
        #Image
        sb.execute_script(CreateBusinessPartner.ButtonIamage)
        time.sleep(2)
        '''
        sb.execute_script(CreateBusinessPartner.ButtonAddImage)
        time.sleep(2)
        dir_name = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(dir_name, "example_logs/%s" % "screenshot.png")
        sb.choose_file('button[class*="dz-button"]', file_path)
        time.sleep(6)
        sb.click("#buttonConfirm")
        '''
    except:
        imageFile = 'screenshot/BusinessPartner/Image.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: Image")      
    
#Save
@then('guardo formulario')
def guardo_formulario (sb):
    try:
        sb.execute_script(Global.SaveAll)
        time.sleep(10)
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "Management/BusinessPartner" in getURL)
    except:
        imageFile = 'screenshot/BusinessPartner/guardo formulario.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: guardo formulario")  
        
      
@when('busco y presiono el boton de editar un business partner')
def busco_el_partner_code_y_edito (sb): 
    try:
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "Management/BusinessPartner" in getURL)
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
        sb.type('[name*="Value"]', PartnerCode )
        time.sleep(2)
        sb.execute_script(Global.AcceptSearch)
        time.sleep(5)
        sb.click('#btnSearchPanel')
        time.sleep(5)
        sb.execute_script(CreateBusinessPartner.EditIBP)
        time.sleep(8)
    except:
        imageFile = 'screenshot/BusinessPartner/busco y presiono el boton de editar un business partner.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: busco y presiono el boton de editar un business partner")

   
@when('busco y presiono el boton de Eliminar un business partner')
def busco_el_partner_code_y_elimino (sb): 
    try:
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "Management/BusinessPartner" in getURL)
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
        sb.type('[name*="Value"]', PartnerCode )
        time.sleep(2)
        sb.execute_script(Global.AcceptSearch)
        time.sleep(5)
        sb.click('#btnSearchPanel')
        time.sleep(5)
        sb.execute_script(CreateBusinessPartner.DeleteBP)
        time.sleep(8)
        sb.execute_script(CreateBusinessPartner.ModalDeleteBP)
        time.sleep(10)
        allure_screenshot_success(feature)
    except:
        imageFile = 'screenshot/BusinessPartner/busco y presiono el boton de eliminar un business partner.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: busco y presiono el boton de eliminar un business partner")
