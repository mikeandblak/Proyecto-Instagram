__author__ = 'Mk&Bk'
from instagram import InstagramAPI
import Busquedas
import ConexionFTP

MSJ_NUM_IMG = 'Cuantas imagenes quieres descargar: '
MSJ_NUM_MAX_TAGS = 'Numero maximo de tags a buscar: '
MSJ_NUM_MAX_UBICACIONES = 'Numero maximo de ubicaciones a buscar: '
MSJ_NUM_MAX_IMG_UBICACION = 'Numero de imagenes por cada Ubicacion: '
MSJ_NAME_IMG = 'Nombre principal de las imagenes: '
RESOLUTION_THUMBNAIL = 'thumbnail'
RESOLUTION_STANDAR = 'standard_resolution'
RESOLUTION_LOW = 'low_resolution'


DIRECTORIO_IMG = 'Aqui va el nombre de la carpeta donde guardara las imagenes en tu servidor'

def main():
    access_token = 'Aqui va tu llave de Instagram'
    conexion = ConexionFTP.abrir_conexion_ftp()
    if conexion is not None:
        api = InstagramAPI(access_token=access_token)
        ConexionFTP.cambiar_directorio_servidor(conexion, DIRECTORIO_IMG)
        lista_media = menu(api)
        urls = Busquedas.obtener_urls_de_lista_media(lista_media, pedir_resolucion_imagenes())
        ConexionFTP.guardar_imagenes_servidor(conexion, urls, pedir_nombre_imagenes())
        ConexionFTP.cerrar_conexion_servidor(conexion)

def pedir_entero(mensaje):
    """

    :param mensaje: str
    :rtype : int
    """
    while True:
        numero = raw_input(mensaje)
        if es_entero(numero):
            return numero


def pedir_nombre_imagenes():
    while True:
        nombre = raw_input(MSJ_NAME_IMG)
        if nombre is not '':
            return nombre
        else:
            print('Por favor introduce un nombre.')


def pedir_resolucion_imagenes():
    """

    :rtype : str
    """
    respuesta = raw_input("Con que calidad quieres bajar las imagenes?\n\t1)Baja \n\t2)Media \n\t3)Normal\n Calidad: ")
    if respuesta == '1':
        calidad = RESOLUTION_THUMBNAIL

    elif respuesta == '2':
        calidad = RESOLUTION_LOW

    elif respuesta == '3':
        calidad = RESOLUTION_STANDAR

    else:
        print("Opcion invalida, se dejo la calidad por defecto")
        calidad = RESOLUTION_THUMBNAIL
    return calidad


def es_entero(numero):
    """

    :param numero: int
    :rtype : bool
    """
    try:
        numero = int(numero)
        if numero > 0:
            return True
        else:
            print('No puede ser negativo.')
            return False
    except ValueError:
        print('No es un numero entero.')
        print('Introduce un numero valido.')
        return False


def menu(api):
    while True:
        print('Como quieres buscar las imagenes:')
        print('1. Por tag')
        print('2. Por ubicaciones (latitud, longitud)')
        print('3. Popular Media')
        opcion = raw_input("\nEscribe una opcion: ")

        if opcion is '1':
            numero_imagenes = pedir_entero(MSJ_NUM_IMG)
            tag = raw_input("Que tag quieres buscar: ")
            lista_imagenes = Busquedas.obtener_media_por_tag(api, tag, numero_imagenes)
            if len(lista_imagenes) is not 0:
                return lista_imagenes
            print("No hay imagenes con ese tag")
        
        elif opcion is '2':
            numero_ubicaciones = pedir_entero(MSJ_NUM_MAX_UBICACIONES)
            numero_imagenes = pedir_entero(MSJ_NUM_MAX_IMG_UBICACION)
            lista_imagenes = Busquedas.obtener_imagenes_varias_ubicaciones(api, numero_imagenes, numero_ubicaciones)
            if len(lista_imagenes) is not 0:
                 return lista_imagenes

        elif opcion is '3':
            numero_imagenes = pedir_entero(MSJ_NUM_IMG)
            lista_imagenes = Busquedas.obtener_media_popular(api, numero_imagenes)
            if len(lista_imagenes) is not 0:
                return lista_imagenes


        else:
            print('Opcion no valida. Escoge de nuevo.')



main()