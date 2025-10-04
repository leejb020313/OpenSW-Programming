import sys
from collections import deque

# 빠른 입력을 위해 sys.stdin.readline 사용
# 재귀 깊이 제한을 늘려주면 DFS로도 풀 수 있습니다.
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline

def is_tree_component(start_node, visited, graph):
    """
    주어진 시작 노드로부터 연결된 요소가 트리인지 판별하는 함수.
    BFS를 사용하여 컴포넌트를 탐색하고, 정점과 간선의 수를 센다.
    """
    
    # 컴포넌트 탐색을 위한 큐
    queue = deque([start_node])
    visited[start_node] = True
    
    vertices_count = 0
    edges_sum_of_degrees = 0 # 간선은 각 정점의 차수의 합을 2로 나눈 것과 같다.
    
    while queue:
        node = queue.popleft()
        vertices_count += 1
        edges_sum_of_degrees += len(graph[node])
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                
    # 실제 간선의 수는 (모든 정점의 차수의 합) / 2
    edges_count = edges_sum_of_degrees // 2
    
    # 트리의 조건: (간선의 수) == (정점의 수 - 1)
    if edges_count == vertices_count - 1:
        return True
    else:
        return False

# 정점(N)과 간선(M)의 개수 입력
n, m = map(int, input().split())

# 인접 리스트로 그래프 표현
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문 여부 확인 리스트
visited = [False] * (n + 1)
tree_count = 0

# 1번부터 N번까지 모든 정점을 확인
for i in range(1, n + 1):
    # 아직 방문하지 않은 정점이라면, 새로운 연결 요소를 의미
    if not visited[i]:
        # 해당 연결 요소가 트리인지 판별
        if is_tree_component(i, visited, graph):
            tree_count += 1

# 최종 트리 개수 출력
print(tree_count)