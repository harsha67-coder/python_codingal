class ferrari:
    def __init__(self,engine,max_speed,colour):
        self.engine=engine
        self.max_speed=max_speed
        self.colour=colour

    def display(self):
        print("engine used in this car is",self.engine)
        print("max speed of this car is",self.max_speed)
        print("the colour of this car is",self.colour)

class porche(ferrari):
    def __init__(self,engine,max_speed,colour,car_model):
        ferrari.__init__(self,engine,max_speed,colour)
        self.car_model=car_model

obj=porche("v12",190,"red",911)
obj.display()