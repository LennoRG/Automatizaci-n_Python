# Created by Lenno at 03/09/2020
Feature: Registro de usuario en Correo
  # Enter feature description here

  @RegisterUserCorreo
  Scenario: Registro de Usuario
    Given Open the Applicationn
    When I charge the Json of the App: registerCorreo.json
    Then I click on the button Registrate
    And I click on Correo
    Then I enter the Registro data
    And I click the button Registrarme

    When You select the TDC plan
    Then I click on the 200GB plan
    And I click the button Aceptar

    When I am in the payment information enter Nombre of the TDC Titular
    Then Enter the TDC number
    Then Income the Mes of the TDC
    Then Enter the Anio of the TDC
    Then Enter the CVV of the TDC
    And I click button Aceptar

    When I am on the success screen, I click on the IR A MI CLARO DRIVE button
    Then Opens the Popup Bienvenida and I click on Google Play
    Then I click on App Store
    Then I click on Claro drove Desktop
    Then I click on Terminos and Politicas de Privacidad
    Then I click on 200GB
    Then I click on 300GB
    Then I click on 1024GB
    And I click button Cerrar Popup Bienvenida

    When The Wizard opens I click the Comenzar button
    Then I click on the Siguiente button on CREAR
    Then I click on the Siguiente button on Menu
    Then I click on the Siguiente button on Favoritos
    And I click on the Finalizar button on Galeria
    When I click button Wizard
    Then The Wizard opens I click the Comenzar button
    And I click button Cerrar Wizard
    When I click button Wizard
    And I click button Saltar Wizard











