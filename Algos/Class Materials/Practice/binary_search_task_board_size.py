'''
Task 2
You have n pictures with size (a, b)
You need to buy a board with size (size, size)
What is the minimum size you need to fit all the pictures in.
Example a = 2, b = 3, n = 10, answer = 9
'''

'''
The most obvious formula n/(x+y) (and round in greater side)

Try to match principles:
If can fit all pics with size s1, we can do it with the size s2 as well

if (size / a) * (size / b) >= n then size is enough
size 0 - never enough, n*max(a,b) is always enough

'''


a = int(input())
b = int(input())
n = int(input())

def good(size):
    return (size // a) * (size // b) < n

l = 0
r = n * max(a, b) # So we place them in one row or one column

while l < r - 1:
    mid = (l + r) // 2
    if good(mid):
        l = mid
    else:
        r = mid
print(l, r)
