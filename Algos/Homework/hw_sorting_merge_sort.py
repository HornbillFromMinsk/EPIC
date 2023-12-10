'''
Merge Sort

'''

def merge(a:list, b:list):
    aidx = 0
    bidx = 0
    res = []
    while aidx < len(a) and bidx < len(b):
        if b[bidx] < a[aidx]:
            res.append(b[bidx])
            bidx += 1
        else:
            res.append(a[aidx])
            aidx += 1
    # Add from the array which still has some elements
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
    return merge(l_arr, r_arr)


if __name__=='__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(*merge_sort(a, n), sep=" ")
