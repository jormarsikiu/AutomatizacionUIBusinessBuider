@survey
Feature: Survey
  
  Scenario Outline: Crear una Encuesta
    Given Abro el menu Panel de Consumo
    And Presiono el boton Survey Administrador y el boton crear encuesta
    When Selecciono el <Tipo> de encuesta y el <Estatus> 
    And Agrego los datos de la encuesta <Titulo> <Descripcion>
    Then Agrego una pregunta
    And Agrego una respuesta y guardo

    Examples: surveyinfo
    |Titulo                              |Descripcion                               | Tipo               | Estatus |
    |Test-Encuesta-para-pruebas-UI-Ref   |Esta-es-una-prueba-de-interfaz-de-usuario | Personal-Reference | Open    |
    |Test-Encuesta-para-pruebas-UI-360   |Esta-es-una-prueba-de-interfaz-de-usuario | 360-Survey         | Open    |
    |Test-Encuesta-para-pruebas-UI-Form  |Esta-es-una-prueba-de-interfaz-de-usuario | Form-Survey        | Open    |
