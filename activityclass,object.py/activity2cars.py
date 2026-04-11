class vehicle:
    wheels=4
    def __init__(self,name,max_speed,milage):
        self.name=name
        self.max_speed=max_speed
        self.milage=milage

    def fuel_use(self,distance):
        fuel_needed=distance/self.milage
        print("fuel needed is "+ str(fuel_needed) +"litres")
    
bmw = vehicle("bmw",270,18)
porche = vehicle("porsche 911",340,34)

print(bmw.max_speed)
print(porche.max_speed)
print(porche.wheels)