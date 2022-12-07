@createinvoice
Feature: CreateInvoice
  
  Scenario: Crear una Factura
    Given Abro el módulo de Sales
    And presiono el boton Transactions 
    When presiono el boton Factura y luego el boton Crear
    And selecciono FechaCreacion FechaVencimiento Cliente Proveedor
    Then selecciono los productos
    And guardo y busco la factura en el index