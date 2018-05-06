#Ant Stack
def solve(weights):
    n = len(weights)
    #minW[i] is the min weight to form a i length stack
    minW = [0]
    for w in weights:
        tmp = [0]
        for i in range(1, len(minW)):
            if minW[i-1]+w < minW[i] and minW[i-1] <= 6*w:
                tmp.append(minW[i-1]+w)
            else:
                tmp.append(minW[i])
        if minW[-1] <= w*6:
            tmp.append(w+minW[-1])
        minW = tmp
    return len(minW)-1

import math
#When n is 140, the last weight > 10**9
#So the max stack length is 139
def generateInput(n):
    weights = [1]
    totalW = 1
    for i in range(n-1):
        weights.append(math.ceil(totalW/6))
        totalW += weights[-1]
    print(1)
    print(n)
    print(" ".join(str(x) for x in weights))

tn = int(input())
for tc in range(1, tn + 1):
    n = int(input())
    weights = [int(x) for x in input().split()]
    print("Case #{}: {}".format(tc, solve(weights)))
