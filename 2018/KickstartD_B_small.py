
def solve(p,h,x,y):
    N, K = len(p), len(x)
    ret = 0
    for i in range(K):
        for j in range(N):
            if y[i]+abs(p[j]-x[i]) <= h[j]:
                ret += 1
                break
    return ret
    
def getPos(n):
    x1,x2,a,b,c,m = [int(x) for x in input().split()]
    ret = [x1,x2]
    for i in range(n-2):
        ret.append((a*ret[-1] + b*ret[-2] + c)%m + 1)
    return ret
    
tn = int(input())
for tc in range(1, tn + 1):
    N, K = [int(x) for x in input().split()]
    p = getPos(N)
    h = getPos(N)
    x = getPos(K)
    y = getPos(K)
    ret = solve(p,h,x,y)
    print("Case #{}: {}".format(tc, ret))
