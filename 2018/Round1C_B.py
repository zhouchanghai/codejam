import sys,random
def solve(n):
    like = [0]*n #like[i] is the number of person like flavor i
    status = [1] * n #1 available, 0 sold
    for person in range(n):
        flavors = [int(x) for x in input().split()]
        if flavors[0] == -1: #error
            sys.exit(1)
        flavors = flavors[1:]
        if not flavors: #like 0 flavor
            print(-1)
            continue
        for f in flavors:
            like[f] += 1
        pf = [(like[f], f) for f in flavors if status[f]]
        if not pf: #liked all sold
            print(-1)
            continue
        pf.sort()
        for j in range(1, len(pf)):
            if pf[j][0] != pf[0][0]:
                pf[j:] = []
                break
        p, f = random.choice(pf)
        status[f] = 0
        print(f)

tn = int(input())
for tc in range(1, tn + 1):
    N = int(input())
    solve(N)
