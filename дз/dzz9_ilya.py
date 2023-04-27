#1
# my_dict = {'first_one': 'we can do it'}
# def biggest_dict(**kwargs):
#     my_dict.update(**kwargs)


# biggest_dict(k1=22, k2=31, k3=11, k4=91)
# biggest_dict(name='Елена', age=31, weight=61, eyes_color='grey')
# print(my_dict)

#2
from collections import OrderedDict
dct = OrderedDict({1: 1, 2: 2, 3: 3, 4: 4, 5: 5})
first = list(dct.items())[0]
last = list(dct.items())[-1]
dct.move_to_end(key=first[0])
dct.move_to_end(key=last[0], last=False)
second = list(dct.items())[1]
del dct[second[0]]
dct['new_key'] = 'new_value'
print(dct, id(dct))

#3 (шаблон?)
countries={'Turkey':'Ankara', 'Georgia':'Tbilisi', 'Russia':'Moscow'}
countries_saveslot={}
print(f'The playlist you have: {countries}')
t=int(input("Select operation:\n1-Add or Edit\t2-Remove\t3-Search\n"))
if t==1:
    print("Add or Edit")
    countries.update({input():input()})
elif t==2:
    print("Remove")
    try:
        countries.pop(input())
    except KeyError as e:
        print("There is no matching element")
elif t==3:
    b=input("Search: ")
    print(countries.get(b))
else:
    print("wut?")