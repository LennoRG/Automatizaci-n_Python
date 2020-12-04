import os



class Inicializar():
    #DIRECTORIO BASE
    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    DateFormat = '%d/%m/%Y'
    HourFormat = "%H%M%S"

    #JSON Data
    Json = basedir + u'\jsons'

    Environment = 'Test'

    #BROWSER DE PRUEBAS
    NAVEGADOR = u'Chrome'

    #DIRECTORIO DE EVIDENCIAS
    Path_Envidencias = basedir + u'\data\capturas'

    #Hoja de datos EXCEL
    Excel = basedir + u'\data\Data.xlsx'

    if Environment == 'Test':
        URL = 'https://test-portal.clarodrive.com/'

    if Environment == 'PROD':
        URL = 'https://www.clarodrive.com/'


