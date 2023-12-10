'''
Quick Sort

'''
import random

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

def _quick_sort(a, l, r):
    if (l < r) & (l > 0):
        pivot = random_partition(a, l, r)
        _quick_sort(a , l, pivot-1)
        _quick_sort(a, pivot + 1, r)
    else: 
        return a
    return a

def quick_sort(a, n):
    if n < 2:
       return a
    return _quick_sort(a, l = 0, r = n - 1)


if __name__=='__main__':
 #   n = int(input())
 #   a = list(map(int, input().split()))
    n = 10**3
    a = []
    for i in range(n):
        a.append(0)

    print(*quick_sort(a, n), sep=" ")
