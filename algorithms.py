# algorithms.py

def read_graph(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return adj


def graph_coloring_bruteforce(adj):
    n = len(adj)
    colors = [-1] * n
    best = [n + 1, None]

    def valid(node, color):
        return all(colors[v] != color for v in adj[node])

    def backtrack(node, used_colors):
        if used_colors >= best[0]:
            return
        if node == n:
            best[0] = used_colors
            best[1] = colors[:]
            return

        for c in range(used_colors):
            if valid(node, c):
                colors[node] = c
                backtrack(node + 1, used_colors)
                colors[node] = -1

        colors[node] = used_colors
        backtrack(node + 1, used_colors + 1)
        colors[node] = -1

    backtrack(0, 0)
    return best[0], best[1]


def greedy_coloring(adj):
    n = len(adj)
    colors = [-1] * n

    for u in range(n):
        used = {colors[v] for v in adj[u] if colors[v] != -1}
        c = 0
        while c in used:
            c += 1
        colors[u] = c

    return max(colors) + 1, colors


def dsatur_coloring(adj):
    n = len(adj)
    colors = [-1] * n
    saturation = [0] * n
    degrees = [len(adj[i]) for i in range(n)]

    def pick_node():
        return max(
            (i for i in range(n) if colors[i] == -1),
            key=lambda x: (saturation[x], degrees[x])
        )

    for _ in range(n):
        u = pick_node()
        used = {colors[v] for v in adj[u] if colors[v] != -1}
        c = 0
        while c in used:
            c += 1
        colors[u] = c

        for v in adj[u]:
            if colors[v] == -1:
                saturation[v] = len({colors[x] for x in adj[v] if colors[x] != -1})

    return max(colors) + 1, colors


def greedy_coloring_degree(adj):
    n = len(adj)
    degree = [(len(adj[i]), i) for i in range(n)]
    degree.sort(reverse=True)

    color = [-1] * n

    for _, u in degree:
        used = set()
        for v in adj[u]:
            if color[v] != -1:
                used.add(color[v])
        c = 0
        while c in used:
            c += 1
        color[u] = c

    num_colors = max(color) + 1
    return num_colors, color
