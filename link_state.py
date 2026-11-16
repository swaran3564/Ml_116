INF = 999
n = int(input("Enter no. of routers: "))
graph = [list(map(int, input().split())) for _ in range(n)]
src = int(input("Enter source router: "))

dist = [INF] * n
visited = [False] * n
dist[src] = 0

for _ in range(n):
    u = min((dist[i], i) for i in range(n) if not visited[i])[1]
    visited[u] = True
    for v in range(n):
        if dist[u] + graph[u][v] < dist[v]:
            dist[v] = dist[u] + graph[u][v]

print("Shortest distances:", dist)