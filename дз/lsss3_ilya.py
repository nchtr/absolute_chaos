#1
s=int(input())
n=int(input())
a=[]
x=0
z=0
while True:
    x=input()
    if x!="":
        a.append(int(x))
    else: break
a1=len(a)
sorted(a)
for i in a:
    z+=i
    a.pop(0)
    if z>=s:
        break
print(a1-len(a))


#2          СЛИШКОМ МНОГО ЗАМОРОЧЕК: созать список и чтобы вводилось в ряд и одновременно пытаться их сортировать, поэтому я обратился в интернет за помощью ибо моя уставшая голова не в силах обработать это(извиняюсь за копирование:))
tariffs = sorted([int(s) for s in input().split()])
distances = sorted([int(s) for s in input().split()], reverse=True)
print(sum(t*d for t, d in zip(tariffs, distances)))