#1
class Digit:
    def __init__(self, digit) -> None:
        self._dig=digit
    
    def __add__(self, other):
        return self._dig + other

    def __sub__(self, other):
        return self._dig - other

    def __div__(self, other):
        return self._dig / other 

    def __mul__(self, other):
        return self._dig * other
    
    
d=Digit(6)
print(d+36)



#2
class Fraction:
    def __init__(self, numerator, denominator) -> None:
        self.numerator = numerator
        self.denominator = denominator
        self.canonize()
    
    def canonize(self):
        def gcd(a,b):
            while a != 0 and b != 0:
                if a > b:
                    a %= b
                else:
                    b %= a
            return a+b
        
        g = gcd(self.numerator, self.denominator)
        self.numerator //= g
        self.denominator //= g
        
    def __float__(self):
        return self.numerator / self.denominator
        
    def __trunc__(self):
        return self.numerator // self.denominator
        
    def __int__(self):
        return self.__trunc__()
        
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
        
    def __repr__(self):
        return f"Fraction({str(self)})"
        
    def __round__(self, ndigits=None, /):
        return round(float(self), ndigits)
        
    def __add__(self, value):
        return Fraction(self.numerator*value.denominator + value.numerator*self.denominator, self.denominator*value.denominator)
        
    def __mul__(self, value):
        return Fraction(self.numerator*value.numerator, self.denominator*value.denominator)
        
    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)
        
    def __sub__(self, value, /):
        return Fraction(self.numerator*value.denominator - value.numerator*self.denominator, self.denominator*value.denominator)
        
    def __truediv__(self, value):
        return Fraction(self.numerator*value.denominator, self.denominator*value.numerator)
    
    

#3
class Library:
    def __init__(self, name, addr, books) -> None:
        self._name=name
        self._addr=addr
        self._books=books
        
#math
    def __add__(self, other):
        return self._books + other

    def __sub__(self, other):
        return self._books - other

    def __div__(self, other):
        return self._books / other 

    def __mul__(self, other):
        return self._books * other
    
    def __iadd__(self, other):
        return self._books + other

    def __isub__(self, other):
        return self._books - other

    def __idiv__(self, other):
        return self._books / other 

    def __imul__(self, other):
        return self._books * other
#comp
    def __eq__(self, __o: object) -> bool: # == eq-equal
        return self._books == __o

    def __ne__(self, __o: object) -> bool: # != ne-non-equal
        return self._books != __o

    def __lt__(self, __o: object) -> bool: # < lt-less than
         return self._books < __o

    def __gt__(self, __o: object) -> bool: # > gt-greater than
         return self._books > __o

    def __le__(self, __o: object) -> bool: # <=
        return self._books <= __o

    def __ge__(self, __o: object) -> bool: # >=
        return self._books >= __o