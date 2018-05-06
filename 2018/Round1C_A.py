
def solve(words):
    prefix = [""]
    L = len(words[0])
    for pos in range(L):
        chs = set()
        newPrefix = set()
        for w in words:
            chs.add(w[pos])
            newPrefix.add(w[:pos+1])
        for p in prefix:
            for ch in chs:
                pr = p + ch
                if pr not in newPrefix:
                    return pr + words[0][pos+1:]
        prefix = newPrefix
    return "-"

tn = int(input())
for tc in range(1, tn + 1):
    N, L = [int(s) for s in input().split(" ")]
    words = []
    for i in range(N):
        words.append(input())
    ret = solve(words)
    print("Case #{}: {}".format(tc, ret))
