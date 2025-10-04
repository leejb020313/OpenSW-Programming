n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

for i in range(0,11):
    print(edges[i][0])