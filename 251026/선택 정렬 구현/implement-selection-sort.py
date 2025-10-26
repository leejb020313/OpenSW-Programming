n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(0,n-1):
    min = i
    for j in range(i,n-1):
        if arr[j] < arr[min]:
            tmp = arr[j]
            arr[j] = arr[min]
            arr[min] = tmp

print(*arr)