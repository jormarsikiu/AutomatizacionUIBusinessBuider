@createdraft
Feature: CreateDraft
  
  Scenario: Crear un Borrador
    Given Abro el módulo de Sales
    And presiono el boton Transactions 
    When presiono el boton Crear
    And selecciono FechaCreacion FechaVencimiento Cliente Proveedor
    Then selecciono los productos
    And guardo y busco el borrador en el index