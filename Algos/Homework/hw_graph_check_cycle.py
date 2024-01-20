'''
Given a directed graph. It is required to determine whether there is a cycle in it.
'''


def dfs_no_recur(start, g, color):
    stack = [(start, -1)]
    while stack:
        u, child = stack.pop()
        if child == -1:
            if color[u] == 'B':
                continue
            color[u] = 'G'

        if g[u]:
            child = g[u].pop()
            stack.append((u, child))
            if color[child] == 'W':
                stack.append((child, -1))
            if color[child] == 'G':
                return True
        else:
            color[u] = 'B'
    return False

def check_cycle(g, n):
    color = ['W'] * n
    for v in range(n):
        if color[v] != 'B':
            if dfs_no_recur(v, g, color):
                return 1
    return 0

n, m = map(int, input().split(' '))
 
graph = []
for i in range(n):
    graph.append([])
 
for i in range(m):
    from_, to = map(int, input().split(' '))
    graph[from_ - 1].append(to - 1)
 
print(check_cycle(graph, n))