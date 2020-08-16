# Created by Lenno at 15/06/2020
Feature: Funciones de Buzon Claro drive
  # Enter feature description here

  @Buzon
  Scenario: Abrir el Navegador
    Given Open the application
    When I charge the Json of the App: portal.json
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
   # Then I click Header_Descargar
    And I clic Menu_List_Imagenes
    Then I compare actions of BTNS filters
    And I click Reciente
    Then I click Favoritos
    Then I click Imagenes
    Then I click Videos
    Then I click Contactos
    Then I click Compartidos
    And I click Te compartieron
    And I click Compartiste
    And I click Ligas compartidas
    Then I click Etiquetas
    Then I click Papelera
    Then I click Todo los archivos

    When I click Seccion Actividad
    And I click Por usted
    Then I click Por otros
    Then I click Favoritos_Actividad
    Then I click Cambios al archivo
    Then I click Seguridad
    Then I click Archivos compartidos
    Then I click Comentarios
    Then I click Descargar la app
    Then I click Legales

    When I click Gallery
    And I click Orden_Gallery
    Then I click Todo_Gallery
    Then I click Albumes_Gallery
    Then I click Compartido_Gallery

    When I click Espacio_Familiar
    Then I click Informacion_Personal
    And  Clean text box and add Nombre Usuario
    Then I click button Seleccionar desde archivos
    And I choose a user photo
    Then I click button Seleccionar
    And I click button Seleccionar como foto de perfil
    Then I click button Eliminar foto de perfil
    And I click button Guardar Cambios
    Then I click Espacio_Fam_Seguridad
    And I write current password and new password Cambio Contraseña
    And  I click button Cambiar contraseña
    Then I click Espacio_Fam_Actividad
    And  Disable and enable chekbox in Actividad
    Then I click Informacion_Pago
    #Then I click Claro drive ajuste
    Then I click Configuraciones_Adicionales
    And Disable and enable chekbox in Configuraciones_Adicionales

    When I click Espacio_Familiar
    Then I click Añadir usuario
    And I add the user data in the Espacio Familiar
    Then I click Reenviar Invitacion
    Then I click Cancelar Invitacion


    When I click Avatar perfil
    Then I click Ajustes
    When I click Avatar perfil
    Then I click Ayuda
    When I click Avatar perfil
    Then I click Logout


















    