class Roman:
    ROMAN_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

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
        result = self.decimal_value // other.decimal_value
        return Roman.from_decimal(result)

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
