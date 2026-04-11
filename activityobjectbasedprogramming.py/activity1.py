class car:
    def __init__(self, model , milage , engine , tyre , distance ):
        self.model=model
        self.milage=milage
        self.engine=engine
        self.tyre=tyre
        self.distance=distance

    def calculate_fuel_use(self,distance):
        fuel_use=distance/self.milage
        print("fuel used is",fuel_use,"for",distance)

audi=car("Audi",12,"v12",14,310)
lamborghini=car("Lamborghini",17,"v12",14,310)
    
    
audi.calculate_fuel_use(310)
lamborghini.calculate_fuel_use(310)

