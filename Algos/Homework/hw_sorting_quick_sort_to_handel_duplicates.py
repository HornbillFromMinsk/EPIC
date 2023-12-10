'''
Quick Sort v2.
I was able to imitate the failed test - the max recursion depth is exceeded
for the long arrays consisting of the same elements (duplicates).
This is an attempt to put the elements equal to pivot in the third (middle) partition,
and sort only the other two partitions.

'''
import random

def random_partition(a:list, l:int, r:int):
    pivot = random.randrange(l, r)
    a[r], a[pivot] = a[pivot], a[r]
    return partition(a, l, r)

def partition(a:list, l:int, r:int):

    pivot_l, pivot_r = l, l 
    pivot = a[r]

    while  (pivot_r <= r):
        if (a[pivot_r] < pivot):
            a[pivot_l], a[pivot_r] = a[pivot_r], a[pivot_l]
            pivot_r = pivot_r + 1
            pivot_l = pivot_l + 1
        elif (a[pivot_r] > pivot):
            a[r], a[pivot_r] = a[pivot_r], a[r]
            r = r - 1
        else:
            # shifting the right border of the partition with el = pivot
            pivot_r = pivot_r + 1

    return pivot_l, pivot_r

def _quick_sort(a, l, r):
    if (l < r) & (l >= 0):
        # pivot_l, pivot_r will be the borders of the middle partition,
        # containing the elements equal to pivot
        pivot_l, pivot_r = random_partition(a, l, r)
        _quick_sort(a , l, pivot_l - 1)
        _quick_sort(a, pivot_r , r)
    else: 
        return a
    return a

def quick_sort(a, n):
    if n < 2:
       return a
    return _quick_sort(a, l = 0, r = n - 1)


if __name__=='__main__':
    n = int(input())
    a = list(map(int, input().split()))

    print(*quick_sort(a, n), sep=" ")