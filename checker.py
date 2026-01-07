# checker.py

def check_coloring(adj, colors):
    for u in range(len(adj)):
        for v in adj[u]:
            if colors[u] == colors[v]:
                return False
    return True
