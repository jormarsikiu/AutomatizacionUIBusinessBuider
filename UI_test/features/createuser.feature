@createuser
Feature: CreateUser  
  
  Scenario: Crear un usuario
    Given Abro el menu User
    When Presiono el boton crear usuario
    Then Agrego los datos <FirstName> <LastName> <Avatar> <Email> <Password> <ConfirmPassword> <PhoneNumber> y guardo

    Examples: userinfo
    |FirstName  |LastName | Avatar     | Email                | Password  | ConfirmPassword | PhoneNumber|
    |Marta      |Perez    | martaperez | martaperez@gmail.com | Pa$$w0rd  | Pa$$w0rd        | 589875234  |
