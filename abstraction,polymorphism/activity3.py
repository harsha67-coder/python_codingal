from abc import ABC,abstractmethod
class animal(ABC):
    def __init__(self,colour,fur):
        self.colour=colour
        self.fur=fur

    @abstractmethod
    def legs(self,no_of_legs):
        pass
    
    def legs(self,no_of_legs):
        self.legs=no_of_legs
        print("this animal has",self.legs,"number of legs")
class human(animal):
    def __init__(self,colour,fur):
        animal.__init__(self,colour,fur)

    def legs(self,no_of_legs):
        self.legs=no_of_legs
        print("this animal has",self.legs,"number of legs")


class cow(animal):
    def __init__(self,colour,fur):
        animal.__init__(self,colour,fur)
    def legs(self,no_of_legs):
        self.legs=no_of_legs
        print("this animal has",self.legs,"number of legs")
me = human("dark","no fur")
me.legs(2)
moose=cow("dark","has fur")
moose.legs(4)
monkey=animal("light","has fur")
monkey.legs(4)