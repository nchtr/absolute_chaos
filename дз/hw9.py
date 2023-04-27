a=int(input())
b=int(input())
m=max(b,a)
while True:
    if m%b==0 and m%a==0:
        print(m)
        break
    else:
        m+=1   