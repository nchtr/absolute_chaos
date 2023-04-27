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