@createwarehouse
Feature: CreateWarehouse
  
  Scenario: Crear un Almacen
    Given Abro el modulo business
    And presiono el boton WareHouse
    When presiono el boton de crear un WareHouse
    And completo los datos del formulario del Almacen <Code> <Name> <ShortName>
    Then añado el Impuesto Atributos Equipos Contacto Imagen

    Examples: businesspartnerinfo
    |Code         |Name   |ShortName|
    |UITestP1th0n |Pytest |PyT      |