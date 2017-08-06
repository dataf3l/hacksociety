import cherrypy


class HelloWorld(object):
    def index(self):
        return """{
         "messages": [
           {"text": "hola, todo funciona"},
           {"text": "Va a comprar, o que?"}
         ]
        }"""
    index.exposed = True

cherrypy.server.socket_host = '0.0.0.0'
cherrypy.quickstart(HelloWorld())
