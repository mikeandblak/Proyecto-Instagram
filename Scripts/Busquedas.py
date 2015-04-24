__author__ = 'Mk&Bk'
from instagram import InstagramAPIError
from httplib2 import ServerNotFoundError


def obtener_id_usuario_por_nombre(api):
    nombre = raw_input("Nombre de usuario para buscar ID: ")
    recent_media = api.user_search(nombre, count=1)
    try:
        id_usuario = recent_media[0].id
        return id_usuario
    except IndexError, e:
        return "El usuario no existe: {0}".format(str(e.message))


def obtener_media_usuario_token(api):
    """

    :rtype : list
    :param api: InstagramAPI
    """
    try:
        lista_media = api.user_media_feed()  # Devuelvelve Tupla con dos elementos el segundo es de paginacion
        if len(lista_media) is not 0:
            return lista_media[0]  # Solo deuelve el que contiene media
        else:
            lista_media = []
            print('No hay imagenes del usuario')
            return lista_media
    except InstagramAPIError, e:
        print('Error generado por el ApiInstagram: {0}'.format(str(e.message)))


def obtener_like_media_usuario_token(api):
    try:
        lista_media = api.user_liked_media()  # Devuelvelve Tupla con dos elementos el segundo es de paginacion
        if len(lista_media) is not 0:
            return lista_media[0]  # Solo deuelve el que contiene media
        else:
            lista_media = []
            print('No hay media usuario token like')
            return lista_media
    except InstagramAPIError, e:
        print('Error generado por el ApiInstagram: {0}'.format(str(e.message)))


def obtener_datos_usuario(api, user_id):
    try:
        usuario = api.user(user_id)
        return usuario  # Devuelve el objeto Media con la informacion del usuario
    except InstagramAPIError, e:
        print('Error generado por el ApiInstagram al obtener datos del usuario'.format(str(e.message)))


def buscar_usuarios_por_key(api, key='UNAM', numero_usuarios='10'):
    try:
        lista_usuarios = api.user_search(q=key, count=numero_usuarios)
        if len(lista_usuarios) is not 0:
            return lista_usuarios  # Devuelve una lista con los nombre de usuario
        else:
            lista_usuarios = []
            print('No hay usuarios con esa palabra clave')
            return lista_usuarios
    except InstagramAPIError, e:
        print('Error generado por el ApiInstagram al buscar usuarios por palabra clave: {0}'.format(str(e.message)))


def obtener_seguidores_de_usuario(api, id_usuario):
    try:
        lista_seguidores = api.user_followed_by(id_usuario)

        if len(lista_seguidores) is not 0:
            return lista_seguidores[0]  # Solo deuelve el que contiene media
        else:
            lista_seguidores = []
            print('No se encontraron seguidores del usuario')
            return lista_seguidores
    except InstagramAPIError, e:
        print('Error generado por el ApiInstagram al obtener Followers: {0}'.format(str(e.message)))


def obtener_media_popular(api, numero_media=10):
    """

    :rtype : list
    """
    try:
        lista_media = api.media_popular(count=numero_media)

        if len(lista_media) is not 0:
            return lista_media
        else:
            print('No se encontro media popular')
            return lista_media
    except InstagramAPIError, e:
            print('Error generado por el ApiInstagram al obtener Media Popular: {0}'.format(str(e.message)))


def obtener_usuarios_con_like(api, id_media):
    try:
        lista_usuarios = api.media_likes(id_media)
        if len(lista_usuarios) is not 0:
            return lista_usuarios
        else:
            print('No se encontraron usuarios que dieran like a la imagen')
            return lista_usuarios
    except InstagramAPIError, e:
            print('Error generado por el ApiInstagram al obtener usuarios like en Media: {0}'.format(str(e)))


def obtener_informacion_tag(api, nombre_tag):
    try:
        informacion_tag = api.tag(nombre_tag)
        if len(informacion_tag) is not 0:
            return informacion_tag
        else:
            print('No hay informacion sobre ese tag')
            return informacion_tag
    except InstagramAPIError, e:
        print('Error generado por el ApiInstagram al obtener informacion del tag: {0}'.format(str(e.message)))


def obtener_media_por_tag(api, tag, numero_media=10):
    try:
        lista_media = api.tag_recent_media(count=numero_media, tag_name=tag)
        if len(lista_media) is not 0:
            return lista_media[0]  # Solo deuelve el que contiene media
        else:
            print('No se encontraron imagenes con ese tag.')
            return lista_media
    except InstagramAPIError, e:
        print('Error generado por el ApiInstagram al obtener Media Por Tag: {0}'.format(str(e.message)))
    except ServerNotFoundError, e:
        print("Error de servidor: {0}".format(str(e.message)))
        lista = []
        return lista


