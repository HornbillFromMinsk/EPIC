def dfs( g, v, p, visited, depth, cut_points, h, dp):
    visited[v] = True
    dp[v] = h[v] = depth
    children = 0
    for u in g[v]:
        if u != p:
            if visited[u]:
                dp[v] = min(dp[v], h[u]) # back edge
            else:
                dfs(g, u, v, visited, depth + 1, cut_points, h, dp)
                dp[v] = min(dp[v], dp[u])
                if (h[v] <= dp[u]) and (p != -1): 
                    cut_points.append(v + 1)
                children += 1

    if (p == -1) and (children > 1):
        cut_points.append(v + 1) # v -- root and cut point

def get_cut_points(g, n):

    visited = [False] * n
    cut_points = []
    h, dp = [0] * n, [0] * n

    for i in range(n):
        if not visited[i]:
            dfs(g, i, -1, visited, 0, cut_points, h, dp)
    return cut_points

if __name__=='__main__':
    
    n, m = map(int, input().split(' '))
    graph = []

    for i in range(n):
        graph.append([])
    
    for i in range(m):
        from_, to = map(int, input().split(' '))
        graph[from_ - 1].append(to - 1)
    
    answ = sorted(get_cut_points(graph, n))
    print(len(answ), *answ, sep = ' ')