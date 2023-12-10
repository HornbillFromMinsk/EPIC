# put your python code here

'''
Counting Sort
'''

# From the problem statement
C = 10**4 + 1

def selection_sort(a, n):
    b = [0] * C
    a_new = [0] * n
    for el in a:
        b[el] += 1
    for i in range(1, C):
        b[i] = b[i] + b[i - 1]
    for j in range(n - 1, -1, -1):
        a_new[b[a[j]] - 1] = a[j]
        b[a[j]] -= 1
    return a_new

if __name__=='__main__':
    n = int(input())
    a = list(map(int, input().split()))

    print(*selection_sort(a, n), sep=' ')