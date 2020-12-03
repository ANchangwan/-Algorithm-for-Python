def dfs(v, d):
    global Max
    if d > Max:
        Max = d
    visited[v] = 1
    for w in G[v]:
        if not visited[w]:
            dfs(w, d + 1)
            visited[w] = 0


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    G = [[] for _ in range(n + 1)]

    for _ in range(m):
        x, y = map(int, input().split())
        G[x].append(y)
        G[y].append(x)
    Max = 0
    for i in range(1, n + 1):
        visited = [0 for _ in range(n + 1)]
        dfs(i, 1)
    print(f'#{test_case} {Max}')
