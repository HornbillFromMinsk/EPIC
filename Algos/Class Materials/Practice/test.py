def count_numbers(k, n, flag) : 
 
    # Base case 
    if (n == 1) : 
 
        # If 0 wasn't chosen previously 
        if (flag) : 
            return (k - 1) 
        else : 
            return 1
 
    # If 0 wasn't chosen previously 
    if (flag) : 
        return (k - 1) * (count_numbers(k, n - 1, 0) +
                          count_numbers(k, n - 1, 1)) 
    else :
        return count_numbers(k, n - 1, 1) 
 
# Driver code 

k = 4
print(list(count_numbers(k, n, True) for n in range(1,9)))

dp =[3, 12, 45] + [0]*5
for i in range(3, 7):
    dp[i] = dp[i-1] +3*dp[i-2]

print(dp)

'''
dp = [1,1,2] + [0]*15
for i in range(3, 15):
    dp[i] = dp[i-1] + dp[i-2]
l = ['{}: {}'.format(i+1, el) for i, el in enumerate(dp)]
print(l, sep = " ")
'''


def solve_recurrence(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return (7 * solve_recurrence(n - 2) - 3 * solve_recurrence(n - 1))/2

# Example usage:

for n in range(2, 15):
    print(f"The value of a{n} is: {solve_recurrence(n)}")