import sys
sys.setrecursionlimit(50000)

# 변수 선언 및 입력:
n, d = tuple(map(int, input().split()))
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
dist_node = [0] * (n + 1)
dist = [0] * (n + 1)
max_dist = (0, 0)
last_node = 0

# n - 1개의 간선 정보를 입력받습니다.
for _ in range(n - 1):
    x, y, di = tuple(map(int, input().split()))
    edges[x].append((y, di))
    edges[y].append((x, di))


# 모든 노드의 정점을 탐색하는 DFS를 진행합니다.
def dfs(x):
    global max_dist, last_node

    for y, di in edges[x]:
        # 이미 방문한 정점이면 스킵합니다.
        if visited[y]: 
            continue

        visited[y] = True
        dist_node[y] = dist_node[x] + 1
        dist[y] = dist[x] + di

        cur_dist = (dist_node[y], -dist[y])

        # 현재 정점을 기준으로 가장 먼 노드를 찾습니다.
        # 지나는 간선의 수가 최대가 되도록 하며,
        # 동일한 경우 거리의 합이 최소가 되도록 합니다.
        if cur_dist > max_dist:
            max_dist = cur_dist
            last_node = y

        dfs(y)


# DFS를 통해 가장 먼 노드를 찾습니다.
visited[1] = True
dfs(1)

# 가장 먼 노드에서 시작해 다시 한번 DFS를 돌려 트리의 가장 긴 거리를 찾습니다.
for i in range(1, n + 1):
    visited[i] = False
    dist_node[i] = 0
    dist[i] = 0

visited[last_node] = True
dfs(last_node)

# 꼭 필요한 날짜의 수를 출력합니다.
print(1 + (-max_dist[1] - 1) // d)
