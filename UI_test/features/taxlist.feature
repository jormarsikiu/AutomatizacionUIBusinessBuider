@taxlist
Feature: taxlist
  
  Scenario Outline: Crear un Impuesto
    Given Abro el modulo business
    And presiono el boton Impuesto
    When presiono el boton de crear un Impuesto
    And completo los datos del primer formulario <Name> <ShortName> <LowerLimit> <UpperLimit>
    Then añado el valor del impuesto
    Then guardo formulario

    Examples: taxlistinfo
    |Name   | ShortName  | LowerLimit | UpperLimit  | 
    |UITest | Pytest     | 1          | 12          |


  Scenario Outline: Editar un Impuesto
    Given Abro el modulo business
    And presiono el boton Impuesto
    When busco y presiono el boton de editar Impuesto
    And cambio los datos del primer formulario <Name> <ShortName>
    Then añado otro el valor del impuesto
    Then guardo formulario

    Examples: taxlistinfo
    |Name        | ShortName    |
    |UITest-edit | Pytest-edit  | 

  Scenario Outline: Eliminar un Impuesto
    Given Abro el modulo business
    And presiono el boton Impuesto
    When busco y presiono el boton de Eliminar Impuesto