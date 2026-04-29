from abc import ABC,abstractmethod
class vehicle(ABC):
    def __init__(self,name,max_speed,milage):
        self.name=name
        self.max_speed=max_speed
        self.milage=milage

    @abstractmethod
    def wheels(self,number):
        self.wheels=number

class car(vehicle):
    def __init__(self,name,max_speed,milage,colour):
        super().__init__(name,max_speed,milage)
        self.colour=colour

    def wheels(self,number):
        self.wheels=number
        print("this car has",self.wheels,"number of wheels")

class bus(vehicle):
    def __init__(self,name,max_speed,milage,colour):
        super().__init__(name,max_speed,milage)
        self.colour=colour

    def wheels(self,number):
        self.number=number
        print("this bus has",self.number,"number of wheels")

audi=car("Audi",280,12,"red")
public_bus=bus("Ferrari",300,14,"yellow")
audi.wheels(4)
public_bus.wheels(6)
        



