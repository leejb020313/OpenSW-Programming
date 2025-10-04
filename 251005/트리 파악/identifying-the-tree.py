import sys
sys.setrecursionlimit(100000)

# 변수 선언 및 입력:
n = int(input())
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
depth = [0] * (n + 1)

# 리프노드 깊이의 총합
ans = 0

# n - 1개의 간선 정보를 입력받습니다.
for _ in range(n - 1):
    x, y = tuple(map(int, input().split()))

    # 간선 정보를 인접리스트에 넣어줍니다.
    edges[x].append(y)
    edges[y].append(x)


# DFS를 통해 리프노드와 리프노드의 깊이를 탐색합니다.
def dfs(x):
    global ans
    
    is_leaf = True

    for y in edges[x]:
        # 이미 방문한 노드는 스킵합니다.
        if visited[y]: 
            continue

        visited[y] = True

        # 하나라도 자식 노드가 있다면 리프 노드가 아닙니다.
        is_leaf = False
        
        # root로부터의 거리를 갱신합니다.
        depth[y] = depth[x] + 1

        dfs(y)

    # 리프노드라면, 해당 노드의 깊이를 더합니다.
    if is_leaf: 
        ans += depth[x]


# DFS를 통해 리프노드와 리프노드의 깊이를 탐색합니다.
visited[1] = True
dfs(1)

# 모든 리프노드의 깊이의 합이 짝수인지 홀수인지 판단해 정답을 출력합니다.
if ans % 2 == 1: 
    print(1)
else:
    print(0)
