n = int(input())
arr = list(map(int, input().split()))
merged_arr = [0] * n 

def merge(low,mid,high):
    front = low
    back = mid+1
    pos = low
    
    while front <= mid and back <= high:
        if arr[front] <= arr[back]:
            merged_arr[pos] = arr[front]
            front += 1
            pos += 1
    
        else:
            merged_arr[pos] = arr[back]
            back += 1
            pos += 1
    
    while front <= mid:
        merged_arr[pos] = arr[front]
        front += 1
        pos += 1
    
    while back <= high:
        merged_arr[pos] = arr[back]
        back += 1
        pos += 1
    
    for i in range(low,high+1):
        arr[i] = merged_arr[i]

def merge_sort(low,high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(low,mid)
        merge_sort(mid+1,high)
        merge(low,mid,high)

merge_sort(0, n - 1)


print(*arr)