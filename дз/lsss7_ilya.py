#1      why not
def to_dict(lst):
    d={i:i for i in lst}
    return d


print(to_dict([s for s in input().split()]))


#2
def count_it(sequence):
    todict={int(i):sequence.count(i) for i in sequence}
    todictsort=sorted(todict.items(), key=lambda i: i[1], reverse=True)
    return dict(todictsort[:3])


print(count_it(input()))



#3
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


#4 из интернетов, тяжеловато
from collections import Counter
from functools import reduce
from operator import or_, add

d1 = {1: 12, 2: 33, 3: 10, 4: 10, 5: 2, 6: 90}
d2 = {1: 12, 3: 7, 4: 1, 5: 2, 7: 112}
d3 = {2: 3, 3: 3, 4: 60, 6: 8, 7: 25, 8: 71}
d4 = {3: 1, 4: 13, 5: 31, 9: 9, 10: 556}

def sum_dct(*dicts):
    return dict_transformer(*dicts)

def max_dct(*dicts):
    return dict_transformer(*dicts, op=or_)

def dict_transformer(*dicts, op=add):
    return dict(reduce(lambda a, b: op(Counter(a), Counter(b)), dicts))


print(max_dct(d1, d2))
print(sum_dct(d1, d4, d3)) 
print(max_dct(d1, d2, d3, d4))
print(sum_dct(d1, d2, d3, d4))
