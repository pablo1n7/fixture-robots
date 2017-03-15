import random
from Encuentro import Encuentro

class Fixture(object):
    robots = []
    nro_robots = 0
    nro_rondas = 0
    encuentros = []

    def __init__(self,_robots):
        self.robots = _robots
        self.nro_robots = len(self.robots)
        # self.nro_rondas = len(_robots) if len(_robots)%2!=0 else len(_robots)-1

        return
    

    def vencedor(self, _robot):
        pass

    def get_encuentros(self, _ronda=-1):
        return self.encuentros[_ronda]
    
    def generar_encuentros(self, _robs=robots):
        print("robs: {}".format(_robs))
        if len(_robs)==2:
            return [Encuentro([_robs[0], _robs[1]])]
        
        _escuela = _robs[0].escuela
        _neutros = [r for r in _robs if r.escuela==_escuela]
        random.shuffle(_neutros)
        
        _contrincantes = [r for r in _robs if r.escuela!=_escuela]
        random.shuffle(_contrincantes)

        _rob_1 = _neutros[0]
        _encuentros = []
        if len(_contrincantes) !=0:
            _rob_2 = _contrincantes[0]
        else:
            _rob_2 = _neutros[1]
        
        _robs.remove(_rob_1)
        _robs.remove(_rob_2)
        _encuentros.append(Encuentro([_rob_1, _rob_2]))
        
        _encuentros.extend(self.generar_encuentros(_robs))
        
        return _encuentros


    def cambiar_ronda(self, _robots_ganadores):
        """ Avanza de ronda, generando los encuentros entre los robots ganadores
            Pre:
            Post: """
        print("Robots en juego:\n".format(_robots_ganadores))
        _encuentros_ronda = self.generar_encuentros(self.robots.copy())
        self.encuentros.append(_encuentros_ronda)
        return