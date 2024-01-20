'''
A ladder is a set of cubes in which each horizontal layer contains fewer cubes than the layer below it.

Count the number of different ladders that can be built from N cubes.
'''


def ladders(n: int):

    # DP Initialization
    # dp[i][j]: i - number of cubes, j - number of cubes inthe lowest layer
    dp = [[0] * (n + 1) for _ in range(n + 1)]


    # One ladder from one cube
    dp[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, i):
            s = 0
            for r in range(1, j):
                s += dp[i - j][r]
            dp[i][j] = s
        dp[i][i] = 1

    return sum(dp[n])
 

 
if __name__ == '__main__':
    n = int(input())
    print(ladders(n))