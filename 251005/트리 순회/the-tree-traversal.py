# 변수 선언 및 입력:
n = int(input())
left, right = {}, {}
for _ in range(n):
    x, l, r = tuple(input().split())
    left[x] = l
    right[x] = r


def pre_order(x):
    # .이면 존재하지 않으므로 빠져나갑니다.
    if x == '.':
        return

    print(x, end="")
    pre_order(left[x])
    pre_order(right[x])


def in_order(x):
    # .이면 존재하지 않으므로 빠져나갑니다.
    if x == '.':
        return

    in_order(left[x])
    print(x, end="")
    in_order(right[x])


def post_order(x):
    # .이면 존재하지 않으므로 빠져나갑니다.
    if x == '.':
        return

    post_order(left[x])
    post_order(right[x])
    print(x, end="")


# 전위 순회를 진행합니다.
pre_order('A')
print()
# 중위 순회를 진행합니다.
in_order('A')
print()
# 후위 순회를 진행합니다.
post_order('A')
print()
