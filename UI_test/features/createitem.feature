@createitem
Feature: CreateItem  
  
  Scenario: Crear un Producto y Servicio
    Given Abro el modulo business
    And presiono el boton items
    When presiono el boton de crear item
    And completo los datos del formulario de cliente <Tipo> <Nombre> <NombreCorto> <SKU> <PrecioVenta> <PrecioCosto> <PuntoPedido> <PrecioDescuento> <Capacidad> <Unidad>
    Then selecciono que el producto este Activo En venta Sujeto a impuesto y Favorito
    And completo la descripcion imagen grupo lista de precios atributo relacion y almacen y guardo

    Examples: Iteminfo
    |Tipo     |Nombre | NombreCorto | SKU    | PrecioVenta | PrecioCosto | PuntoPedido | PrecioDescuento | Capacidad | Unidad |
    |Product  |PRODUI | ItemUI      | 656516 | 5           | 5           | 5           | 4               | 200       | 1      |