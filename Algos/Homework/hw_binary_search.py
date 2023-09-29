'''
Input
The first line contains the numbers n and k (1≤n,k≤105)
The second line contains n elements of the first array sorted in ascending order, 
The third line — k elements of the second array. 

For each of the k, numbers in the second array, 
print on a separate line «YES» if that number occurs in the first array, and «NO» otherwise.'''


def good(mid: int, v: int, arr: list):
    return arr[mid] < v

def bin_search(v: int, arr: list):
    l, r = -1, len(arr)

    if (v < arr[0]) or (v > arr[r - 1]):
        return "NO"

    while l < r - 1:
        mid = (l + r) // 2
        if arr[mid] < v:
            l = mid
        elif arr[mid] > v:
            r = mid
        else: 
            return "YES"
    return "NO"

# Driver code
if __name__=='__main__':
    
    n, k = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))

    res = dict()
    for el in arr_b:
        if el in res:
            print(res[el])
        else:
            res[el] = bin_search(el, arr_a)
            print(res[el])
        