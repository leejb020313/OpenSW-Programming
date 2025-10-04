import sys
sys.setrecursionlimit(100000)

# 변수 선언 및 입력:
n = int(input())

# 트리를 중위 순회한 결과와 후위 순회한 결과를 입력받습니다.
in_order = [0] + list(map(int, input().split()))
post_order = [0] + list(map(int, input().split()))

pre_order = [0] * (n + 1)
cnt = 1

# 트리의 후위 순회, 중위 순회 결과를 바탕으로 해당 서브트리에서
# 왼쪽 서브트리, 오른쪽 서브트리, 루트를 잘 관리하여 DFS합니다.
# 후위 순회의 [l, r] 정보와
# 중위 순회의 [l2, r2] 정보를 이용한 탐색을 진행합니다.
def dfs(l, r, l2, r2):
    global cnt
    
    # 탐색이 불가능한 종료조건에 해당합니다.
    if l > r: 
        return

    # l = r이 되면
    # 전위, 중위, 후위 순회 결과가 전부 단일 노드로서 동일해집니다.
    if l == r:
        pre_order[cnt] = post_order[l]
        cnt += 1
        return

    # 후위 순회는 (왼쪽 서브 트리, 오른쪽 서브 트리, 현재 노드)
    # 중위 순회는 (왼쪽 서브 트리, 현재 노드, 오른쪽 서브 트리)
    # 순이므로 후위 순회의 맨 뒤 노드인 post_order[r]과 일치하는
    # 중위 순회의 노드인 in_order[x]를 찾으면
    # 각각의 후위 순회 / 중위 순회 정보 중
    # 왼쪽 서브 트리 정보와 오른쪽 서브 트리 정보를 구분지어줄 수 있습니다.
    root_num = 0
    for i in range(l2, r2 + 1):
        if post_order[r] == in_order[i]:
            root_num = i

    # 왼쪽 서브트리  현재 노드   오른쪽 서브트리 
    #  -= 1 -= 1 -= 1 -= 1-  -= 1 -= 1 -= 1 -= 1   -= 1 -= 1 -= 1 -= 1 -= 1 -= 1
    # [l2, ..., root_num, ..., ..., r2]
    # 왼쪽 / 오른쪽 서브 트리의 크기를 계산합니다.
    lef_sz = root_num - l2
    rig_sz = r2 - root_num

    # 전위 순회의 경우 (현재 노드, 왼쪽 서브 트리, 오른쪽 서브 트리)
    # 순으로 순서가 구성되어야 하므로
    # 위의 두 재귀 함수 (왼쪽, 오른쪽) 탐색을 진행하기 전에
    # 현재 노드의 위치 값을 적어줍니다.
    pre_order[cnt] = post_order[r]
    cnt += 1

    # 후위 순회 / 중위 순회의 왼쪽 서브 트리 정보를 이용하여 재귀적으로 탐색합니다.
    dfs(l, l + lef_sz - 1, l2, root_num - 1)

    # 후위 순회 / 중위 순회의 오른쪽 서브 트리 정보를 이용하여 재귀적으로 탐색합니다.
    dfs(l + lef_sz, r - 1, root_num + 1, r2)

   
# 트리의 후위 순회, 중위 순회 결과를 바탕으로 해당 서브트리에서
# 왼쪽 서브트리, 오른쪽 서브트리, 루트를 잘 관리하여 DFS합니다.
dfs(1, n, 1, n)

# 전위순회의 번호를 순서대로 출력합니다.
for i in range(1, n + 1):
    print(pre_order[i], end=" ")
