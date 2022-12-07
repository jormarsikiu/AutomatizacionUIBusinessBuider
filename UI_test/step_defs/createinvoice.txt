from pytest_bdd import scenarios, given, when, then, parsers
from objects.paths import *
from objects.global_variables import Page
import time
from .login import *

PAGE = Page

# Scenarios 
scenarios('../features/createinvoice.feature')
InvoiceCode = ""

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

@when('presiono el boton Factura y luego el boton Crear')
def presiono_el_boton_crear_factura(sb):
    sb.execute_script(CreateInvoice.TapInvoice)
    time.sleep(2)
    sb.execute_script(CreateInvoice.ButtonCreate)
    sb.is_valid_url("https://test-xweb.eurokaizen.com/Documents/Transactions/CreateDraftFormAsync")
    time.sleep(5)

@when('selecciono FechaCreacion FechaVencimiento Cliente Proveedor')
def selecciono_fechas_cliente_proveedor(sb):
    #InvoiceCode = sb.execute_script(CreateInvoice.GetInvoiceCode)
    
    #Client
    sb.execute_script(CreateInvoice.SelectOpenClient)
    time.sleep(2)
    sb.execute_script(CreateInvoice.SelectClient)
    time.sleep(2)
    sb.execute_script(CreateInvoice.SelectOpenClientAddress)
    time.sleep(2)
    sb.execute_script(CreateInvoice.SelectClientAddress)
    time.sleep(2)
    
    #Provider
    sb.execute_script(CreateInvoice.SelectOpenProvider)
    time.sleep(2)
    sb.execute_script(CreateInvoice.SelectProvider)
    time.sleep(2)
    sb.execute_script(CreateInvoice.SelectOpenProviderAddress)
    time.sleep(2)
    sb.execute_script(CreateInvoice.SelectProviderAddress)
    time.sleep(2)
    sb.click("#InvoiceDate")
    sb.execute_script(Global.SelectOKDate2)
    time.sleep(3)
    sb.click("#InvoiceDateDue")
    sb.execute_script(Global.SelectOKDate3)
    time.sleep(2)

@then('selecciono los productos')
def selecciono_productos(sb):  
    sb.execute_script(CreateInvoice.AddItem)
    time.sleep(2)
    
@then('guardo y busco la factura en el index')
def guardo_busco_en_el_index(sb):  
    sb.execute_script(CreateInvoice.SaveInvoice)
    time.sleep(10)
    
    #Busqueda
    sb.is_valid_url("https://test-xweb.eurokaizen.com/documents/transactions")
    sb.execute_script(CreateInvoice.TapInvoice)
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
    sb.type('[name*="Value"]', InvoiceCode)
    time.sleep(2)
    sb.click("#btnSearchPanel")
    time.sleep(2)
    sb.execute_script(CreateInvoice.EditInvoice)
    time.sleep(8)
 