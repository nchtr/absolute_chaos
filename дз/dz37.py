#1
original_list = [1, 2, 3, 4, 5, 6, 7]
result_dict = {x: x**3 for x in original_list if x % 2 == 1}
print(result_dict)
#2
original_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
result_set = {x for x in original_list if x % 2 == 0}
print(result_set)
#3
print([x*10 for x in range(10)])
#4
def divisible_by_7(n):
    for i in range(n+1):
        if i % 7 == 0:
            yield i

for num in divisible_by_7(50):
    print(num, end=' ')
