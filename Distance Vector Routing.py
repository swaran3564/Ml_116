
n = int(input("Enter number of routers: "))
print("Enter cost matrix (999 for no connection):")
d = [list(map(int, input().split())) for _ in range(n)]

for _ in range(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

print("\nDistance Vector Routing Table:")
for i in range(n):
    print("Router", i, ":", d[i])
