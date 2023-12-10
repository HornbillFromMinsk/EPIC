'''
GIS
'''

import bisect

INF = 1e9

def dp_1_gis(a:list, n:int):
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if (a[j] < a[i]):
                dp[i] = max(dp[j] + 1, dp[i])
    return max(dp)

def dp_3_gis(a:list, n:int):
# First dp value is -inf, other inf
    dp = [-INF] + [INF] * (n - 1)
    for i in range(n):
        for j in range(1, n + 1):
            if dp[j - 1] < a[i] and a[i] < dp[j]:
                dp[j] = a[i]
    return max([el for el in dp if el != INF])

def gis_logn(a:list, n:int):
# First dp value is -inf, other inf
    dp = [-INF] + [INF] * (n - 1)
    for i in range(n):
        j = bisect.bisect_left(dp, a[i], 1)
        if dp[j - 1] < a[i] and a[i] < dp[j]:
            dp[j] = a[i]
    return max([el for el in dp if el != INF])

def gds_logn(a:list, n:int):
# Still need to figure this out
    dp = [-INF] + [INF] * (n - 1)
    for i in range(n):
        j = bisect.bisect_left(dp, a[i], 1)
        if dp[j - 1] < a[i] and a[i] < dp[j]:
            dp[j] = a[i]
    return max([el for el in dp if el != INF])

# Driver code
if __name__=='__main__':
#    n = int(input())
#   a = list(map(int, input().split()))
    n = 5
    a = [5, 3, 4, 4, 2]
    print(gis_logn(a, n))