def left_rotate_by_k_places(arr, n, k):
    arr[:k] = reversed(arr[:k])
    arr[k:] = reversed(arr[k:])
    arr[:] = reversed(arr)

n, k = map(int, input().split())
k = k % n
arr = list(map(int, input().split()))
left_rotate_by_k_places(arr, n, k)
print(*arr)
