from Robot import Robot
from Fixture import Fixture

def main():
    robots = [Robot("Ultron","Los Avengers","Nick Fury"),
	          Robot("Wall-e","Pixar","Sr. Disney"),
	          Robot("Sony","R&H Mecanicos","Dt. Spooner"),
	          Robot("Robocop","O.C.P.","Bob Morthon"),
	          Robot("Terminator","Skynet","Jhon Connor"),
	          Robot("R2-D2","La Republica","Obiwan Kenobi"),
	          Robot("3-CPO","La Republica","Anakin Skywalker"),
	          Robot("BB-8","La Republica","Poe Dameron")] 

    fixture = Fixture(robots)
    print("Hola Mundo")

if __name__ == '__main__':
    main()

