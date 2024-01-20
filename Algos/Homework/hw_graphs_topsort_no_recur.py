''' 
A directed unweighted graph is given. It is necessary to sort it topologically.

For Top Sort we need the graphto be acyclic. Therefore, use the color-coding instead of bool visited flag to detect the cycle.
W - default value
G - started processing (added to the recursion stack)
B - processed (deleted from the recursion stack)

Got the execution failure on the test 18 -> suspect the reccurtion depth limit, again. 
v2: Rewrite to stack. Store the (vertex, child) pair in the stack to calculate time
'''

from collections import deque
 
def dfs_without_rec(start, g, color, topsort):
    stack = [(start, -1)]
    while stack:
        u, child = stack.pop()
        if child == -1:
            if color[u] == "B":
                continue
            color[u] = "G"
        
        if g[u]:
            child = g[u].pop()
            stack.append((u, child))
            if color[child] == "W":
                stack.append((child, -1))
            if color[child] == "G":
                return True
        else:
            topsort.appendleft(u + 1)
            color[u] = "B"
    return False
 
    
 
def TopSort(g, n):
    color = ["W"] * n
    topsort = deque()
 
    for i in range(n):
        if color[i] != 'B':
            if dfs_without_rec(i, g, color, topsort):
                return [-1]
 
    return topsort

n, m = map(int, input().split(' '))
 
graph = []

for i in range(n):
    graph.append([])
 
for i in range(m):
    from_, to = map(int, input().split(' '))
    graph[from_ - 1].append(to - 1)

print(*TopSort(graph, n), sep = ' ')