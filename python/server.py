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

    def handle_name(self):
        global cust
        name = ""
        if "customer_name" in cust:
            name = cust["customer_name"]
        print(cust)
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

    def handle_age(self):
        global cust
        # age = ""
        # if "age" in cust:
        #    age = cust["age"]
        print(cust)
        return """{
          "messages": [
            {
              "attachment": {
                "type": "template",
                "payload": {
                  "template_type": "button",
                  "text": "May I know your gender?",
                  "buttons": [
                    {
                      "type": "show_block",
                      "block_name": "step2_client_is_male",
                      "title": "Male"
                    },
                    {
                      "type": "show_block",
                      "block_name": "step2_client_is_female",
                      "title": "Female"
                    }
                  ]
                }
              }
            }
          ]
        }
        """

    def index(self, **json):
        global cust
        if "customer_name" in json:
            cust["customer_name"] = json["customer_name"]
            return self.handle_name()
        if "age" in json:
            cust["age"] = json["age"]
            return self.handle_age()

    def ex_or_resident(self):
        return """{
          "messages": [
            {
              "attachment": {
                "type": "template",
                "payload": {
                  "template_type": "button",
                  "text": "Do you currently reside in Colombia?",
                  "buttons": [
                    {
                      "type": "show_block",
                      "block_name": "is_colombian",
                      "title": "yes, I live in Colombia"
                    },
                    {
                      "type": "show_block",
                      "block_name": "is_not_colombian",
                      "title": "No"
                    }
                  ]
                }
              }
            }
          ]
        }
        """

    def ask_income(self):
        return """{
          "messages": [
            {
              "attachment": {
                "type": "template",
                "payload": {
                  "template_type": "button",
                  "text": "What is your income?",
                  "buttons": [
                    {
                      "type": "show_block",
                      "block_name": "step4_income1",
                      "title": "Less than 25000"
                    },
                    {
                      "type": "show_block",
                      "block_name": "step4_income2",
                      "title": "Between 25000 and 50000"
                    },
                    {
                      "type": "show_block",
                      "block_name": "step4_income3",
                      "title": "  above 50000+"
                    }
                  ]
                }
              }
            }
          ]
        }
        """

    def done(self):
        global cust
        return """{
         "messages": [
           {"text": "Thank you:,"""+cust["customer_name"]+""""},
         ]
        }"""

    @cherrypy.expose
    def step4_income1(self, **json):
        global cust
        cust["income_class"] = "1"
        print(cust)
        return self.done()

    @cherrypy.expose
    def step4_income2(self, **json):
        global cust
        cust["income_class"] = "2"
        print(cust)
        return self.done()

    @cherrypy.expose
    def step4_income3(self, **json):
        global cust
        cust["income_class"] = "3"
        print(cust)
        return self.done()

    @cherrypy.expose
    def step3_is_colombian(self, **json):
        global cust
        cust["is_colombian"] = "0"
        print(cust)
        return self.ask_income()

    @cherrypy.expose
    def step3_is_not_colombian(self, **json):
        global cust
        cust["is_colombian"] = "1"
        print(cust)
        return self.ask_income()

    @cherrypy.expose
    def step2_client_is_male(self, **json):
        global cust
        cust["gender"] = "MALE"
        print(cust)
        return self.ex_or_resident()

    @cherrypy.expose
    def step2_client_is_female(self, **json):
        global cust
        cust["gender"] = "FEMALE"
        print(cust)
        return self.ex_or_resident()


#        return """{
#         "messages": [
#           {"text": "hola, """ + cust["customer_name"] + """"},
#           {"text": "Siguiente Pregunta"}
#         ]
#        }"""
    index.exposed = True

cherrypy.server.socket_host = '0.0.0.0'
cherrypy.quickstart(HelloWorld())
