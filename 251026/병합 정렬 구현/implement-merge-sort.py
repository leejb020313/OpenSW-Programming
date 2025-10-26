n = int(input())
arr = list(map(int, input().split()))
 
def merge(low,mid,high):
    merged_arr = []
    left = low
    right = mid+1
    
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            merged_arr.append(arr[left])
            left += 1
    
        else:
            merged_arr.append(arr[right])
            right += 1
    
    while left <= mid:
        merged_arr.append(arr[left])
        left += 1
    
    while right <= high:
        merged_arr.append(arr[right])
        right += 1
    
    for i in range(len(merged_arr)):
        arr[low + i] = merged_arr[i]

def merge_sort(low,high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(low,mid)
        merge_sort(mid+1,high)
        merge(low,mid,high)

merge_sort(0, n - 1)


print(*arr)