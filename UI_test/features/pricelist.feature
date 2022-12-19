@pricelist
Feature: PriceList

  Scenario Outline: Crear una lista de precios
    And presiono el boton Impuesto
    When presiono el boton de crear un Impuesto
    And completo los datos del primer formulario <Name> <ShortName> <LowerLimit> <UpperLimit>
    Then añado el valor del impuesto
    Then guardo formulario


