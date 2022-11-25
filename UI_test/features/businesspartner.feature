@businesspartner
Feature: BusinessPartner  
  
  Scenario Outline: Crear un Business Partner
    Given Abro el modulo business
    And presiono el boton business partner
    When presiono el boton de crear un business partner
    And completo los datos del formulario de cliente <Name> <ShortName> <ComercialActivity> <TaxCode>
    Then añado la Direccion Contabilidad Grupo Condicion comercial
    And añado el Impuesto Atributos Equipos Contacto Imagen
    Then guardo formulario

    Examples: businesspartnerinfo
    |Name   | ShortName  | ComercialActivity | TaxCode |
    |UITest | Pytest     | Test              | T3ts    |

  
  Scenario Outline: Editar un Business Partner
    Given Abro el modulo business
    And presiono el boton business partner
    When busco y presiono el boton de editar un business partner
    And cambio los datos del formulario de cliente <Name> <ShortName> <ComercialActivity> <TaxCode>
    Then guardo formulario

     Examples: businesspartnerinfo
    |Name        | ShortName       | ComercialActivity      | TaxCode      |
    |UITest-edit | Pytest-edit     | Test-edit              | T3ts-edit    |
