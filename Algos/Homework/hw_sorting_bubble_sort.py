'''
Bubble sort
'''

def bubble_sort(a, n):
    cnt = 0
    for _ in range(n):
        for idx in range(len(a) - 1):
            if a[idx] > a[idx + 1]:
                a[idx], a[idx + 1] = a[idx + 1], a[idx]
                cnt += 1
 
    return a, cnt

# Driver code
if __name__=='__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(*bubble_sort(a, n), sep=' ')