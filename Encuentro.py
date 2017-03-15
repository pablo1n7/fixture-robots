class Encuentro(object):
    robot_l = None
    robot_v = None
    ganador = None

    def __init__(self,_robots):
        self.robot_l = _robots[0]
        self.robot_v = _robots[1]
        return
    
    
    def gano(self, _nombre_r):
        """  """
        # pass
        if self.robot_l.nombre == _nombre_r:
            self.ganador = self.robot_l
    
        elif self.robot_v.nombre == _nombre_r:
            self.ganador = self.robot_v
        
        else:
            raise Exception('No pertece al encuentro')
    
    def get_ganador(self):
        """  """
        # pass
        return self.ganador

            