import sys

# 재귀 허용 깊이를 넉넉하게 늘려줍니다.
sys.setrecursionlimit(10**5) 

def postorder(start, end):
    """
    전위 순회 리스트의 특정 구간을 후위 순회로 변환하여 출력하는 함수
    (이 함수의 로직은 이전과 동일하게 올바릅니다)
    """
    if start > end:
        return
    
    root = preorder_list[start]
    
    split_index = end + 1
    for i in range(start + 1, end + 1):
        if preorder_list[i] > root:
            split_index = i
            break
            
    postorder(start + 1, split_index - 1)
    postorder(split_index, end)
    print(root)


# --- ★★★★★ 완전히 수정된 입력 처리 방식 ★★★★★ ---
# 첫 줄을 읽어 노드의 개수 N을 얻습니다.
try:
    n = int(sys.stdin.readline())
except (ValueError, IndexError):
    n = 0 # 입력이 비었을 경우를 대비

# N개의 줄을 읽어 preorder_list를 구성합니다.
preorder_list = []
for _ in range(n):
    try:
        preorder_list.append(int(sys.stdin.readline()))
    except (ValueError, IndexError):
        break
# --- 여기까지 수정 ---

# 전체 리스트를 대상으로 후위 순회 시작
if preorder_list:
    postorder(0, len(preorder_list) - 1)