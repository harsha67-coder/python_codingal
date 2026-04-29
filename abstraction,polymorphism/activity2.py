from abc import ABC,abstractmethod
class vehicle(ABC):
    def __init__(self,model,colour,price):
        self.model=model
        self.colour=colour
        self.price=price

    def display(self):
        print("the vehicle model is",self.model,"the colour of the vehicle is",self.colour,"the price is",self.price)

    @abstractmethod
    def wheels(self,no_of_wheels):
        pass


class car(vehicle):
    def __init__(self,brand,height):
        self.brand=brand
        self.height=height

    def wheels(self,no_of_wheels):
        self.no_of_wheels=no_of_wheels

BMW=car("BMW",7)
BMW.wheels(4)
