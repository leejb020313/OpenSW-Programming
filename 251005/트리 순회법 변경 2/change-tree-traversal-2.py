import sys
sys.setrecursionlimit(100000)

# 변수 선언 및 입력:
n = int(sys.stdin.readline())

# 트리를 전위 순회한 결과와 중위 순회한 결과를 입력받습니다.
pre_order = [0] + list(map(int, sys.stdin.readline().split()))
in_order = [0] + list(map(int, sys.stdin.readline().split()))

# 후위 순회 결과를 저장할 리스트와 카운터 초기화
post_order = [0] * (n + 1)
cnt = 1

# 해시 맵을 사용하여 in_order 배열의 값과 인덱스를 매핑
in_order_map = {}
for i in range(1, n + 1):
    in_order_map[in_order[i]] = i

# 트리의 전위 순회, 중위 순회 결과를 바탕으로 해당 서브트리에서
# 왼쪽 서브트리, 오른쪽 서브트리, 루트를 잘 관리하여 DFS합니다.
# 전위 순회의 [l, r] 정보와
# 중위 순회의 [l2, r2] 정보를 이용한 탐색을 진행합니다.
def dfs(l, r, l2, r2):
    global cnt

    # 탐색이 불가능한 종료조건에 해당합니다.
    if l > r: 
        return

    # l = r이 되면
    # 전위, 중위, 후위 순회 결과가 전부 단일 노드로서 동일해집니다.
    if l == r:
        post_order[cnt] = pre_order[l]
        cnt += 1
        return

    # 전위 순회는 (현재 노드, 왼쪽 서브 트리, 오른쪽 서브 트리)
    # 중위 순회는 (왼쪽 서브 트리, 현재 노드, 오른쪽 서브 트리)
    # 순이므로 전위 순회의 맨 앞 노드인 pre_order[l]과 일치하는
    # 중위 순회의 노드인 in_order[x]의 인덱스를 해시 맵에서 찾습니다.
    root_num = in_order_map[pre_order[l]]

    # 왼쪽 서브트리  현재 노드   오른쪽 서브트리 
    # --------- --------  ------------
    # [l2, ..., root_num, ..., ..., r2]
    # 왼쪽 서브트리의 크기를 계산합니다.
    lef_sz = root_num - l2
    # 오른쪽 서브트리의 크기를 계산합니다.
    rig_sz = r2 - root_num

    # 전위 순회 / 중위 순회의 왼쪽 서브 트리 정보를 이용하여 재귀적으로 탐색합니다.
    dfs(l + 1, l + lef_sz, l2, root_num - 1)

    # 전위 순회 / 중위 순회의 오른쪽 서브 트리 정보를 이용하여 재귀적으로 탐색합니다.
    dfs(l + lef_sz + 1, r, root_num + 1, r2)

    # 후위 순회의 경우 (왼쪽 서브 트리, 오른쪽 서브 트리, 현재 노드)
    # 순으로 순서가 구성되어야 하므로
    # 위의 두 재귀 함수 (왼쪽, 오른쪽) 탐색을 끝내고 난 이후에
    # 현재 노드의 위치 값을 적어줍니다.
    post_order[cnt] = pre_order[l]
    cnt += 1

# 트리의 전위 순회, 중위 순회 결과를 바탕으로 해당 서브트리에서
# 왼쪽 서브트리, 오른쪽 서브트리, 루트를 잘 관리하여 DFS합니다.
dfs(1, n, 1, n)

# 후위 순회의 번호를 순서대로 출력합니다.
print(' '.join(map(str, post_order[1:n+1])))
