def diff(a:str, b:str):
    if a == b:
        return 0
    else:
        return 1
 
 
def levenstein_dist(a:str, b:str):
    n, m, = len(a), len(b)
 
    # DP Initialization
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(1, m + 1):
        dp[i][0] = i
    for j in range(1, n + 1):
        dp[0][j] = j
 
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(
                dp[i][j - 1] + 1,
                dp[i - 1][j] + 1,
                dp[i - 1][j - 1] + diff(b[i - 1], a[j - 1]),
            )
            if (
                (i > 1)
                and (j > 1)
                and (diff(b[i - 1], a[j - 2]) == 0)
                and (diff(b[i - 2], a[j - 1]) == 0)
            ):
                dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + diff(b[i - 1], a[j - 1]))
 
    return dp[m][n]
    
 
 
if __name__ == '__main__':
    a, b = input(), input()
    print(levenstein_dist(a, b))