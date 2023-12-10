'''
Insertion Sort
'''

def insertion_sort(a, n):
    for idx in range(1, n):
        X = a[idx]
        j = idx - 1
        while (j >= 0) and (X < a[j]):
            if a[j] > X:
                a[j], a[j + 1] = a[j + 1], a[j]
            j-=1
    return a

# Driver code
if __name__=='__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(*insertion_sort(a, n), sep=' ')
