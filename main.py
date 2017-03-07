from Robot import Robot
from Fixture import Fixture

def main():
    robots = [Robot({"nombre":"Ultron","escuela":"Hogwarts","encargado":"Navarro Pablo"}),
        Robot({"nombre":"Ultron1","escuela":"Hogwarts","encargado":"Navarro Pablo"}),
        Robot({"nombre":"Ultron2","escuela":"Hogwarts","encargado":"Navarro Pablo"}),
        Robot({"nombre":"Ultron3","escuela":"Hogwarts","encargado":"Navarro Pablo"})]
    
    fixture = Fixture({"robots":robots})

    import ipdb
    ipdb.set_trace()

if __name__ == '__main__':
    main()

