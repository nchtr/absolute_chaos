#1
def avg(a, b):
    return (a * b) ** 0.5


try:
    a = float(input("a = "))
    b = float(input("b = "))
except ValueError:
    print("a or b must be digit")
c = avg(a, b)
print("Среднее геометрическое = {:.2f}".format(c))



#2
class Roman:
    ROMAN_VALUES = {"0":0, "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def __init__(self, roman_numeral):
        self.roman_numeral = roman_numeral
        self.decimal_value = Roman.to_decimal(roman_numeral)

    def __add__(self, other):
        result = self.decimal_value + other.decimal_value
        return Roman.from_decimal(result)

    def __sub__(self, other):
        result = self.decimal_value - other.decimal_value
        return Roman.from_decimal(result)

    def __mul__(self, other):
        result = self.decimal_value * other.decimal_value
        return Roman.from_decimal(result)

    def __truediv__(self, other):
        try:
            result = self.decimal_value / other.decimal_value
            return Roman.from_decimal(result)
        except ZeroDivisionError:
            return 'DONT DIVIDE BY ZERO'

    @staticmethod
    def to_decimal(roman_numeral):
        decimal_value = 0
        prev_value = 0

        for char in roman_numeral:
            curr_value = Roman.ROMAN_VALUES.get(char, 0)
            if curr_value > prev_value:
                decimal_value += curr_value - 2 * prev_value
            else:
                decimal_value += curr_value
            prev_value = curr_value

        return decimal_value

    @staticmethod
    def from_decimal(decimal_value):
        if decimal_value < 1 or decimal_value > 3999:
            raise ValueError("Invalid Roman numeral value")

        result = ""
        for numeral, value in sorted(Roman.ROMAN_VALUES.items(), key=lambda item: -item[1]):
            while decimal_value >= value:
                result += numeral
                decimal_value -= value

        return Roman(result)


