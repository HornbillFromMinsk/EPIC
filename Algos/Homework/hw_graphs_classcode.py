# 3 ways to represent the graph: adjasency matrix, list of edges, list of lists (list of all the verticies, the vertex has an edge with)
# Agjasency matrix bad in memory for sparse graphs

n, m = map(int, input().split(' '))
 
# Matrix 
Matrix = []
# List of lists
l = []
for _ in range(n):
	Matrix.append([False] * n)
	l.append([])
 
for i in range(m):
	from_, to = map(int, input().split(' '))
	Matrix[from_ - 1][to - 1] = True
	# Matrix[to - 1][from_ - 1] = True # for non-oriented
	l[from_ - 1].append(to - 1)
	# l[to - 1].append(from_ - 1)
 
print(Matrix)
print(l)



visited = [False for _ in range(n)]
# dfs
def dfs_tree(u, p, g):
	visited[u] = True
	print(u)
	for v in g[u]:
		if v != p:
			dfs_tree(v, u, g)

# dfs
def dfs(u, g):
	visited[u] = True
	print(u)
	for v in g[u]:
		if not visited[v]:
			dfs(v, g)

depth = [0] * n
def dfs_depth(u, p, g, depth):
	for v in g[u]:
		if v != p:
			depth[v] = depth[u] + 1
			dfs_depth(v, u, g, depth)



def dfs_without_rec(root, g, visited):
	stack = [root]
	while stack:
		u = stack.pop()
		visited[u] = True
		for v in g[u]:
			if not visited[v]:
				stack.append(v)

#dfs_without_rec(0, l, visited)
				

from collections import deque

INF = 10**9
distance = [INF] * n
def dfs_dist(g, root, distance):
	queue = deque([root])

	distance[root] = 0

	while queue:
		u = queue.popleft()
		for v in g[u]:
			if distance[v] == INF:
				distance[v] = distance[u] + 1
				queue.append(v)		
 
 
dfs_dist(l, 0, distance)
 
print(distance)




