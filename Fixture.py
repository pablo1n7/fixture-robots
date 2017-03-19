import random
from Encuentro import Encuentro

class Fixture(object):
    
    def __init__(self, robots):
        self.robots = robots
        self.rondas = []


    def vencedor(self, robot):
        pass


    def ronda(self):
        robots = not self.rondas and self.robots or [e for e in self.rondas[-1] if e.ganador() ]
        self.rondas.append(self._generar_encuentros(robots))


    def encuentros(self, ronda):
        return self.rondas[ronda]
    

    def _generar_encuentros(self, _robs):
        if len(_robs) == 2:
            return [Encuentro(_robs[0], _robs[1])]
        
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
        _encuentros.append(Encuentro(_rob_1, _rob_2))
        
        _encuentros.extend(self._generar_encuentros(_robs))
        
        return _encuentros


    def cambiar_ronda(self, _robots_ganadores):
        """ Avanza de ronda, generando los encuentros entre los robots ganadores
            Pre:
            Post: """
        print("Robots en juego:\n".format(_robots_ganadores))
        _encuentros_ronda = self.generar_encuentros(self.robots.copy())
        self.encuentros.append(_encuentros_ronda)
        return
    