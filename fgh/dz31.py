#1
class Circle:
    def __init__(self, radius):
        self.radius = radius

    # оператор ==
    def __eq__(self, other):
        return self.radius == other.radius

    # оператор >
    def __gt__(self, other):
        return self.radius > other.radius

    # оператор <
    def __lt__(self, other):
        return self.radius < other.radius

    # оператор <=
    def __le__(self, other):
        return self.radius <= other.radius

    # оператор >=
    def __ge__(self, other):
        return self.radius >= other.radius

    # оператор +
    def __add__(self, other):
        return Circle(self.radius + other.radius)

    # оператор -
    def __sub__(self, other):
        return Circle(self.radius - other.radius)

    # оператор +=
    def __iadd__(self, other):
        self.radius += other.radius
        return self

    # оператор -=
    def __isub__(self, other):
        self.radius -= other.radius
        return self

    def __repr__(self):
        return f"Circle({self.radius})"


#2
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # оператор +
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    # оператор -
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    # оператор *
    def __mul__(self, other):
        return Complex(self.real*other.real - self.imag*other.imag, self.real*other.imag + self.imag*other.real)

    # оператор /
    def __truediv__(self, other):
        denominator = other.real**2 + other.imag**2
        return Complex((self.real*other.real + self.imag*other.imag)/denominator,
                       (self.imag*other.real - self.real*other.imag)/denominator)

    def __repr__(self):
        return f"({self.real}, {self.imag}i)"


#3
class Airplane:
    def __init__(self, type, max_passengers, current_passengers):
        self.type = type
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers

    # оператор ==
    def __eq__(self, other):
        return self.type == other.type

    # оператор +
    def __add__(self, passengers):
        if self.current_passengers + passengers > self.max_passengers:
            raise ValueError("Too many passengers")
        else:
            self.current_passengers += passengers
            return self

    # оператор -
    def __sub__(self, passengers):
        if self.current_passengers - passengers < 0:
            raise ValueError("Negative number of passengers")
        else:
            self.current_passengers -= passengers
            return self

    # оператор +=
    def __iadd__(self, passengers):
        return self.__add__(passengers)

    # оператор -=
    def __isub__(self, passengers):
        return self.__sub__(passengers)

    # оператор >
    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    # оператор <
    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    # оператор >=
    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    # оператор <=
    def __le__(self, other):
        return self.max_passengers <= other.max_passengers


#4
class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __le__(self, other):
        return self.price <= other.price
