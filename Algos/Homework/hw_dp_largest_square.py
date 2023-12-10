"""

The Largest Squares

"""
 
 
def get_max_square(a:list, n:int, m:int):
 
    # DP Initialization
    dp = a.copy()
    max_dp = 1
    coord = (1, 1)

    for i in range(n - 1):
        for j in range(m - 1):
            if a[i][j] == 1:
                if not(coord):
                    coord = (i, j)
                if ((a[i][j + 1] == 1) & (a[i + 1][j + 1] == 1) & (a[i + 1][j]) == 1):
                    if min(i, j) > 0:
                        dp[i][j] += max(min(a[i - 1][j], a[i - 1][j - 1], a[i][j - 1]), 1)
                    else:
                        dp[i][j] += 1
                    if dp[i][j] >= max_dp:
                        max_dp = dp[i][j]
                        coord = (i - (max_dp - 3), j - (max_dp - 3))

                    max_dp = max(max_dp, dp[i][j])
 
    return max_dp, coord

def matrix_input(n:int, m:int):
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    return a


    
if __name__ == '__main__':
    n, m = map(int, input().split())
    answer, coords = get_max_square(matrix_input(n, m), n, m)
    print(answer)
    print(*coords, sep = " ")