import numpy as np
#1
m=np.random.random((10,10))
mmin=m.min()
mmax=m.max()
print(mmin, mmax)



#2
m1 = np.random.random(30)
mr = m1.mean()
print(mr)


#3
m2 = np.ones((10,10))
m2[1:-1,1:-1] = 0


#4
m3 = np.diag(np.arange(1, 5), k=-1)
print(m3)


#5 need help
i=1000
while True:
    i-=7
    print(i)