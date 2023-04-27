#1
c=int(input())
l1=0
l=sorted([int(s) for s in input().split()], reverse=True)
print(l)
if c<3:
    print(sum(l))
else:
    for i in range(0, c, 3):
        l1+=l[i]
    for i in range(1, c, 3):
        l1+=l[i]
    print(l1)
    
    
#2
li=sorted([int(s) for s in input().split()])
t = 0
t1 = 1
for i in range(len(li)-1):
    for j in range(i+1,len(li)):
        if abs(li[i] - li[j]) < abs(li[t] -li[t1]):
            t = i
            t1 = j
print(t,t1)
