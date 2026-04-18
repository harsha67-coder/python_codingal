class bird:
    def __init__(self):
        print("bird is ready")
    def WhoIsThis(self):
        print("bird")
    def swim(self):
        print("bird jumbed into the water and started swimming")
class penguin(bird):
    def __init__(self):
        super().__init__()
        print("penguin is ready")
    def WhoIsThis(self):
        print("penguin is here")
    def walk(self):
        print("penguin took a walk to sahara desert now!!!")
peggy=penguin()
peggy.swim()
peggy.WhoIsThis()
peggy.walk()
