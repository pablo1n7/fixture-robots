class Robot(object):
    nombre = ""
    escuela = ""
    encargado = "" #consultar el reglamento para poner un nombre mejor

    def __init__(self,_nombre,_escuela,_encargado):
        self.nombre = _nombre
        self.escuela = _escuela
        self.encargado = _encargado

    def __str__ (self):
        return self.nombre