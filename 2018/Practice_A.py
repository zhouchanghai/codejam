#Number Guessing
def run():
    a,b = input().split()
    a,b = int(a)+1, int(b)
    n = int(input())
    for i in range(n):
        guess = (a+b)//2
        print(guess)
        resp = input()
        if resp == "CORRECT":
            return
        if resp == "TOO_SMALL":
            a = guess + 1
            continue
        if resp == "TOO_BIG":
            b = guess - 1
            continue
        if resp == "WRONG_ANSWER":
            return

t = int(input())
for i in range(t):
    run()
