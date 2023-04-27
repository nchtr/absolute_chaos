#1
def superset(set1, set2):
    if set1.issuperset(set2):
        print(f'Объект {set1} является чистым супермножеством')
    elif set1.issubset(set2):
        print('Супермножество не обнаружено')
    elif set1==set2:
        print('Множества равны')


superset({s for s in input()}, {p for p in input()})

#2
dictionary={'Hello':'Bonjour', 'Thanks':'Merci', 'Goodbye':'Au revoir'}
print(f'The dictionary you have: {dictionary}')
t=int(input("Select operation:\n1-Add or Edit\t2-Remove\t3-Search\n"))
if t==1:
    print("Add or Edit")
    ji=input('Enter:')
    ij=input('Enter:')
    dictionary.update({ji:ij})
elif t==2:
    print("Remove")
    try:
        dictionary.pop(input())
    except KeyError as e:
        print("There is no matching element")
elif t==3:
    b=input("Search: ")
    print(dictionary.get(b))
else:
    print("wut?")
    
    

#3
def set_gen(lst):
    ix = 0
    while ix < len(lst):
        cnt = lst.count(lst[ix])
        if cnt > 1:
            lst[ix] = str(lst[ix]) * cnt
        ix += 1
    return set(lst)

print(set_gen([int(s) for s in input().split()]))
