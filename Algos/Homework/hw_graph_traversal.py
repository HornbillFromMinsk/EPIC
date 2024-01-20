'''
Given an undirected, unweighted graph, you need to find the number of vertices in the same connected component as a given vertex (including this vertex).
'''

def dfs(start, g, n):
    visited = [False] * n

    count = 0
    stack = [start]
 
    while stack:
        u = stack.pop()
        if not visited[u]:
            visited[u] = True
            count += 1
 
            for v in range(n):
                if g[u][v] == 1 and not visited[v]:
                    stack.append(v)
    return count
 


n, s = map(int, input().split(' '))
 
# Matrix 
Matrix = []
 
for i in range(n):
	Matrix.append(list(map(int, input().split(' '))))
 
print(dfs(s - 1, Matrix, n))