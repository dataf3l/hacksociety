import cherrypy


class HelloWorld(object):
    """
    1.- Nombre
    2.- Tiene productos con este banco ?
    3.- Edad
    4.- Genero ?
    5.- Extranjero ó residente?
    6.- Nivel de educativo? Postgrado, Profesional, Bachiller.
    7.- Nivel de ingresos. menor ó igual a
    50000, 100000, 150000, 200000, 250000, ó 300000
    """

    def index(self, **json):
        print(json)
        return """{
         "messages": [
           {"text": "hola, todo funciona111"},
           {"text": "Va a comprar, o que?"}
         ]
        }"""
    index.exposed = True

cherrypy.server.socket_host = '0.0.0.0'
cherrypy.quickstart(HelloWorld())
