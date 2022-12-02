@warehouse
Feature: Warehouse
  
  Scenario Outline: Crear un Almacen
    Given Abro el modulo business
    And presiono el boton WareHouse
    When presiono el boton de crear un WareHouse
    And completo los datos del formulario del Almacen <ShortName>
    Then anado la Direccion Grupos Condicion comercial Atributo de entidad
    Then guardo formulario

    Examples: warehouseinfo
    |ShortName|
    |PyT      |
    
  Scenario Outline: Editar un Almacen
    Given Abro el modulo business
    And presiono el boton WareHouse
    When busco y presiono el boton de editar un Almacen
    And cambio los datos del formulario del Almacen <ShortName>
    Then guardo formulario

    Examples: warehouseinfo
    |ShortName  |
    |PyT-edit   |

  Scenario Outline: Eliminar un Almacen
    Given Abro el modulo business
    And presiono el boton WareHouse
    When busco y presiono el boton de Eliminar un Almacen