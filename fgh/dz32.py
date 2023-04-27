#1
class Device:
    def __init__(self, power):
        self.power = power

    def switch_on(self):
        print("Device is switched on.")

    def switch_off(self):
        print("Device is switched off.")


class CoffeeMachine(Device):
    def __init__(self, power, brand, model):
        super().__init__(power)
        self.brand = brand
        self.model = model

    def make_coffee(self):
        print("Making coffee.")


class Blender(Device):
    def __init__(self, power, brand, model):
        super().__init__(power)
        self.brand = brand
        self.model = model

    def blend(self):
        print("Blending.")


class MeatGrinder(Device):
    def __init__(self, power, brand, model):
        super().__init__(power)
        self.brand = brand
        self.model = model

    def grind_meat(self):
        print("Grinding meat.")



#2
class Ship:
    def __init__(self, name, length, displacement):
        self.name = name
        self.length = length
        self.displacement = displacement

    def sail(self):
        print(f"The ship {self.name} is sailing.")

    def anchor(self):
        print(f"The ship {self.name} is anchoring.")



class Frigate(Ship):
    def __init__(self, name, length, displacement, missile_count):
        super().__init__(name, length, displacement)
        self.missile_count = missile_count

    def fire_missile(self):
        print(f"Frigate {self.name} is firing missile.")
        
class Frigate(Ship):
    def __init__(self, name, length, displacement, missile_count):
        super().__init__(name, length, displacement)
        self.missile_count = missile_count

    def fire_missile(self):
        print(f"Frigate {self.name} is firing missile.")



class Cruiser(Ship):
    def __init__(self, name, length, displacement, missile_count, gun_count):
        super().__init__(name, length, displacement)
        self.missile_count = missile_count
        self.gun_count = gun_count

    def fire_missile(self):
        print(f"Cruiser {self.name} is firing missile.")

    def fire_gun(self):
        print(f"Cruiser {self.name} is firing gun.")

