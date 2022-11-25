@businesspartner
Feature: BusinessPartner  
  
  Scenario: Crear un Business Partner
    Given Abro el modulo business
    And presiono el boton business partner
    When presiono el boton de crear un business partner
    And completo los datos del formulario de cliente <Name> <ShortName> <ComercialActivity> <TaxCode>
    Then añado la Direccion Contabilidad Grupo Condicion comercial
    And añado el Impuesto Atributos Equipos Contacto Imagen
    When busco el partner code 
    Then presiono el boton de editar
    And cambio el campo <Name>

    Examples: businesspartnerinfo
    |Name        | ShortName  | ComercialActivity | TaxCode |
    |UITest      | Pytest     | Test              | T3ts    |
