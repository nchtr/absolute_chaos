# 1
alphabet = " abcdefghijklmnopqrstuvwxyz"
a=0
unil=[]
key = int(input())
s = input()
subst = dict(zip(alphabet, alphabet[key:]+alphabet[:key]))
res = ''.join(map(subst.__getitem__, s)) 
resl=list(res)
for i in resl:
    a=ord(i)
    unil.append(a)
print(res)
print(*unil)


# 2 / 3
fruits=('banana', 'pineapple', 'apple', 'bananaapple', 'cherry')
ch=input()
z=0
x=0
for i in fruits:
    if i==ch:
        z+=1
    elif ch in i:
        x+=1
print(z, x)



#4
cars=('Chevy', 'Ford', 'Toyota', 'Volkswagen', 'Chevy', 'Ford', 'Toyota', 'Volkswagen', 'Chevy', 'Ford', 'Toyota', 'Volkswagen')
cc=list(cars)

check=input()
repl=input()
for i in range(len(cc)):
    if cc[i]==check:
        cc[i]=repl
print(tuple(cc))
