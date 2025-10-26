n = int(input())
arr = list(map(int, input().split()))

for i in range(0,len(arr)-1):
    for j in range(0,len(arr)-1-i):
        if arr[j] > arr[j+1]:
            tmp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = tmp

print(*arr)