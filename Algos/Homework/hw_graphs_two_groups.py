'''

Mikhail Dmitrievich has recorded all the pairs of lkshats who exchanged notes.
 It is required to determine whether he can divide the lkshat into two groups so that any exchange of notes 
 is carried out from the lkshon of one group to the lkshon of the other group.

It is necessary to derive the answer to Pavel Olegovich's problem. 
If it is possible to divide lkshat into two groups, print "YES"; otherwise print "NO".

Idea: try to color the nodes
'''



next_color = {"G": "B", "B": "G"}

def dfs(g, u, colors, color):
    colors[u] = color
 
    for v in g[u]:
        if colors[v] == "W":            
            if not dfs(g, v, colors, next_color[color]):
                return False
        elif colors[v] == color: # If the next vertex is of the same color - contradiction
            return False

    return True
 
    
 
def check_split_to_groups(g, n):
    colors = ['W'] * n
 
    for i in range(n):
        if colors[i] == 'W':
            if not dfs(g, i, colors, 'G'):
                return "NO"
    return "YES"
 
n, m = map(int, input().split(' '))
 
graph = []

for i in range(n):
    graph.append([])
 
for i in range(m):
    from_, to = map(int, input().split(' '))
    graph[from_ - 1].append(to - 1)
 
print(check_split_to_groups(graph, n))