#1
s1={1, 2, 3, 4, 5, 6, 12, 24}
print(s1)
s1.discard(int(input("Enter number you want to remove: ")))
print(s1)
#2
s2={1, 2, 4, 'Apple', 'John', 'CS', 'Mango', 'Grapes'}
print(s2)
s2.update({3, True})
print(s2)
#3
s3={2, 6, 99, False}
s4={2, 'sugar',6 , False}
s3.union(s4)
print(s3)
#4
countries={'Kazakhstan', 'Georgia', 'Egypt', 'Japan', 'Germany'}
print(f'List of countries you have: {countries}')
t=int(input("Select operation:\n1-Add\t2-Remove\t3-Search\t4-Check\n"))
if t==1:
    print("Add")
    countries.add(input('Name of country: '))
elif t==2:
    print("Remove")
    countries.remove(input("Name of country(enter in true register): "))
elif t==3:
    b=input("Search: ")
    for i in countries:
        if b in i:
            print(i)
    else:
        print('No results')
elif t==4:
    print(input('Country: ') in countries)
else:
    print("wut?")
