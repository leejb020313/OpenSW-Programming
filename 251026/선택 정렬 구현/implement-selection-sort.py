n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
min = arr[0]
for i in range(0,len(arr)-1):
    if arr[i] < min:
        tmp = arr[i]
        arr[i] = min
        min = tmp

print(*arr)