import sys
from collections import deque

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# 노드의 개수 N, 거리 질문 개수 M 입력
n, m = map(int, input().split())

# 트리를 인접 리스트 형태로 표현
# 각 노드에 (연결된 노드, 거리)를 함께 저장
graph = [[] for _ in range(n + 1)]

# N-1개의 간선 정보를 입력받아 인접 리스트에 저장
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def get_distance(start, end):
    """
    start 노드에서 end 노드까지의 거리를 BFS로 계산하는 함수
    """
    # BFS를 위한 큐(deque) 생성
    # 큐에는 (현재 노드, 시작점부터의 누적 거리)를 저장
    queue = deque([(start, 0)])
    
    # 방문 여부를 확인할 리스트
    visited = [False] * (n + 1)
    visited[start] = True
    
    while queue:
        # 큐에서 현재 노드와 누적 거리를 꺼냄
        now, dist = queue.popleft()
        
        # 목표 노드에 도달했다면, 거리를 반환하고 함수 종료
        if now == end:
            return dist
        
        # 현재 노드와 연결된 다른 노드들을 확인
        for next_node, weight in graph[now]:
            # 아직 방문하지 않은 노드라면
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, dist + weight))

# M개의 질문을 처리
for _ in range(m):
    start_node, end_node = map(int, input().split())
    print(get_distance(start_node, end_node))