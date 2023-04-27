l = [input()]
while True:
    n=input()
    if n not in l:
        l.append(n)
    elif n == "":
        break
for i in l:
    print(i)