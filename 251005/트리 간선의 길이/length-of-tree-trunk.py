# 변수 선언 및 입력:
n, k = tuple(map(int, input().split()))
par = [0] * (n + 1)
finding_node = -1
ans = 0

# n개의 수열 원소를 입력받습니다.
a = [0] + list(map(int, input().split()))
for i in range(1, n + 1):
    if a[i] == k: 
        finding_node = i

# n개의 원소를 바탕으로 트리를 만들어줍니다.
par_node = 0
for i in range(2, n + 1):
    # 두 원소가 연속하지 않는다면
    # 부모 노드 index를 1 증가시킵니다.
    if a[i] > a[i - 1] + 1:
        par_node += 1
    
    # i번 노드의 부모 노드는 par_node(index)가 됩니다.
    par[i] = par_node

# 부모 노드는 다르면서 
# 부모의 부모 노드가 같은 경우를 찾습니다.
# 해당 노드들은 사촌이 됩니다.
for i in range(1, n + 1):
    # 부모의 부모 노드가 존재하지 않는 경우에는 패스합니다.
    if not par[par[i]] or not par[par[finding_node]]:
        continue

    if par[i] != par[finding_node] and par[par[i]] == par[par[finding_node]]:
        ans += 1

# 사촌 노드의 개수를 출력합니다.
print(ans)