def obtener_tags_por_key(api, key, numero_tags='10'):
    try:
        lista_tags = api.tag_search(q=key, count=numero_tags)
        if len(lista_tags) is not 0:
            return lista_tags[0]  # Solo deuelve el que contiene media
        else:
            print('No se encontraron tags con esa palabra.')
            return lista_tags
    except InstagramAPIError, e:
        print('Error generado por el ApiInstagram al obtener Tags por palabra clave: {0}'.format(str(e.message)))


def obtener_ubicaciones_por_coordenadas(api, latitud, longitud, numero_ubicaciones):
    try:
        lista_ids_ubicaciones = api.location_search(count=numero_ubicaciones, lat=latitud, lng=longitud)
        if len(lista_ids_ubicaciones) is 0:
            return lista_ids_ubicaciones
        else:
            print('No se encontraron ubicaciones con esas coordenadas.')
            return lista_ids_ubicaciones
    except InstagramAPIError, e:
        print('Error generado por el ApiInstagram al obtener Locations por palabra clave: {0}'.format(e.message))


def obtener_informacion_de_ubicacion(api, id_ubicacion):
    try:
        informacion_location = api.location(id_ubicacion)
        if len(informacion_location) is not 0:
            return informacion_location
        else:
            print('No hay informacion sobre esa Ubicacion')
            return informacion_location
    except InstagramAPIError, e:
        print('Error generado por el ApiInstagram al obtener informacion de Location: {0}'.format(e.message))


def obtener_media_por_id_ubicacion(api, id_ubicacion, numero_media=10):
    try:
        lista_media = api.location_recent_media(count=numero_media, location_id=id_ubicacion)
        if len(lista_media) is not 0:
            return lista_media[0]  # Solo deuelve el que contiene media
        else:
            print('No se encontro media en esa Ubicacion.')
            return lista_media
    except InstagramAPIError, e:
        print('Error generado por el ApiInstagram al obtener Media Location: {0}'.format(e.message))


def obtener_media_por_coordenadas_ubicacion(api, key='unam', numero_media=10, latitud=19.32590558, longitud=-99.18214):
    try:
        lista_media = api.media_search(key, numero_media, latitud, longitud)

        if len(lista_media) is not 0:
            return lista_media
        else:
            print('No se encontraron imagenes en ese lugar')
            return lista_media
    except InstagramAPIError, e:
            print('Error generado por el ApiInstagram al obtener Media Por Location: {0}'.format(e.message))


def mostrar_datos_media(media):
    try:
        print 'Usuario: {0}'.format(str(media.user.username))
        print 'Tipo: {0}'.format(str(media.type))
        print "Text: {0}".format(str(media.caption))
        print "Numero de Comentarios: {0}".format(str(media.comment_count))
        print "Comentarios: {0}".format(str(media.comments))
        print "Filtros: {0}".format(str(media.filter))
        print "Numero de likes: {0}".format(str(media.like_count))
        print "Le gusta al usuario: {0}".format(str(media.user_has_liked))
        print "En Instagram {0}".format(str(media.link))
        print "Fecha y Hora: {0}".format(str(media.created_time))
        print "Imagenes: {0}".format(str(media.images))
        print "Likes: {0}".format(str(media.likes))
    except AttributeError, e:
        print "Error de algun atributo: {0}".format(e.message)
    try:
        print media.tags
    except AttributeError, e:
        print "No contiene tags: {0}".format(e.message)


def mostrar_lista_media(lista_media):
    for media in lista_media:
        mostrar_datos_media(media)
        print('\n')


def obtener_urls_de_lista_media(lista_media, resolucion='low_resolution'):
    """

    :rtype : list
    """
    lista = []
    for elemento_media in lista_media:
        lista.append(elemento_media.images[resolucion].url)
    return lista


def guardar_elementos_lista_nueva(lista_mayor, lista):
    for elemento_lista in lista:
        lista_mayor.append(elemento_lista)

def obtener_imagenes_varias_ubicaciones(api, numero_imagenes=20, numero_ubicaciones=10):
    """

    :rtype : list
    """
    lista_total = []
    latitud = raw_input("\tLatitud: ")
    longitud = raw_input("\tLongitud: ")
    lista_id_locations = obtener_ubicaciones_por_coordenadas(api, latitud, longitud, numero_ubicaciones)
    for location in lista_id_locations:
        lista_media = obtener_media_por_id_ubicacion(api, location.id, numero_imagenes)
        guardar_elementos_lista_nueva(lista_total, lista_media)
    if len(lista_total) is 0:
        print('No se encontraron imagenes en la ubicaciones de estas coordenadas :(.')
    else:
        print('Se encontraron {0} imagenes'.format(len(lista_total)))
    return lista_total