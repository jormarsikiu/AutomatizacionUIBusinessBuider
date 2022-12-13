from pytest_bdd import scenarios, given, when, then, parsers
from objects.paths import *
from objects.global_variables import Page
from objects.allure_screenshot import *
import time
from .login import *
import random
import os
import shutil

#Carpeta para fotos
dir = 'screenshot/Item'
if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)

PAGE = Page

# Scenarios 
scenarios('../features/item.feature')
feature = "features/item.feature"
ItemCode = random.randint(0,1000)

@given('Abro el modulo business')
def abro_el_modulo_de_security(sb, login_con_cookies_usuario_y_contrasena):
    try:
        sb.get(PAGE)
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "dashboard/security/index/MAP-001" in getURL)
        sb.execute_script(Global.ButtonBusiness)
        time.sleep(3)
    except:
        imageFile = 'screenshot/Item/Abro el modulo business.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: Abro modulo business") 

@given('presiono el boton items')
def presiono_el_boton_item(sb):  
    try:
        sb.execute_script(CreateItem.ButtonItem)
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "Management/Item" in getURL)
        time.sleep(8)
    except:
        imageFile = 'screenshot/Item/presiono el boton items.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: presiono el boton items")

@when('presiono el boton de crear item')
def presiono_el_boton_crear_business_partenr(sb):  
    try:
        sb.execute_script(CreateItem.ButtonItemCreate)
        time.sleep(6)
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "Management/Item/_ItemForm" in getURL)
        time.sleep(3)
    except:
        imageFile = 'screenshot/Item/presiono el boton de crear item.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: presiono el boton de crear item")

@when(parsers.parse('cambio los datos del formulario de cliente {Tipo} {Nombre} {NombreCorto} {SKU} {PrecioVenta} {PrecioCosto} {PuntoPedido} {PrecioDescuento} {Capacidad} {Unidad}'))
@when(parsers.parse('completo los datos del formulario de cliente {Tipo} {Nombre} {NombreCorto} {SKU} {PrecioVenta} {PrecioCosto} {PuntoPedido} {PrecioDescuento} {Capacidad} {Unidad}'))
def completar_los_datos_de_formulario(sb,Tipo,Nombre, NombreCorto,SKU, PrecioVenta, PrecioCosto, PuntoPedido, PrecioDescuento, Capacidad, Unidad):
            
    try:
        Tipo0 = str(Tipo)
        if (Tipo0 == "Product"):    
            sb.execute_script(CreateItem.SelectOpenType)
            sb.execute_script(CreateItem.SelectTypeProduct)
        elif(Tipo0 == "Service"):
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
        time.sleep(20)
    except:
        imageFile = 'screenshot/Item/completo los datos del formulario de cliente .png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: completo los datos del formulario de cliente ")

@then('selecciono que el producto este Activo En venta Sujeto a impuesto y Favorito')
def selecciono_activo_enventa_sujetoimpuesto_favorito(sb):  
    try:
        sb.execute_script(CreateItem.ButtonIsActive)
        time.sleep(4)
        sb.execute_script(CreateItem.ButtonIsActive)
        time.sleep(4)
        sb.execute_script(CreateItem.ButtonForSale)
        time.sleep(4)
        sb.execute_script(CreateItem.ButtonForSale)
        time.sleep(4)
        sb.execute_script(CreateItem.ButtonTaxable)
        time.sleep(4)
        sb.execute_script(CreateItem.ButtonTaxable)
        time.sleep(3)
        sb.execute_script(CreateItem.ButtonFeatured)
        time.sleep(4)
    except:
        imageFile = 'screenshot/Item/selecciono que el producto este Activo En venta Sujeto a impuesto y Favorito.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: selecciono que el producto este Activo En venta Sujeto a impuesto y Favorito")
    
