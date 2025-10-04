import sys
sys.setrecursionlimit(200000)

# 변수 선언 및 입력:
n = int(input())
left_num = [0] * (n + 1)
right_num = [0] * (n + 1)
ans = 0

# 각 노드의 왼쪽 자식노드와 오른쪽 자식노드를 입력받습니다.
for i in range(1, n + 1):
    left_num[i], right_num[i] = tuple(map(int, input().split()))

k = int(input())


# 트리의 루트 노드에서부터 시작해
# k번째 공이 어느 노드로 내려갈지 DFS로 계산합니다.
def dfs(x, ball_num):
    global ans
    
    # 리프 노드에 도착하면 해당 위치가 답이 됩니다.
    if left_num[x] == -1 and right_num[x] == -1:
        ans = x
        return

    # 왼쪽 노드가 비어있다면 오른쪽으로 이동합니다.
    if left_num[x] == -1:
        dfs(right_num[x], ball_num)
    # 오른쪽 노드가 비어있다면 왼쪽으로 이동합니다.
    elif right_num[x] == -1:
        dfs(left_num[x], ball_num)
    # 홀수 개의 공이 남았다면
    # 왼쪽으로 1개 더 공이 떨어지게 되며
    # 우리는 왼쪽으로 이동해야 합니다.
    elif ball_num % 2 == 1:
        dfs(left_num[x], (ball_num + 1) // 2)
    # 짝수 개의 공이 남았다면
    # 왼쪽, 오른쪽 공이 동일하게 떨어지게 되며
    # 우리는 오른쪽으로 이동해야 합니다.
    else:
        dfs(right_num[x], ball_num // 2)

   
# 트리의 루트 노드에서부터 시작해
# k번째 공이 어느 노드로 내려갈지 DFS로 계산합니다.
dfs(1, k)

# 공이 마지막에 멈추는 노드의 번호를 출력합니다.
print(ans)
