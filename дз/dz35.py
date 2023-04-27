#1
def plus_two(num1, num2):
    return num1+num2
try:
    number=int(input("Enter a number: "))
    print(plus_two(2, number))
except ValueError:
    print("Ожидаемый тип данных— число!")