# derivatives

EPS = 10 ** (-9)

def f(x):
    return 2 * x * x - 3 * x + 5 

def good(x):
    return f(x) - f(x - EPS) <= 0


l, r = -10, 10
ops = 100

while ops > 0:
    mid = (l + r) / 2
    if good(mid):
        l = mid
    else:
        r = mid
    ops -= 1
    print(f(mid))

print(l, r)