"""

Special Numbers

A natural number will be called special if any three consecutive digits in it form a three-digit prime number. Given N
, it is required to find the number of special N -digit numbers.

Answer should be outputed modulo 10^9 + 9

"""
from math import sqrt
 
def is_prime(n):
    if n <= 3:
        return True
    for i in range(3, n//2, 2):
        if n % i == 0:
            return False
    return True
def count_3digit_primes():
    c = 0
    for i in range(100, 1000):
        if is_prime(i):
            c += 1
    return c

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
    const = 10**9
    a = count_3digit_primes()
    print(a % (const + 9))