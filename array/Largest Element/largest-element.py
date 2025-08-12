def largestElement(arr):
    max_val = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    print(max_val)


n = int(input())
arr = list(map(int, input().split()))
largestElement(arr)
