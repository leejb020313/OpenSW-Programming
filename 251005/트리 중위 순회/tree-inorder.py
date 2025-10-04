# 변수 선언 및 입력:
k = int(input())

# 2^i은 (1 << i)로 쉽계 계산이 가능합니다.
n = (1 << k) - 1

tree_num = [0] * (n + 1)
cnt = 1

# a라는 배열에 중위 순회 순서를 입력받습니다.
a = [0] + list(map(int, input().split()))


# 중위 순회를 진행하여 각 트리의 위치에 맞는 번호를 채워 넣습니다.
def in_order(x):
    global cnt

    # n보다 큰 노드는 없습니다. 빠져나갑니다.
    if x > n:
        return

    in_order(x * 2)
    tree_num[x] = a[cnt]
    cnt += 1
    in_order(x * 2 + 1)

   
# 중위 순회를 진행하여 각 트리의 위치에 맞는 번호를 채워 넣습니다.
in_order(1)

# 트리의 구조에 맞게 출력을 진행합니다.
for i in range(1, k + 1):
    for j in range(1 << (i - 1), 1 << i):
        print(tree_num[j], end=" ")
    print()
