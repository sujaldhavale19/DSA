def find_missing_number(arr, n):
    sum1 = 0
    for i in range(len(arr)):
        sum1 += arr[i]
    sum2 = (n * (n + 1)) // 2
    return sum2 - sum1
n = int(input())
arr = list(map(int, input().split()))
missing = find_missing_number(arr, n)
print(missing)
