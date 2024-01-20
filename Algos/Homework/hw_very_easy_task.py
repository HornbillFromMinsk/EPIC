'''
VERY EASY TASK
min time to print n copies
'''

def good(t, x, y):
    return t / x + t / y <= n

def bin_find_min_time(n, x, y):
    # Initially we can print the first copy using only one printer
    t = min(x, y) 
    if n == 1:
        return t
    n -= 1
    l = 0
    r = (n + 1) * t

    while l < r - 1:
        mid = (l + r) // 2
        if good(mid, x, y):
            l = mid
        else:
            r = mid
    return l + t
# Driver code
if __name__=='__main__':
    
    n, x, y = map(int, input().split())

    print(bin_find_min_time(n, x, y))