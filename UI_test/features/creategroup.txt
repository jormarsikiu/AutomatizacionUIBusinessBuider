@creategroup
Feature: CreateGroup
  
  Scenario: Crear un Grupo
    Given Abro el modulo business
    And presiono el boton Entity Group
    When presiono el boton Crear Grupo de entidades
    And agrego Codigo Nombre NombreCorto TipoEntidad CodigoPadre 
    Then selecciono cargo una imagen
    And guardo el grupo