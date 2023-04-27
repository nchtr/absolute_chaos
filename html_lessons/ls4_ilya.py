#1
class Point:
    def __init__(self, x, y) -> None:
        self.x=x
        self.y=y
    
    def getDistance(self): return (self.x**2 + self.y**2)**0.5
    
    def getPoint(self): return (self.x, self.y)
    

class PointColor(Point):
    def __init__(self, x, y, color) -> None:
        super().__init__(x, y)
        self.color=color
        
    def getColor(self): return self.color
    



#2
class Pet:
    def __init__(self, sound, show, type) -> None:
        self.sound=sound
        self.show=show
        self.type=type
        
class Dog(Pet):
    def __init__(self, sound, show, type) -> None:
        super().__init__(sound, show, type)
    
    def getSound(self):
        print(self.sound)
    
    def getShow(self):
        print(self.show)
    
    def getType(self):
        print(self.type)
    
    
class Cat(Dog):
    def __init__(self, sound, show, type) -> None:
        super().__init__(sound, show, type)

class Parrot(Dog):
    def __init__(self, sound, show, type) -> None:
        super().__init__(sound, show, type)

class Hamster(Dog):
    def __init__(self, sound, show, type) -> None:
        super().__init__(sound, show, type)
        


#3
class Employer:
    def Print(self):
        print("This is Employer class.")

class President(Employer):
    def Print(self):
        print("I am the President.")

class Manager(Employer):
    def Print(self):
        print("I am a Manager.")

class Worker(Employer):
    def Print(self):
        print("I am a Worker.")

        
