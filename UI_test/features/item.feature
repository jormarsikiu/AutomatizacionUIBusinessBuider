@item
Feature: Item  
  
  Scenario Outline: Crear un Producto y Servicio
    Given Abro el modulo business
    And presiono el boton items
    When presiono el boton de crear item
    And completo los datos del formulario de cliente <Tipo> <Nombre> <NombreCorto> <SKU> <PrecioVenta> <PrecioCosto> <PuntoPedido> <PrecioDescuento> <Capacidad> <Unidad>
    Then selecciono que el producto este Activo En venta Sujeto a impuesto y Favorito
    And completo la descripcion imagen grupo lista de precios atributo relacion y almacen
    Then guardo formulario

    Examples: Iteminfo
    |Tipo     |Nombre | NombreCorto | SKU    | PrecioVenta | PrecioCosto | PuntoPedido | PrecioDescuento | Capacidad | Unidad |
    |Product  |PRODUI | ItemUI      | 656516 | 5           | 5           | 5           | 4               | 200       | 1      |


  Scenario Outline: Editar un Producto y Servicio
    Given Abro el modulo business
    And presiono el boton items
    When busco y presiono el boton de editar un Producto y Servicio
    And cambio los datos del formulario de cliente <Tipo> <Nombre> <NombreCorto> <SKU> <PrecioVenta> <PrecioCosto> <PuntoPedido> <PrecioDescuento> <Capacidad> <Unidad>
    Then guardo formulario

    Examples: Iteminfo
    |Tipo     |Nombre      | NombreCorto    | SKU    | PrecioVenta | PrecioCosto | PuntoPedido | PrecioDescuento | Capacidad | Unidad |
    |Product  |PRODUI-edit | ItemUI-edit    | 545412 | 4           | 3           | 5           | 2               | 300       | 2      |

  Scenario Outline: Eliminar un Producto y Servicio
    Given Abro el modulo business
    And presiono el boton items
    When busco y presiono el boton de eliminar un Producto y Servicio
