def gids(a:list, n:int):
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if (a[i] % a[j] == 0):
                dp[i] = max(dp[j] + 1, dp[i])
    return max(dp)

# Driver code
if __name__=='__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(gids(a, n))