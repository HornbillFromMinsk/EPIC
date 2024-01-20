"""

Special Numbers

A natural number will be called special if any three consecutive digits in it form a three-digit prime number. Given N
, it is required to find the number of special N -digit numbers.

Answer should be outputed modulo 10^9 + 9

Oservations:
if len > 3, we can not have zeros, since the condition (any three consecutive digits form prime) will not be satisfied.

"""
from math import sqrt
 
def is_prime(n):
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def count_3digit_primes():
    c = 0
    primes = set()
    for i in range(100, 1000):
        if is_prime(i):
            c += 1
            primes.add(i)
    return c, primes



def get_special_number_count(n:int):
    dp = {}
    c, primes = count_3digit_primes()

    if n == 3:
        return c
    
    prime_endings = set(map(lambda x: x % 100, primes))  

    # DP Initialization
    for i in prime_endings:
        dp[i] = [0] * (n + 1)

    for p in primes:
        if p % 100 > 9:
            dp[p % 100][3] += 1

    s = 0

    for i in range(4, n + 1):
        for p in primes:
            if (p // 10) in dp:
                dp[p % 100][i] += dp[p // 10][i -1]

    for v in dp.values():
        s += v[n]

    return s

    
if __name__ == '__main__':
    const = 10**9 + 9
    n = int(input())
    print(get_special_number_count(n) % const)

