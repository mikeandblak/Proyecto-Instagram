__author__ = 'Mk&Bk'
import urllib2
from ftplib import FTP
from socket import gaierror
from ftplib import error_temp

MSJ_INI_CONEXION = 'Conectando al servidor...'
MSJ_CONEXION_CORRECTA = '|==============Conexion correcta=============|'
MSJ_ERROR_CONEXION = 'No se pudo conectar con el servidor. :('
MSJ_SUIENDO_FILE = 'Subiendo el archivo'
MSJ_UPLOAD_CORRECT = 'Imagen enviada al servidor correctamente.'
MSJ_ERROR_UPLOAD_FILE = 'Error al subir la imagen al servidor'
STOR = 'STOR '

def abrir_conexion_ftp():
    datos_servidor = {'servidor': 'Ip de tu servidor',
                      'usuario': 'usuario de tu servidor',
                      'password': 'contraseña del usuario'}
    print('\t\t{0}\n\n'.format(MSJ_INI_CONEXION))
    try:
        conexion = FTP(datos_servidor['servidor'])  # Conecta con el servidor
        conexion.login(datos_servidor['usuario'], datos_servidor['password'])  # Recibe el usuario y pass del servidor
        print(MSJ_CONEXION_CORRECTA + '\n')
        return conexion
    except gaierror:
        print(MSJ_ERROR_CONEXION)
        return None
    except error_temp, e:
        print('Error en login: {0}'.format(str(e.message)))

def descargar_y_enviar_a_servidor(con, url, i, nombre, extencion='.jpg'):
    nombre_imagen = generar_nombre_imagen(nombre, i, extencion)
    print('{0}: {1}'.format(MSJ_SUIENDO_FILE, nombre_imagen))
    descargar_imagen(nombre_imagen, url)
    mandar_imagen_a_servidor(con, url, nombre_imagen)
    print('{0}\n'.format(MSJ_UPLOAD_CORRECT))


def mandar_imagen_a_servidor(conexion, url, nombre):
    """

    :type nombre: str
    """
    stor_nombre = "{0}{1}".format(STOR, nombre)
    datos_imagen = obtener_imagen_url(url)
    if datos_imagen is not None:
        try:
            conexion.storbinary(stor_nombre, datos_imagen)
        except gaierror:
            print('{0}'.format(MSJ_ERROR_UPLOAD_FILE))
        except Exception, e:
            print('Error desconocido: {0}'.format(str(e.message)))
    else:
        print('No se subio la imagen {0}'.format(nombre))


def obtener_imagen_url(url):
    try:
        datos_imagen = urllib2.urlopen(url)
        return datos_imagen
    except urllib2.HTTPError, e:
        print('Error HTTP al obtener la imagen: {0}'.format(str(e.reason)))
    except urllib2.URLError, e:
        print('Error URL al obtner la imagen: {0}'.format(str(e.reason)))
    except Exception, e:
        print('Error desconocido: {0}'.format(str(e.message)))
    return None


def descargar_imagen(nombre_descarga, url):
    datos_imagen = obtener_imagen_url(url)
    try:
        archivo_salida = open(nombre_descarga, 'wb')
        archivo_salida.write(datos_imagen.read())
        archivo_salida.close()
    except Exception, e:
        print('Error en archivos: {0}'.format(str(e.message)))


def generar_nombre_imagen(nombre, posicion, extencion):
    """

    :type extencion: str
    """
    nombre_posicion = '{0}_{1}'.format(nombre, str(posicion))
    nombre_imagen = '{0}{1}'.format(nombre_posicion, extencion)
    return nombre_imagen




def cambiar_directorio_servidor(conexion, nombre_del_directorio):
    try:
        conexion.cwd(nombre_del_directorio)  # Entra en el directorio del servidor
        print('Ahora estas en el directorio: {0}'.format(nombre_del_directorio))
    except Exception, e:
        print("Error al cambiar de directorio: {0}".format(str(e.message)))


def cerrar_conexion_servidor(conexion):
    try:
        conexion.quit()  # Cierra la conexion con el servidor
        print('Conexion finalizada corectamente!!')
    except Exception, e:
        print("Error al cerrar la conexion: {0}".format(str(e.message)))


def mostrar_directorio_actual_servidor(conexion):
    try:
        print conexion.pwd()  # Muestra la ruta del servidor
    except Exception, e:
        print('Error al mostrar el directorio actual: {0}'.format(str(e.message)))


def mostrar_contenido_servidor(conexion):
    try:
        print('\n\t\t**************Contenido del servidor******************')
        print conexion.retrlines('LIST')
    except Exception, e:
        print('Error al mostrar los archivos del directorio actual: {0}'.format(str(e.message)))


def remover_directorio(conexion, nombre_directorio):
    """

    :type conexion: FTP
    """
    try:
        conexion.rmd(nombre_directorio)
        print('Carpeta {0} eliminada con exito.'.format(nombre_directorio))
    except Exception, e:
        print('Error al remover directorio: {0}'.format(str(e.message)))


def guardar_imagenes_servidor(conexion, lista_urls, nombre):
    contador = 1
    for url in lista_urls:
        descargar_y_enviar_a_servidor(conexion, url, contador, nombre)
        contador += 1