'''

Hints for binsearch

if x is good, then y > x or y < x is also good
We can somehow check if x is good
We can guess left and right bound(later we will need only one of them)

'''


'''
Task 1
We have two printers
The first one prints x pages per minute
The second one prints y pages per minute
You need to print n pages, how much time will it take?
Example, x = 3, y = 4, n = 12, answer = 2 minutes
Example, x = 3, y = 4, n = 25, answer = 4 minutes
'''

'''
The most obvious formula n/(x+y) (and round in greater side)

Try to match principles:
If we can print all pages in t1 secs then we can print them in t2>t1 secs as well
if x*t + y*t >= n then t minutes is enough
0 - never enough, n/x is always enough

'''

x = int(input())
y = int(input())
n = int(input())

def good(t):
    return x * t + y * t < n

l = 0
r = (n - 1) // x + 1 # Why?

while l < r - 1:
    mid = (l + r) // 2
    if good(mid):
        l = mid
    else:
        r = mid
print(l, r)