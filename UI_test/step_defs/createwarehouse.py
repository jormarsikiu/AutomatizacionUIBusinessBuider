from pytest_bdd import scenarios, given, when, then, parsers
from objects.paths import *
from objects.global_variables import Page
import time
from .login import *

PAGE = Page

# Scenarios
scenarios('../features/createwarehouse.feature')

@given('Abro el modulo business')
def abro_el_modulo_de_business(sb, login_con_cookies_usuario_y_contrasena):
    sb.is_valid_url("https://test-xweb.eurokaizen.com/dashboard/security/index/MAP-001")
    sb.execute_script(Global.ButtonBusiness)
    time.sleep(1)

@given('presiono el boton WareHouse')
def presiono_el_boton_warehouse(sb):  
    sb.execute_script(CreateWareHouse.ButtonWarehouse)
    sb.is_valid_url("https://test-xweb.eurokaizen.com/Management/WareHouse")
    time.sleep(3)

@when('presiono el boton de crear un WareHouse')
def presiono_el_boton_crear_warehouse(sb):  
    sb.execute_script(CreateWareHouse.ButtonCreateWarehouse)
    sb.is_valid_url("https://test-xweb.eurokaizen.com/Management/Warehouse/Form")
    time.sleep(3)

@when(parsers.parse('completo los datos del formulario del Almacen {Code} {Name} {ShortName}'))
def completo_los_datos_de_formulario(sb,Code,Name,ShortName):
    sb.is_valid_url("https://test-xweb.eurokaizen.com/Management/BusinessPartner/Form")
    sb.type("#WareHouseCode", Code)
    sb.type("#WareHouseName", Name)
    sb.execute_script(CreateWareHouse.SelectClientTypeEntityOpen)
    sb.execute_script(CreateWareHouse.SelectClientTypeEntity)
    sb.type("#ShortName", ShortName)
    time.sleep(5)

@then('añado la Direccion Contabilidad Grupo Condicion comercial')
def anado_direccion_contabilidad_grupo_direccioncomercial(sb):  
    
    #Address
    sb.execute_script()
    time.sleep(5)
    #Address
    sb.execute_script()
    time.sleep(5)