# %%
print("OOP")

# %%
# int float str 
number = 6 
type(number)

# %%
def toFly():
    return 0

class Bird:
    pass

# %%
class Car:
    axis = 0 # coordinate
    lane = 0
    velocity = 0

    def toDrive(self):
        return 0

class Road:
    length = 0
    width = 0

    def __init__(self, length) -> None:
        self.length = length

    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

road_one = Road(100, 50)


# %%
road_one.length

# %%
road_one.length = 100
road_one.width = 50


# %%
road_one.length

# %%
bird = Bird()

# %%
bird.name = 'parrot'

# %%
dir(bird)

# %%
bird.name

# %%
list1 = [1,2,3,4,5]



# %%
list1.index(1)

# %%
class ListElements:
    val = 1

class MyList:
    idx = 0
    next_value = ListElements()
    length = 5

    def getIndex(self, searching):
        for i in self.length:
            if self.val == searching:
                return self.idx

# chain 



# %%
# Class methods: Getters and Setters
class Building:
    height = 0
    width = 0
    floors = 0
    roof = ''
    city = ''

    def getHeigth(self):
        return self.height
    
    def setHeight(self, new_height):
        self.height = new_height

house = Building()

house.setHeight(10)
house.getHeigth()



# %%



