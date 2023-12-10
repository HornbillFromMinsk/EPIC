'''
Selection Sort
'''

def selection_sort(a, n):
    for idx in range(n):
        min_i = idx # Set min to the first unsorted el
        for j in range(idx, n):
            if a[j] < a[min_i]:
                min_i = j
        a[idx], a[min_i] = a[min_i], a[idx]
    return a

# Driver code
if __name__=='__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(*selection_sort(a, n), sep=' ')
