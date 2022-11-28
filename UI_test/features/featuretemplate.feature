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

Scenario: Eliminar un Business Partner
        Given Abro el modulo Business
        And presiono el boton business partner
        When busco el bussines partner por el codigo
        Then presiono el boton de eliminar un business partner      