#1
original_list = [1, -2, 3, -4, 5, -6]
new_list = [x**3 if x < 0 else x**2 for x in original_list if x % 2 == 0]
print(new_list)
#2
string_list = ['apple', 'banana', 'cherry', 'date']
new_list = [len(x) for x in string_list]
print(new_list)

#3
original_list = [1, 2, 3, 4, 5, 6]
new_list = [x**2 for x in original_list if x % 2 == 0]
print(new_list)
#4
original_list = [1, -10, 15, -20, 25, -30]
new_list = [x if x > 0 and x % 5 == 0 else 0 for x in original_list]
print(new_list)
#5
original_string = "hello world"
vowels = ['a', 'e', 'i', 'o', 'u']
new_list = [x for x in original_string if x.lower() in vowels]
print(new_list)
