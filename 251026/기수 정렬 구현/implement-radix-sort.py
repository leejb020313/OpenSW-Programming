n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
max_count = 1
for i in range(len(arr)):
    count = 0
    num = arr[i]
    while num > 0 :
        num //= 10
        count += 1
    if max_count < count:
        max_count = count 

divisor = 1
for pos in range(max_count):
    arr_new = [[] for _ in range(10)]
    
    for num in arr:
        digit = (num // divisor) % 10
        arr_new[digit].append(num)

    store_arr = []
    for i in range(10):
        for j in range(len(arr_new[i])):
            store_arr.append(arr_new[i][j])
    
    arr = store_arr
    divisor *= 10

print(*arr)