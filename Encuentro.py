class Encuentro(object):
    robot_l = None
    robot_v = None
    ganador_v = False
    ganador_l = False

    def __init__(self,_robots):
        self.robot_l = _robots[0]
        self.robot_v = _robots[1]
        return
    
    def ganador(_robot):
        return True