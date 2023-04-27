#1
try:
    list=range(0,6)
    for i in range(len(list)+1):
        print(list[i])
    
except IndexError:
    print("WE REACHED THE END OF LIST!!!!!!!")