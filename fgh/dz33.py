#1
class Square:
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side ** 2
    

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2
    

class CircleInSquare(Square, Circle):
    def __init__(self, side):
        Square.__init__(self, side)
        Circle.__init__(self, side / 2)
        
    def area_diff(self):
        return self.area() - Circle.area(self)


#2
class Wheels:
    def __init__(self, size, material):
        self.size = size
        self.material = material

    def change_size(self, new_size):
        self.size = new_size


class Engine:
    def __init__(self, power, fuel_type):
        self.power = power
        self.fuel_type = fuel_type

    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")


class Doors:
    def __init__(self, number, lock_type):
        self.number = number
        self.lock_type = lock_type

    def open(self):
        print("Doors opened")

    def close(self):
        print("Doors closed")


class Car(Wheels, Engine, Doors):
    def __init__(self, size, material, power, fuel_type, number, lock_type):
        Wheels.__init__(self, size, material)
        Engine.__init__(self, power, fuel_type)
        Doors.__init__(self, number, lock_type)

    def drive(self):
        self.start()
        print("Car is driving")

    def stop(self):
        print("Car is stopping")
        self.stop()



#3
import pickle

class Shape:
    def __init__(self):
        self.type = "Shape"
        
    def Show(self):
        print(f"This is a {self.type}")
        
    def Save(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)
            print(f"{self.type} has been saved to {filename}")
            
    @classmethod
    def Load(cls, filename):
        with open(filename, "rb") as file:
            obj = pickle.load(file)
            print(f"{obj.type} has been loaded from {filename}")
            return obj


class Square(Shape):
    def __init__(self, x, y, length):
        super().__init__()
        self.type = "Square"
        self.x = x
        self.y = y
        self.length = length
        
    def Show(self):
        super().Show()
        print(f"Position: ({self.x}, {self.y}), Length: {self.length}")
        
        
class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.type = "Rectangle"
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def Show(self):
        super().Show()
        print(f"Position: ({self.x}, {self.y}), Width: {self.width}, Height: {self.height}")
        
        
class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__()
        self.type = "Circle"
        self.x = x
        self.y = y
        self.radius = radius
        
    def Show(self):
        super().Show()
        print(f"Position: ({self.x}, {self.y}), Radius: {self.radius}")
        
        
class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.type = "Ellipse"
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def Show(self):
        super().Show()
        print(f"Position: ({self.x}, {self.y}), Width: {self.width}, Height: {self.height}")
        

shapes = [
    Square(10, 10, 50),
    Rectangle(20, 20, 100, 50),
    Circle(30, 30, 25),
    Ellipse(40, 40, 150, 75)
]

for i, shape in enumerate(shapes):
    shape.Save(f"shape_{i}.pickle")
    
loaded_shapes = []
for i in range(len(shapes)):
    loaded_shapes.append(Shape.Load(f"shape_{i}.pickle"))
    
for shape in loaded_shapes:
    shape.Show()
