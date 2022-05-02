from pytest_bdd import scenarios, given, when, then, parsers
from .objects import *
import time
from .login import *
import random

# Scenarios 
scenarios('../features/createitem.feature')
file = "1.png"
ItemCode = random.randint(0,1000)

@given('Abro el modulo business')
def abro_el_modulo_de_security(sb, login_con_cookies_usuario_y_contrasena):
    sb.is_valid_url("https://test-xweb.eurokaizen.com/dashboard/security/index/MAP-001")
    sb.execute_script(Global.ButtonBusiness)
    time.sleep(3)

@given('presiono el boton items')
def presiono_el_boton_item(sb):  
    sb.execute_script(CreateItem.ButtonItem)
    sb.is_valid_url("https://test-xweb.eurokaizen.com/Management/Item")
    time.sleep(3)

@when('presiono el boton de crear item')
def presiono_el_boton_crear_business_partenr(sb):  
    sb.execute_script(CreateItem.ButtonItemCreate)
    sb.is_valid_url("https://test-xweb.eurokaizen.com/Management/Item/_ItemForm")
    time.sleep(3)


@when(parsers.parse('completo los datos del formulario de cliente {Tipo} {Nombre} {NombreCorto} {SKU} {PrecioVenta} {PrecioCosto} {PuntoPedido} {PrecioDescuento} {Capacidad} {Unidad}'))
def completar_los_datos_de_formulario(sb,Tipo,Nombre, NombreCorto,SKU, PrecioVenta, PrecioCosto, PuntoPedido, PrecioDescuento, Capacidad, Unidad):
    sb.is_valid_url("https://test-xweb.eurokaizen.com/Management/Item/_ItemForm")
    if (Tipo == "Product"):    
        sb.execute_script(CreateItem.SelectOpenType)
        sb.execute_script(CreateItem.SelectTypeProduct)
    elif(Tipo == "Service"):
        sb.execute_script(CreateItem.SelectOpenType)
        sb.execute_script(CreateItem.SelectTypeService)
    sb.type("#ItemCode", ItemCode)
    sb.type("#ItemName", Nombre)
    sb.type("#ShortName", NombreCorto)
    sb.type("#SKU", SKU)
    sb.click("#SaleDate")
    sb.execute_script(Global.SelectOKDate)
    sb.type("#SalesPrice", PrecioVenta)
    sb.type("#CostPrice", PrecioCosto)
    sb.type("#ReorderPoint", PuntoPedido)
    sb.type("#DiscountPrice", PrecioDescuento)
    sb.type("#Capacity", Capacidad)
    sb.type("#Unit", Unidad)
    time.sleep(2)

@then('selecciono que el producto este Activo En venta Sujeto a impuesto y Favorito')
def selecciono_activo_enventa_sujetoimpuesto_favorito(sb):  
    
    sb.execute_script(CreateItem.ButtonIsActive)
    time.sleep(2)
    sb.execute_script(CreateItem.ButtonIsActive)
    time.sleep(2)
    sb.execute_script(CreateItem.ButtonForSale)
    time.sleep(2)
    sb.execute_script(CreateItem.ButtonForSale)
    time.sleep(2)
    sb.execute_script(CreateItem.ButtonTaxable)
    time.sleep(2)
    sb.execute_script(CreateItem.ButtonTaxable)
    time.sleep(3)
    sb.execute_script(CreateItem.ButtonFeatured)
    time.sleep(2)
    
@then('completo la descripcion imagen grupo lista de precios atributo relacion y almacen y guardo')
def selecciono_descripcions(sb):  
    sb.type("#Description", "Esta es una Description")
    time.sleep(5)
    sb.execute_script(CreateItem.ButtonImage)
    time.sleep(5)
    sb.execute_script(CreateItem.ButtonAddImage)
    time.sleep(2)
    #sb.find_element('#myDropzone').send_keys('C:/Users/Kaizen/Desktop/ui_businessBuilding/UITestPython/UI_test/step_defs/1.png')
    
    ##Groups
    sb.execute_script(CreateItem.ButtonGroup)
    time.sleep(2)
    sb.execute_script(CreateItem.ButtonAddGroups)
    time.sleep(2)
    sb.execute_script(CreateItem.SelectOpenGroup)
    time.sleep(2)
    sb.execute_script(CreateItem.SelectParentGroup)
    time.sleep(2)
    #sb.execute_script(CreateItem.SelectOpenChildGroup)
    #sb.execute_script(CreateItem.SelectChildGroup)
    sb.execute_script(Global.Accept)
    time.sleep(2)
    
    #PriceList
    sb.execute_script(CreateItem.ButtonPriceList)
    time.sleep(2)
    sb.execute_script(CreateItem.ButtonAddPriceList)
    time.sleep(2)
    sb.execute_script(CreateItem.SelectOpenPriceList)
    time.sleep(2)
    sb.execute_script(CreateItem.SelectPriceList)
    time.sleep(2)
    sb.execute_script(Global.Accept)
    time.sleep(2)
    
    #Atributes
    sb.execute_script(CreateItem.ButtonAtributes)
    time.sleep(2)
    sb.execute_script(CreateItem.SelectOpenAtributes)
    time.sleep(2)
    sb.execute_script(CreateItem.SelectAtributes)
    time.sleep(2)
    
    #Relations
    sb.execute_script(CreateItem.ButtonRelations)
    time.sleep(2)
    sb.execute_script(CreateItem.ButtonAddRelations)
    time.sleep(5)
    sb.execute_script(CreateItem.SelectOpenRelations)
    time.sleep(2)
    sb.execute_script(CreateItem.SelectRelations)
    time.sleep(2)
    sb.execute_script(CreateItem.SelectOpenItems)
    time.sleep(2)
    sb.execute_script(CreateItem.SelectItems)
    time.sleep(2)
    sb.execute_script(Global.Accept)
    
    #Warehouse
    sb.execute_script(CreateItem.ButtonWarehouse)
    time.sleep(2)
    sb.execute_script(CreateItem.SelectOpenWarehouse)
    time.sleep(2)
    sb.execute_script(CreateItem.SelectWarehouse)
    time.sleep(2)
    
    #Save All
    sb.execute_script(Global.SaveAll)
    time.sleep(20)
    sb.is_valid_url("https://test-xweb.eurokaizen.com/Management/Item")
    time.sleep(5)
    
    #Busqueda
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
    sb.type('[name*="Value"]', ItemCode)
    time.sleep(2)
    sb.click("#btnSearchPanel")
    time.sleep(2)
    sb.execute_script(CreateItem.EditItem)
    time.sleep(8)