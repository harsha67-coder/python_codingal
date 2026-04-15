class dad:
    def __init__(self,eye,skin_colour):
        self.eye=eye
        self.skin_colour=skin_colour

    def display(self):
        print("ur eye colour is",self.eye)
        print("ur skin colour is",self.skin_colour)

class son(dad):
    def __init__(self,eye,skin_colour,hair_colour):
        dad. __init__(self,eye,skin_colour)
        self.hair_colour=hair_colour

obj=son("blue","fair","black")
obj.display()

            

