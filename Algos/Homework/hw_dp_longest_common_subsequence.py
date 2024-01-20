'''
Two sequences are given. 
Find the length of their longest common subsequence (a subsequence — is what can be obtained from a given sequence by deleting some elements).
'''


def diff(a:int, b:int):
    if a == b:
        return True
    else:
        return False
 
 
def lcs(a:list, b:list, n:int, m:int):

    # DP Initialization
    dp = [[0] * (n + 1) for _ in range(m + 1)]

 
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if  diff(b[i - 1], a[j - 1]):
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(
                    dp[i][j - 1],
                    dp[i - 1][j]
            ) 
    return dp[m][n]
    
 
 
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    print(lcs(a, b, n, m))