def maximum_consecutive_ones(arr):
    cur = 0
    max_count = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            cur += 1
            if cur > max_count:
                max_count = cur
        else:
            cur = 0
    return max_count

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = maximum_consecutive_ones(arr)
    print(result)
