'''
Inversions

'''
c = 0

def inversion_cnt(a, n):
# O(n^2), Exceeds time limit
    cnt = 0
    for i in range(n):
        for j in range(i, n - 1):
            if a[i] > a[j + 1]:
                cnt += 1
    return cnt

def merge_invers_count(a:list, b:list):
# n(logn). Had to use the global var for the recursive approach.
# Maybe the iterative one is better for the task.
    aidx = 0
    bidx = 0
    res = []
    global c
    while aidx < len(a) and bidx < len(b):
        if b[bidx] < a[aidx]:
            res.append(b[bidx])
            bidx += 1 
            c += len(a) - aidx
        else:
            res.append(a[aidx])
            aidx += 1
    if aidx < len(a):
        res += a[aidx:]
    if bidx < len(b):
        res += b[bidx:]

    return res

def merge_sort(a, n):

    if n < 2:
       return a    
    mid = n // 2
    l_arr = merge_sort(a[:mid], mid)
    r_arr = merge_sort(a[mid:], n - mid)
    return merge_invers_count(l_arr, r_arr)


if __name__=='__main__':
    n = int(input())
    a = list(map(int, input().split()))
    merge_sort(a, n)
#    assert inversion_cnt(a, n) == c
    print(c)
