@createbusiness
Feature: CreateBusinessPartner  
  
  Scenario: Crear un Business Partner
    Given Abro el modulo business
    And presiono el boton business partner
    When presiono el boton de crear business partner
    And completo los datos del formulario de cliente <Name> <ShortName> <ComercialActivity> <TaxCode>
    Then añado la Direccion Contabilidad Grupo Condicion comercial
    And añado el Impuesto Atributos Equipos Contacto Imagen

    Examples: businesspartnerinfo
    |Name   | ShortName  | ComercialActivity | TaxCode |
    |UITest | Pytest     | Test              | T3ts    |




