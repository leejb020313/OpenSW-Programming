n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

visited = [False] * (n + 1)
parent = [0] * (n + 1)

for _ in range(n - 1):
    x, y = tuple(map(int, input().split()))
    edges[x].append(y)
    edges[y].append(x)

def traversal(x):
    for y in edges[x]:
        if not visited[y]:
            visited[y] = True
            parent[y] = x
            traversal(y)

visited[1] = True
traversal(1)

for i in range(2, n + 1):
    print(parent[i])