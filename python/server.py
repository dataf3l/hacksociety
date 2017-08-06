import cherrypy
global cust
cust = {}


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
        global cust
        if "customer_name" in json:
            cust["customer_name"] = json["customer_name"]

        name = ""
        if "customer_name" in cust:
            name = cust["customer_name"]
        print(json)
        return """{
          "messages": [
            {
              "attachment": {
                "type": "template",
                "payload": {
                  "template_type": "button",
                  "text": "Hello """ + name + """! do you have an existing financial product with us? ",
                  "buttons": [
                    {
                      "type": "show_block",
                      "block_name": "Edad",
                      "title": "Yeah"
                    },
                    {
                      "type": "show_block",
                      "block_name": "non_existing",
                      "title": "Nope"
                    }
                  ]
                }
              }
            }
          ]
        }
        """

#        return """{
#         "messages": [
#           {"text": "hola, """ + cust["customer_name"] + """"},
#           {"text": "Siguiente Pregunta"}
#         ]
#        }"""
    index.exposed = True

cherrypy.server.socket_host = '0.0.0.0'
cherrypy.quickstart(HelloWorld())
