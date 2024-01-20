''' 
Develop a program that, when presented with two vertices within a tree structure, 
ascertains whether one is the ancestor of the other.

Let's use the euler tour for the task.
Got the execution failure on the test 23 -> suspect the reccurtion depth limit. 
v2: Rewrite to stack. Store the (vertex, child) pair in the stack to calculate time
'''

 
def dfs_without_rec_timer(root, g, visited, euler, tin, tout):
	stack = [(root, -1)]
	while stack:
		u, child = stack.pop()
		if child == -1:
			if visited[u]:
				continue
			visited[u] = True
			tin[u] = len(euler)
			euler.append(u)
		
		next_child = list(filter(lambda x: x > child, g[u]))
		if next_child:
			child = next_child[0]
			stack.append((u, child))
			if not visited[child]:
				stack.append((child, -1))
		else:
			euler.append(u)
			tout[u] = len(euler)


	
def is_ancestor(a, b, tin, tout):
	ans = 1 if tin[a] < tin[b] < tout[b] < tout[a] else 0
	return ans
 

if __name__=='__main__':
	graph, euler = [], []
	n = int(input())
	
	visited, tin, tout = [False] * n, [0] * n, [0] * n
	
	for i in range(n):
		graph.append([])
	
	for i, from_ in enumerate(map(int, input().split())):
		if from_ > 0:
			graph[from_ - 1].append(i)
		else:
			start = i
	
	dfs_without_rec_timer(start, graph, visited, euler, tin, tout)
	
	
	answers = []
	m = int(input())
	
	for _ in range(m):
		a, b = tuple(map(int, input().split()))
		answers.append(is_ancestor(a - 1, b - 1, tin, tout))
		
	for a in answers:
		print(a)