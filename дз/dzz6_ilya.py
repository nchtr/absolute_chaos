#1
# M = 3
# simb=[]
# for i in range(M):
#     simb.append(input())

# max_len = max(len(i) for i in simb)
# for i in simb:
#     print('*' * (max_len - len(i)), i)


#2
import math
su=0
sumod=0
sumod1=0
sumod2=0
li=[int(s) for s in input().split()]
for i in li:
    if i<0:
        sumod1+=abs(i)
    else:
        sumod2+=i
sumod=sumod2-sumod1
sumod-=sumod1
for j in li:
    su+=j
print(f'Need {sumod-su}')

