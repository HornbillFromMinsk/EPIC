'''
We have 3 cows and 5 stalls - [1, 2, 3, 100, 1000]
The answer = 99
first cow - 1
second cow - 100
third cow - 1000
'''

'''

Try to match principles:
If can place the cows with the distance a, the distance b<a is also reachable
We can check x by trying to reach such distance
l = min distance between stalls (1), r max distance between stalls + 1 (1000)


'''