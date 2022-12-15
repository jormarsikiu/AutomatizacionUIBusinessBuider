@group
Feature: Group
  
  Scenario: Crear un Grupo
    Given Abro el modulo business
    And presiono el boton Entity Group
    When presiono el boton Crear Grupo de entidades
    And agrego Codigo Nombre NombreCorto TipoEntidad CodigoPadre, selecciono cargo una imagen
    Then guardo el grupo