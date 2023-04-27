import math
def findWinner(votes):
    n = len(votes);
    prev = 0
    res = ""
    for i in range(0, n): 
        count = 0
        for j in range(0, n): 
            if (votes[i] == votes[j]):
                count += 1
            if (count > prev):
                prev = count
                res = votes[i]
            elif (count == prev) :
                res = min(res, votes[i])
    print(res)

votes = [ "Аскаров", "Бекмуханов", "Ернур", "Пешая", "Карим", "Шаримазданов", "Аскаров", "Бекмуханов", "Карим", 'Шаримазданов', "Аскаров", "Бекмуханов", "Ернур", "Пешая", "Карим", "Шаримазданов"]

findWinner(votes)