from pytest_bdd import scenarios, given, when, then, parsers
from objects.paths import *
from objects.global_variables import Page
import time
from .login import *

PAGE = Page

# Scenarios 
scenarios('../features/createdraft.feature')
DraftCode = ""

@given('Abro el módulo de Sales')
def abro_el_modulo_de_sales(sb, login_con_cookies_usuario_y_contrasena):
    sb.is_valid_url("https://test-xweb.eurokaizen.com/dashboard/security/index/MAP-001")
    sb.execute_script(Global.ButtonSales)
    sb.is_valid_url("https://test-xweb.eurokaizen.com/dashboard/sales/SalesPanel/SAL-002")
    time.sleep(3)

@given('presiono el boton Transactions')
def presiono_el_boton_transactions(sb):  
    sb.execute_script(Global.ButtonTransactions)
    sb.is_valid_url("https://test-xweb.eurokaizen.com/documents/transactions")
    time.sleep(3)

@when('presiono el boton Crear')
def presiono_el_boton_crear_draft(sb):  
    sb.execute_script(CreateDraft.ButtonCreate)
    sb.is_valid_url("https://test-xweb.eurokaizen.com/Documents/Transactions/CreateDraftFormAsync")
    time.sleep(5)

@when('selecciono FechaCreacion FechaVencimiento Cliente Proveedor')
def selecciono_fechas_cliente_proveedor(sb):
    DraftCode = sb.execute_script(CreateDraft.GetDraftCode)
    sb.click("#DraftDate")
    time.sleep(2)
    sb.execute_script(Global.SelectOKDate)
    time.sleep(2)
    sb.click("#DraftDateDue")
    time.sleep(2)
    sb.execute_script(Global.SelectOKDate2)
    time.sleep(2)
    sb.execute_script(CreateDraft.SelectOpenClientName)
    sb.execute_script(CreateDraft.SelectOpenClientAddress)
    time.sleep(2)
    sb.execute_script(CreateDraft.SelectOpenProviderName)
    sb.execute_script(CreateDraft.SelectOpenProviderAddress)
    time.sleep(2)

@then('selecciono los productos')
def selecciono_productos(sb):  
    sb.execute_script(CreateDraft.ButtonAddItem)
    time.sleep(2)
    
@then('guardo y busco el borrador en el index')
def guardo_busco_en_el_index(sb):  
    sb.execute_script(CreateDraft.SaveAll)
    time.sleep(10)
    
    #Busqueda
    sb.is_valid_url("https://test-xweb.eurokaizen.com/documents/transactions")
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
    sb.type('[name*="Value"]', DraftCode)
    time.sleep(2)
    sb.click("#btnSearchPanel")
    time.sleep(2)
    sb.execute_script(CreateDraft.EditDraft)
    time.sleep(8)
 