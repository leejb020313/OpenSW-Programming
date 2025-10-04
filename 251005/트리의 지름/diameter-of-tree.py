import sys
from collections import deque

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# 노드의 개수 N 입력
n = int(input())

# 트리를 인접 리스트 형태로 표현할 리스트 초기화
# 각 노드에 (연결된 노드, 간선 가중치)를 함께 저장
graph = [[] for _ in range(n + 1)]

# N-1개의 간선 정보를 입력받아 인접 리스트에 저장
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def bfs(start_node):
    """
    지정한 노드에서 시작하여 각 노드까지의 거리를 계산하고,
    가장 먼 노드와 그 거리를 반환하는 함수
    """
    # 각 노드까지의 거리를 저장할 리스트 (-1은 미방문 상태)
    distance = [-1] * (n + 1)
    
    # BFS를 위한 큐(deque) 생성
    queue = deque()
    
    # 시작 노드를 큐에 넣고 방문 처리
    queue.append((start_node, 0))
    distance[start_node] = 0
    
    # 가장 먼 노드와 거리를 기록할 변수
    max_distance = 0
    farthest_node = start_node
    
    while queue:
        # 큐에서 현재 노드와 현재까지의 거리를 꺼냄
        now, dist = queue.popleft()
        
        # 현재 노드와 연결된 다른 노드들을 확인
        for next_node, weight in graph[now]:
            # 아직 방문하지 않은 노드라면
            if distance[next_node] == -1:
                # 거리 갱신 및 큐에 추가
                new_dist = dist + weight
                distance[next_node] = new_dist
                queue.append((next_node, new_dist))
                
                # 현재까지의 최대 거리보다 길다면 갱신
                if new_dist > max_distance:
                    max_distance = new_dist
                    farthest_node = next_node
                    
    return farthest_node, max_distance

# 알고리즘 실행
# 1. 임의의 점(1번 노드)에서 가장 먼 노드(A)를 찾는다.
node_A, _ = bfs(1)

# 2. 노드 A에서 가장 먼 노드(B)까지의 거리를 찾는다. 이 거리가 트리의 지름이 된다.
_, diameter = bfs(node_A)

# 결과 출력
print(diameter)