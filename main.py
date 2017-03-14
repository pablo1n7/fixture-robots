from Robot import Robot
from Fixture import Fixture

def main():
    robots = [
        Robot("Ultron","Del Mal","Iron Man"),
        Robot("Wall-e","Pixar","Señor Disney"),
        Robot("Sony","Del Mal","Spooner"),
        Robot("Robocop","Primaria de Springfield","Rafa Gorgory")
        ]
    
    fixture = Fixture(robots)
    print("Hola Mundo")

if __name__ == '__main__':
    main()

