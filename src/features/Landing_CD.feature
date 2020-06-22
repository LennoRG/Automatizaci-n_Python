# Created by Lenno at 15/06/2020
Feature: Funciones de Landing Claro drive
  # Enter feature description here

  Scenario: Abrir el Navegador
    Given Open the application
    And I charge the Json of the App: portal.json
    And I click on the button Iniciar Sesion
    And I click Correo
    And I click on the button Btn_Crear+
    And I click Carpeta
    Then I click Archivo de Texto
    Then I click Vista Cuadricula
    Then I click Vista Lista
    Then I click Mover a Papelera
    And I click Compartir
    And I click Favoritiar
    And I click Detalles
    And I click Renombrar
    And I click Mover Copiar
    And I click Descargar
    And I click Desfavoritiar
    And I click Check_Imagen
    Then I click Check_Carpeta
    And I click Mover Carpeta a Papelera
    Then I click Check_Header_list_view
    And I click Mover_Copiar
    Then I click Header_Descargar
    And I clic Menu_List_Imagenes
    Then I compare actions of BTNS filters






    