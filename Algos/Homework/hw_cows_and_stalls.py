'''

Try to match principles:
If can place the cows with the distance a, the distance b < a is also reachable
We can check x by trying to reach such distance
l = min distance between stalls (1), r max distance between stalls + 1 (1000)
Obvious, for k = 2, the optimal solution is first and last stall cause our array is sorted.

'''


def good(dist, cows, arr):
    '''Check if we'll manage to place cows with such distance'''
    # First cow goes to the first stall. If the optimal distance is reachable with placing the 1st cow in nth stall,
    # we can move it to the first one an min distance will remain the same
    cow_pos = arr[0]
    cows -= 1

    for curr_stall in arr[1:]:
        if curr_stall - cow_pos >= dist:
            cow_pos = curr_stall
            cows -= 1
        if cows == 0:
            break

    return cows == 0

def bin_cows_in_stalls(cows, coords):

    distances =  [n - p for n, p in zip(coords[1:], coords[:-1])]

    l = min(distances)
    r = sum(distances) + 1

    while l < r - 1:
        mid = (l + r) // 2
        if good(mid, cows, coords):
            l = mid
        else:
            r = mid
    return l


# Driver code
if __name__=='__main__':
    
    stalls_num, cows_num = map(int, input().split())
    coords = list(map(int, input().split()))
    print(bin_cows_in_stalls(cows_num, coords))
        

