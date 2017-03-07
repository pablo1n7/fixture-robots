class Robot(object):
    nombre = ""
    escuela = ""
    encargado = "" #consultar el reglamento para poner un nombre mejor

    def __init__(self, parameter_list):
        self.nombre = parameter_list["nombre"]
        self.escuela = parameter_list["escuela"]
        self.encargado = parameter_list["encargado"]

    def __str__ (self):
        return self.nombre