'''
Simple binary search

'''

# Simple coded solution

def good(i, k):
    return i < k

def binary_search(a: list, v: int):
    l, r = 0, len(a) - 1
    while l <= r:
        mid = (l + r) // 2
        if v > a[mid]:
            l = mid + 1
        elif v < a[mid]:
            r = mid - 1
        else:
            return mid + 1
    return -1

def binary_search_float(a: list, v: float):
    l, r = 0, len(a) - 1
    op = 100 # compl. log(r-l) + -log(eps) + C
    while op > 0:
        op -= 1
        mid = float((l + r) / 2)
        if v >= a[mid]:
            l = mid
        if v < a[mid]:
            r = mid
    return mid


# Driver code
if __name__=='__main__':
    
    a = list(map(float, input().split()))
    v = float(input())
    print(binary_search_float(a, v))
1