@then('completo la descripcion imagen grupo lista de precios atributo relacion y almacen')
def selecciono_descripcions(sb):
    try:  
        sb.type("#Description", "Esta es una Description")
        time.sleep(5)
        sb.execute_script(CreateItem.ButtonImage)
        time.sleep(5)
        sb.execute_script(CreateItem.ButtonAddImage)
        time.sleep(4)
        #sb.find_element('#myDropzone').send_keys('C:/Users/Kaizen/Desktop/ui_businessBuilding/UITestPython/UI_test/step_defs/1.png')
    except:
        imageFile = 'screenshot/Item/Item Description.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error: Item Description")
    
    ##Groups
    try:
        sb.execute_script(CreateItem.ButtonGroup)
        time.sleep(4)
        sb.execute_script(CreateItem.ButtonAddGroups)
        time.sleep(4)
        sb.execute_script(CreateItem.SelectOpenGroup)
        time.sleep(4)
        sb.execute_script(CreateItem.SelectParentGroup)
        time.sleep(4)
        #sb.execute_script(CreateItem.SelectOpenChildGroup)
        #sb.execute_script(CreateItem.SelectChildGroup)
        sb.execute_script(Global.Accept)
        time.sleep(4)
    except:
        imageFile = 'screenshot/Item/Item Groups.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error:Item Groups")
    
    #PriceList
    try:
        sb.execute_script(CreateItem.ButtonPriceList)
        time.sleep(4)
        sb.execute_script(CreateItem.ButtonAddPriceList)
        time.sleep(4)
        sb.execute_script(CreateItem.SelectOpenPriceList)
        time.sleep(4)
        sb.execute_script(CreateItem.SelectPriceList)
        time.sleep(4)
        sb.execute_script(Global.Accept)
        time.sleep(4)
    except:
        imageFile = 'screenshot/Item/Item PriceList.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error:Item PriceList")

    #Atributes
    try:
        sb.execute_script(CreateItem.ButtonAtributes)
        time.sleep(4)
        sb.execute_script(CreateItem.SelectOpenAtributes)
        time.sleep(4)
        sb.execute_script(CreateItem.SelectAtributes)
        time.sleep(4)
    except:
        imageFile = 'screenshot/Item/Item Atributes.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error:Item Atributes")
    
    #Relations
    try:
        sb.execute_script(CreateItem.ButtonRelations)
        time.sleep(4)
        sb.execute_script(CreateItem.ButtonAddRelations)
        time.sleep(5)
        sb.execute_script(CreateItem.SelectOpenRelations)
        time.sleep(4)
        sb.execute_script(CreateItem.SelectRelations)
        time.sleep(4)
        sb.execute_script(CreateItem.SelectOpenItems)
        time.sleep(4)
        sb.execute_script(CreateItem.SelectItems)
        time.sleep(4)
        sb.execute_script(Global.Accept)
    except:
        imageFile = 'screenshot/Item/Item Relations.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error:Item Relations")
    
    #Warehouse
    try:
        sb.execute_script(CreateItem.ButtonWarehouse)
        time.sleep(4)
        sb.execute_script(CreateItem.SelectOpenWarehouse)
        time.sleep(4)
        sb.execute_script(CreateItem.SelectWarehouse)
        time.sleep(4)
    except:
        imageFile = 'screenshot/Item/Item Warehouse.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error:Item Warehouse")
    
    
#Save All
@then('guardo formulario')
def guardo_fomulario (sb):
    try:
        sb.execute_script(Global.SaveAll)
        time.sleep(10)
        allure_screenshot_success(feature)
    except:
        imageFile = 'screenshot/Item/Item Save All.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error:Item Save All") 
        
#Busqueda
@when('busco y presiono el boton de editar un Producto y Servicio')
def busco_y_presiono_editar_el_producto_y_servicio (sb):
    try:
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "Management/Item" in getURL)
        sb.execute_script(Global.Search)
        time.sleep(4)
        sb.execute_script(Global.FieldOpen)
        time.sleep(4)
        sb.execute_script(Global.FieldCode)
        time.sleep(4)
        sb.execute_script(Global.FieldOpenCondition)
        time.sleep(4)
        sb.execute_script(Global.FieldCondition)
        time.sleep(4)
        sb.type('[name*="Value"]', ItemCode )
        time.sleep(4)
        sb.execute_script(Global.AcceptSearch)
        time.sleep(4)
        sb.click("#btnSearchPanel")
        time.sleep(4)
        sb.execute_script(CreateItem.EditItem)
        time.sleep(8)
    except:
        imageFile = 'screenshot/Item/Item Busqueda.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error:Item Busqueda")

#Delete
@when('busco y presiono el boton de eliminar un Producto y Servicio')
def busco_y_presiono_eliminar_el_producto_y_servicio (sb):
    try:
        getURL = sb.get_current_url()
        sb.assert_true( PAGE + "Management/Item" in getURL)
        sb.execute_script(Global.Search)
        time.sleep(4)
        sb.execute_script(Global.FieldOpen)
        time.sleep(4)
        sb.execute_script(Global.FieldCode)
        time.sleep(4)
        sb.execute_script(Global.FieldOpenCondition)
        time.sleep(4)
        sb.execute_script(Global.FieldCondition)
        time.sleep(4)
        sb.type('[name*="Value"]', ItemCode )
        time.sleep(4)
        sb.execute_script(Global.AcceptSearch)
        time.sleep(4)
        sb.click("#btnSearchPanel")
        time.sleep(8)
        sb.execute_script(CreateItem.DeleteItem)
        time.sleep(8)
        sb.execute_script(CreateItem.ModalDeleteItem)
        time.sleep(10)
        allure_screenshot_success(feature)
    except:
        imageFile = 'screenshot/Item/Item busco y presiono el boton de eliminar un Producto y Servicio.png'
        sb.save_screenshot(imageFile)
        allure_screenshot_fail(imageFile, feature)
        raise Exception("Error:busco y presiono el boton de eliminar un Producto y Servicio")