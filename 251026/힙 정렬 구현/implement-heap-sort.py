n = int(input())
arr = [0] + list(map(int, input().split()))

def heapify(n,i):
    largest = i
    left = i*2
    right = i*2+1

    if left <= n and arr[left] > arr[largest]:
        largest = left
    
    if right <= n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(n,largest)

def heap_sort():
    for i in range(n//2,0,-1):
        heapify(n,i)

    for i in range(n,1,-1):
        arr[1],arr[i] = arr[i],arr[1]
        heapify(i-1,1)

heap_sort()

print(*arr[1:])