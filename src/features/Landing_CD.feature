# Created by Lenno at 15/07/2020
Feature: Funciones de Landing Claro drive
  # Enter feature description here

  @Landing
  Scenario: Abrir el Navegador
    Given Open the application Claro drive
    When I charge the Json of the App: landing.json
    Then I click Inicio sesion
    And I click in partner Telcel
    Then I click in partner Claro musica
    Then I click in partner Claro video
    Then I click in Correo
    Then I click in partner Telmex
    And I click Iniciar Sesion
    Then I click Olvidaste tu contraseña
    When The window will open click ENVIAR
    Then I click Volver a inicio
    Then I click Inicio sesion
    Then I click Cancelar
    When I click Registrarme
    Then I click in partner Telcel
    Then I click in partner Claro musica
    Then I click in partner Claro video
    Then I click in partner Telmex
    Then I click in Correo
    And I click in Terminos y condiciones
    Then I click in Politicas privacidad
    Then I click button Registrame
    Then In click in button Cancelar

    Then I click Descubre
    Then I click Comparte
    Then I click Respalda

    When I click Descarga
    Then I click Google play
    Then I click App Store
    #Then I click Claro drive
    When I click Opciones

    Then I click option Telmex
    When I click Opciones
    Then I click option Telcel
    When I click Opciones
    Then I click option Claro musica
    When I click Opciones
    Then I click option Claro video
    When I click Opciones
    Then I click option Correo

    When I click Planes
    Then I click plan TDC
    Then I click plan Telmex
    Then I click plan Telcel

    When I click Negocio
    Then I click negocio Caracteristicas
    Then I click negocio Descarga
    Then I click negocio Planes
    Then I click Claro dirve personal

    Then I click Link footer Centro de ayuda
    Then I click Link footer Forma de pago Telmex
    Then I click Link footer Forma de pago Telcel
    Then I click Link footer Forma de pago TDC
    Then I click Link footer Acerca de
    Then I click Link footer Terminos y Condicones
    Then I click Link footer Politicas de privacidad

    Then I click Footer Google play
    Then I click Footer App Store
    Then I click Footer Desktop Mac Windows
    Then I click Link footer Correo electronico











