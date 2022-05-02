@createorder
Feature: CreateOrder
  
  Scenario: Crear un Pedido
    Given Abro el módulo de Sales
    And presiono el boton Transactions 
    When presiono el boton Pedido y luego el boton Crear
    And selecciono FechaCreacion FechaVencimiento Cliente Proveedor
    Then selecciono los productos
    And guardo y busco el pedido en el index