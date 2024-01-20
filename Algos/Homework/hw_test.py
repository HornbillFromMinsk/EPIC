''' 
A directed unweighted graph is given. It is necessary to sort it topologically.

For Top Sort we need the graphto be acyclic. Therefore, use the color-coding instead of bool visited flag to detect the cycle.
W - default value
G - started processing (added to the recursion stack)
B - processed (deleted from the recursion stack)

Got the execution failure on the test 18 -> suspect the reccurtion depth limit, again. 
v2: Rewrite to stack. Store the (vertex, child) pair in the stack to calculate time
'''
import random

def dfs_new(u, graph,  colors, color):
    colors[u] = color
    for v in graph[u]:
        if colors[v] == 0:  
            if ( not dfs_new(v, graph, colors, 1 if color == 2 else 2)):
                return False
        elif (colors[v] == color):
            return False
    return True


def check_split_to_groups_new(g, n):
    colors = [0] * n
    result = True
    for i in range(n):
        if not result:
            break
        if colors[i] == 0:
            result = dfs_new(i, g, colors, 1)
    if result:
        return "YES"
    else:
        return "NO"
 

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
 


'''
n, m = map(int, input().split(' '))

for i in range(n):
    graph.append([])
 
for i in range(m):
    from_, to = map(int, input().split(' '))
    graph[from_ - 1].append(to - 1)

'''
for _ in range(100):
    graph = []
    n, m = random.randint(1, 1000), random.randint(0, 4500)
    for i in range(n):
        graph.append([])

    for i in range(m):
        from_, to = random.randint(1, n), random.randint(1, n)
        graph[from_ - 1].append(to - 1)


    try:
        assert check_split_to_groups(graph, n) == check_split_to_groups_new(graph, n)
    except:
        print(n, m, check_split_to_groups(graph, n), graph, check_split_to_groups_new(graph, n))
