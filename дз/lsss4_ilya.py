#1
def check(l):
    while True:
        l[int(input("Num: "))]+=1
        if l[0]: break
        print(l)
        
        
l = [0]*10
check(l)
print(*l[1:])




#2
# list=[]
# def linesear(list, k):
#     for i in range(len(list)):
#         if list[i] == k:
#             print("True")
#             return i
#     return "Not found"


# for i in range(10):
#     k=int(input("Num: "))
#     list.append(k)
# print(linesear(list, int(input("Key: "))))
