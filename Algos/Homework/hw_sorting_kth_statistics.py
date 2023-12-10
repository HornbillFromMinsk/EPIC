'''
Kth Statistics
O(n) in the average case
Re-using my quick sort code with an adjustment to check the position of pivot and 

search only in the partition, the kth element can be located, or return k if pivot's position = k.
'''

import random
from sys import maxsize

def random_partition(a:list, l:int, r:int):
    pivot = random.randrange(l, r)
    a[r], a[pivot] = a[pivot], a[r]
    return partition(a, l, r)

def partition(a:list, l:int, r:int):

    pivot = a[r]
    i = l
    for j in range (l, r):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1 # 'shift a "wal" '
    a[r], a[i] = a[i], a[r]
    return i

def _quick_select(a, k, l, r):
    if (l < r) & (l >= 0):
        pivot = random_partition(a, l, r)
        if pivot - l == k:
            return a[pivot]
        elif pivot - l < k:
            return _quick_select(a, k - (pivot - l) - 1, pivot + 1, r)     
        else:
            return _quick_select(a, k, l, pivot - 1)

    return maxsize

def quick_select(a, n, k):
    # We can not return kth element if there are n<k elements in the array
    if n < k:
        return

    if n < 2:
       return a[0]
    
    return _quick_select(a, k - 1, l = 0, r = n - 1)


if __name__=='__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(quick_select(a, n, k))
